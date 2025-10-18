from .partida import Partida


class Rodada:
	def __init__(self, numero: int):
		self.numero = numero
		self.partidas: list[Partida] = []

	def adicionar_partida(self, partida: Partida):
		self.partidas.append(partida)

	def resultados(self):
		return [(p.mandante.nome, p.gols_mandante, p.visitante.nome, p.gols_visitante) for p in self.partidas]
