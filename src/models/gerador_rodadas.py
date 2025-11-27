from .rodada import Rodada
from .partida import Partida
from .time import Time

class GeradorRodadas:

    
    def __init__(self, times: list[Time], rodadas_existentes: list[Rodada]):
       
        self.times_originais = times
        self.rodadas = rodadas_existentes
        self.times_processados = []
        self.numero_rodada_atual = 1
        
    def gerar_todas_rodadas(self) -> None:
        
        self._validar_times()
        self._preparar_times()
        self._calcular_parametros()
        self._gerar_turno()
        self._gerar_returno()
    
    def criar_rodada_vazia(self, numero: int) -> Rodada:
       
        rodada = Rodada(numero)
        self.rodadas.append(rodada)
        return rodada
    
    def _validar_times(self) -> None:
        
        if len(self.times_originais) < 2:
            raise ValueError()
    
    def _preparar_times(self) -> None:
        
        self.times_processados = self.times_originais.copy()
        
        if len(self.times_processados) % 2 != 0:
            self.times_processados.append(None)
    
    def _calcular_parametros(self) -> None:
        
        self.n_times = len(self.times_processados)
        self.rodadas_por_turno = self.n_times - 1
        self.time_fixo = self.times_processados[0]
        self.times_rotativos = self.times_processados[1:]
    
    def _gerar_turno(self) -> None:
        for _ in range(self.rodadas_por_turno):
            rodada = self.criar_rodada_vazia(self.numero_rodada_atual)
            self.numero_rodada_atual += 1
            
            self._adicionar_partida_time_fixo(rodada)
            self._adicionar_partidas_times_rotativos(rodada)
            self._rotacionar_times()
    
    def _adicionar_partida_time_fixo(self, rodada: Rodada) -> None:
        
        if self.time_fixo is not None and self.times_rotativos[0] is not None:
            rodada.adicionar_partida(Partida(self.time_fixo, self.times_rotativos[0]))
    
    def _adicionar_partidas_times_rotativos(self, rodada: Rodada) -> None:
        
        for j in range(1, self.n_times // 2):
            time_casa = self.times_rotativos[j]
            time_fora = self.times_rotativos[-j]
            
            if time_casa is not None and time_fora is not None:
                rodada.adicionar_partida(Partida(time_casa, time_fora))
    
    def _rotacionar_times(self) -> None:
        
        self.times_rotativos = [self.times_rotativos[-1]] + self.times_rotativos[:-1]
    
    def _gerar_returno(self) -> None:
        
        rodadas_turno = self.rodadas_por_turno
        
        for i in range(rodadas_turno):
            rodada_ida = self.rodadas[i]
            rodada_volta = self.criar_rodada_vazia(self.numero_rodada_atual)
            self.numero_rodada_atual += 1
            
            for partida in rodada_ida.partidas:
                rodada_volta.adicionar_partida(
                    Partida(partida.visitante, partida.mandante)
                )
