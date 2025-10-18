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

    def classificacao(self):
        # ordena por pontos, depois vitorias, saldo e gols marcados
        return sorted(self.times, key=lambda t: (t.pontos, t.vitorias, t.saldo_gols(), t.gols_marcados), reverse=True)

    def buscar_time(self, nome: str) -> Time | None:
        for t in self.times:
            if t.nome == nome:
                return t
        return None