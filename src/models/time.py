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
        if n < 0:
            raise ValueError("Gols marcados não podem ser negativos")
        self.gols_marcados += n

    def registrar_gols_sofridos(self, n: int):
        if n < 0:
            raise ValueError("Gols sofridos não podem ser negativos")
        self.gols_sofridos += n

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