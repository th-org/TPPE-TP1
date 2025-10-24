from .time import Time
from .rodada import Rodada
from .partida import Partida

class Campeonato:
    def __init__(self, nome: str):
        self.nome = nome
        self.times: list[Time] = []
        self.rodadas: list[Rodada] = []

    def adicionar_time(self, time: Time):
        self.times.append(time)

    def criar_rodada(self, numero: int = None) -> None:
        if numero is not None:
            r = Rodada(numero)
            self.rodadas.append(r)
            return r
        
        if len(self.times) < 2:
            raise ValueError()

        times = self.times.copy()

        if len(times) % 2 != 0:
            times.append(None)

        n = len(times)
        rodadas_ida = n - 1
        fixo = times[0]
        jogos = times[1:]
        numero_rodada = 1

        # ida
        for _ in range(rodadas_ida):
            rodada = self.criar_rodada(numero_rodada)
            numero_rodada += 1

            if fixo is not None and jogos[0] is not None:
                rodada.adicionar_partida(Partida(fixo, jogos[0]))

            for j in range(1, n // 2):
                casa = jogos[j]
                fora = jogos[-j]
                if casa is not None and fora is not None:
                    rodada.adicionar_partida(Partida(casa, fora))
            # jogam todos contra todos
            jogos = [jogos[-1]] + jogos[:-1]

        # volta
        for i in range(rodadas_ida):
            rodada_ida = self.rodadas[i]
            rodada_volta = self.criar_rodada(numero_rodada)
            numero_rodada += 1

            for partida in rodada_ida.partidas:
                rodada_volta.adicionar_partida(Partida(partida.visitante, partida.mandante))

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
        """
        Gera tabela de classificação final formatada para console.
        
        A tabela inclui:
        - Posição, nome do time, pontos, vitórias, empates, derrotas
        - Gols marcados, gols sofridos e saldo de gols
        - Identificação de zonas especiais:
          * 1º lugar: Campeão 🏆
          * 2º ao 6º: Libertadores 🌎
          * 7º ao 12º: Sul-Americana 🏆
          * 17º ao 20º: Rebaixados ⬇️
        
        Returns:
            str: Tabela formatada para impressão em console
        """
        if len(self.times) == 0:
            return "Nenhum time cadastrado no campeonato."
        
        classificacao = self.classificacao()
        
        # Cabeçalho
        largura_total = 95
        tabela = "=" * largura_total + "\n"
        tabela += f"{self.nome.upper()} - CLASSIFICAÇÃO FINAL\n".center(largura_total)
        tabela += "=" * largura_total + "\n"
        
        # Colunas
        tabela += f"{'Pos':<5} {'Time':<20} {'P':<5} {'V':<5} {'E':<5} {'D':<5} "
        tabela += f"{'GP':<5} {'GC':<5} {'SG':<6} {'Zona'}\n"
        tabela += "-" * largura_total + "\n"
        
        # Dados dos times
        for i, time in enumerate(classificacao, 1):
            # Determina a zona do time
            zona = self._identificar_zona(i)
            
            # Formata os dados
            saldo = time.saldo_gols()
            saldo_str = f"+{saldo}" if saldo > 0 else str(saldo)
            
            linha = f"{i:<5} {time.nome:<20} {time.pontos:<5} {time.vitorias:<5} "
            linha += f"{time.empates:<5} {time.derrotas:<5} {time.gols_marcados:<5} "
            linha += f"{time.gols_sofridos:<5} {saldo_str:<6} {zona}\n"
            
            tabela += linha
        
        tabela += "=" * largura_total + "\n"
        
        # Legenda
        tabela += "\nLegenda:\n"
        tabela += "  🏆 CAMPEÃO - Campeão brasileiro\n"
        tabela += "  🌎 Libertadores - Classificados para Copa Libertadores (1º ao 6º)\n"
        tabela += "  🏆 Sul-Americana - Classificados para Copa Sul-Americana (7º ao 12º)\n"
        tabela += "  ⬇️  REBAIXADO - Rebaixados para Série B (17º ao 20º)\n"
        
        return tabela
    
    def _identificar_zona(self, posicao: int) -> str:
        """
        Identifica a zona especial do time baseado em sua posição.
        
        Args:
            posicao: Posição do time na classificação (1-20)
            
        Returns:
            str: Identificação da zona especial
        """
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
