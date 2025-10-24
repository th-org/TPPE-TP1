from .time import Time
class Partida:
	def __init__(self, mandante: Time, visitante: Time):
		self.mandante = mandante
		self.visitante = visitante
		self.gols_mandante = 0
		self.gols_visitante = 0
		self.jogada = False

	def registrar_placar(self, gols_m: int, gols_v: int):
		if self.jogada:
			raise ValueError("Placar já registrado para esta partida")
			
		if gols_m < 0 or gols_v < 0:
			raise ValueError("Gols não podem ser negativos")

		
		# atualizar gols individuais
		self.gols_mandante = gols_m
		self.gols_visitante = gols_v

		# atualizar estatísticas dos times
		for time, gols_marcados, gols_sofridos in [(self.mandante, gols_m, gols_v),
			(self.visitante, gols_v, gols_m)]:
			time.registrar_gols_marcados(gols_marcados)
			time.registrar_gols_sofridos(gols_sofridos)

		# definir vencedor/empate
		diferenca = gols_m - gols_v
		if diferenca > 0:
			self.mandante.adicionar_vitoria()
			self.visitante.adicionar_derrota()
		elif diferenca < 0:
			self.visitante.adicionar_vitoria()
			self.mandante.adicionar_derrota()
		else:
			self.mandante.adicionar_empate()
			self.visitante.adicionar_empate()

		self.jogada = True

	def vencedor(self):
		if not self.jogada:
			return None
		if self.gols_mandante > self.gols_visitante:
			return self.mandante
		if self.gols_visitante > self.gols_mandante:
			return self.visitante
		return None

	def resultado(self, mandante, visitante) -> str:
		return f"{mandante.nome} {self.gols_mandante}x{self.gols_visitante} {visitante.nome}"

