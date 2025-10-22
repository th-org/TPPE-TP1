from .time import Time
from .rodada import Rodada
class Campeonato:
    def __init__(self, nome: str):
        self.nome = nome
        self.times: list[Time] = []
        self.rodadas: list[Rodada] = []

    def adicionar_time(self, time: Time):
        self.times.append(time)

    def criar_rodada(self, numero: int) -> Rodada:
        r = Rodada(numero)
        self.rodadas.append(r)
        return r

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