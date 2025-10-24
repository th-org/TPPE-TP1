class Time:
    def __init__(self, nome: str):
        self.nome = nome
        self.pontos = 0
        self.vitorias = 0
        self.empates = 0
        self.derrotas = 0
        self.gols_marcados = 0
        self.gols_sofridos = 0

    def registrar_gols_marcados(self, n: int):
        self._validar_gols(n)
        self.gols_marcados += n

    def registrar_gols_sofridos(self, n: int):
        self._validar_gols(n)
        self.gols_sofridos += n

    def _validar_gols(self, n: int):
        if n < 0:
            raise ValueError("Gols não podem ser negativos")

    def adicionar_vitoria(self):
        self.vitorias += 1
        self.pontos += 3

    def adicionar_empate(self):
        self.empates += 1
        self.pontos += 1

    def adicionar_derrota(self):
        self.derrotas += 1

    def saldo_gols(self) -> int:
        return self.gols_marcados - self.gols_sofridos