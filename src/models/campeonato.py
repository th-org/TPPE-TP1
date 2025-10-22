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

    def gerar_rodadas(self) -> None:
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