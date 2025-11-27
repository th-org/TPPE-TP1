from .time import Time
from .rodada import Rodada
from .partida import Partida
from .gerador_rodadas import GeradorRodadas

class Campeonato:
    def __init__(self, nome: str):
        self.nome = nome
        self.times: list[Time] = []
        self.rodadas: list[Rodada] = []

    def adicionar_time(self, time: Time):
        self.times.append(time)

    def criar_rodada(self, numero: int = None) -> Rodada | None:
        """
        Cria rodadas para o campeonato.
        
        Se um número for fornecido, cria apenas uma rodada vazia com esse número.
        Se nenhum número for fornecido, gera todas as rodadas do campeonato
        usando o algoritmo round-robin (turno e returno).
        
        Args:
            numero: Número da rodada a ser criada (opcional)
            
        Returns:
            A rodada criada (quando numero é fornecido) ou None
            
        Raises:
            ValueError: Se não houver times suficientes (mínimo 2)
        """
        if numero is not None:
            rodada = Rodada(numero)
            self.rodadas.append(rodada)
            return rodada
        
        # Usa a classe GeradorRodadas para encapsular a lógica complexa
        gerador = GeradorRodadas(self.times, self.rodadas)
        gerador.gerar_todas_rodadas()

    def classificacao(self) -> list[Time]:
        return sorted(
            self.times,
            key=self._criterios_desempate,
            reverse=True
        )
    
    def _criterios_desempate(self, time: Time) -> tuple:
        return (
            time.pontos,
            time.vitorias,
            time.saldo_gols(),
            time.gols_marcados
        )

    def buscar_time(self, nome: str) -> Time | None:
        for t in self.times:
            if t.nome == nome:
                return t
        return None

    def gerar_tabela_final(self) -> str:
        if len(self.times) == 0:
            return "Nenhum time cadastrado no campeonato."
        
        classificacao = self.classificacao()
        
        tabela = self._gerar_cabecalho_tabela()
        tabela += self._gerar_linhas_times(classificacao)
        tabela += self._gerar_rodape_tabela()
        tabela += self._gerar_legenda()
        
        return tabela
    
    def _gerar_cabecalho_tabela(self) -> str:
        largura_total = 95
        cabecalho = "=" * largura_total + "\n"
        cabecalho += f"{self.nome.upper()} - CLASSIFICAÇÃO FINAL\n".center(largura_total)
        cabecalho += "=" * largura_total + "\n"
        
        cabecalho += f"{'Pos':<5} {'Time':<20} {'P':<5} {'V':<5} {'E':<5} {'D':<5} "
        cabecalho += f"{'GP':<5} {'GC':<5} {'SG':<6} {'Zona'}\n"
        cabecalho += "-" * largura_total + "\n"
        
        return cabecalho
    
    def _gerar_linhas_times(self, classificacao: list[Time]) -> str:
        linhas = ""
        for i, time in enumerate(classificacao, 1):
            linhas += self._formatar_linha_time(i, time)
        return linhas
    
    def _formatar_linha_time(self, posicao: int, time: Time) -> str:

        zona = self._identificar_zona(posicao)
        saldo_str = self._formatar_saldo_gols(time.saldo_gols())
        
        linha = f"{posicao:<5} {time.nome:<20} {time.pontos:<5} {time.vitorias:<5} "
        linha += f"{time.empates:<5} {time.derrotas:<5} {time.gols_marcados:<5} "
        linha += f"{time.gols_sofridos:<5} {saldo_str:<6} {zona}\n"
        
        return linha
    
    def _formatar_saldo_gols(self, saldo: int) -> str:
        
        return f"+{saldo}" if saldo > 0 else str(saldo)
    
    def _gerar_rodape_tabela(self) -> str:
        
        largura_total = 95
        return "=" * largura_total + "\n"
    
    def _gerar_legenda(self) -> str:
        
        legenda = "\nLegenda:\n"
        legenda += "  🏆 CAMPEÃO - Campeão brasileiro\n"
        legenda += "  🌎 Libertadores - Classificados para Copa Libertadores (1º ao 6º)\n"
        legenda += "  🏆 Sul-Americana - Classificados para Copa Sul-Americana (7º ao 12º)\n"
        legenda += "  ⬇️  REBAIXADO - Rebaixados para Série B (17º ao 20º)\n"
        
        return legenda
    
    def _identificar_zona(self, posicao: int) -> str:
    
        if posicao == 1:
            return "🏆 CAMPEÃO"
        elif posicao <= 6:
            return "🌎 Libertadores"
        elif posicao <= 12:
            return "🏆 Sul-Americana"
        elif posicao >= 17:
            return "⬇️  REBAIXADO"
        else:
            return ""
