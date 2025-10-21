import pytest

from src.models.time import Time
from src.models.campeonato import Campeonato


def test_classificacao_ordenada_por_pontos():
	
	c = Campeonato("Brasileirao")
	time_6pts = Time("Flamengo")
	time_3pts = Time("Palmeiras")
	time_0pts = Time("Santos")

	
	c.adicionar_time(time_0pts)
	c.adicionar_time(time_6pts)
	c.adicionar_time(time_3pts)

	
	time_6pts.adicionar_vitoria()
	time_6pts.adicionar_vitoria()

	
	time_3pts.adicionar_vitoria()

	

	cls = c.classificacao()
	
	
	assert cls[0] is time_6pts
	assert cls[1] is time_3pts
	assert cls[2] is time_0pts


def test_classificacao_desempate_vitorias():
	c = Campeonato("Brasileirao")
	t1 = Time("Corinthians")
	t2 = Time("Flamengo")

	# t1: 1 vitória = 3 pontos
	t1.adicionar_vitoria()

	# t2: 3 empates = 3 pontos, mas 0 vitórias
	t2.adicionar_empate()
	t2.adicionar_empate()
	t2.adicionar_empate()

	c.adicionar_time(t1)
	c.adicionar_time(t2)

	cls = c.classificacao()
	assert cls[0] is t1
	assert cls[1] is t2


def test_classificacao_desempate_saldo_gols():
	c = Campeonato("Brasileirao")
	t1 = Time("Palmeiras")
	t2 = Time("Santos")

	# ambos com 1 ponto (1 empate) e 0 vitórias
	t1.adicionar_empate()
	t2.adicionar_empate()

	# definir gols (saldo): t1 saldo 2, t2 saldo 0
	t1.registrar_gols_marcados(3)
	t1.registrar_gols_sofridos(1)

	t2.registrar_gols_marcados(2)
	t2.registrar_gols_sofridos(2)

	c.adicionar_time(t1)
	c.adicionar_time(t2)

	cls = c.classificacao()
	assert cls[0] is t1
	assert cls[1] is t2


def test_classificacao_desempate_gols_marcados():
	c = Campeonato("Brasileirao")
	t1 = Time("Vasco")
	t2 = Time("Botafogo")

	# ambos com mesmos pontos e vitórias
	t1.adicionar_empate()
	t2.adicionar_empate()

	# mesmos saldo, mas t2 marcou mais gols
	# saldo 1: t1 -> 2-1, t2 -> 3-2
	t1.registrar_gols_marcados(2)
	t1.registrar_gols_sofridos(1)

	t2.registrar_gols_marcados(3)
	t2.registrar_gols_sofridos(2)

	c.adicionar_time(t1)
	c.adicionar_time(t2)

	cls = c.classificacao()
	assert cls[0] is t2
	assert cls[1] is t1


def test_classificacao_multiplos_empates_tres_times():
	"""
	Três times com mesmos pontos iniciais. Verifica desempates em cadeia:
	- Time A e Time B empates resolvidos por vitórias
	- Empate final entre B e C resolvido por saldo/gols
	"""
	c = Campeonato("Brasileirao")
	a = Time("Fluminense")
	b = Time("Cruzeiro")
	d = Time("Atletico-MG")

	# Todos com 3 pontos (1 vitória cada)
	a.adicionar_vitoria()
	b.adicionar_vitoria()
	d.adicionar_vitoria()

	# Ajustar saldo/gols para forçar ordem: B > A > C
	# B: saldo 5 (6-1)
	b.registrar_gols_marcados(6)
	b.registrar_gols_sofridos(1)

	# A: saldo 2 (4-2)
	a.registrar_gols_marcados(4)
	a.registrar_gols_sofridos(2)

	# C: saldo 1 (3-2)
	d.registrar_gols_marcados(3)
	d.registrar_gols_sofridos(2)

	c.adicionar_time(a)
	c.adicionar_time(b)
	c.adicionar_time(d)

	cls = c.classificacao()
	assert cls[0] is b
	assert cls[1] is a
	assert cls[2] is d


def test_classificacao_empate_total_ordem_estavel():
	#Se todos os critérios forem iguais, a ordenação deve ser estável
	#(preservar a ordem de inserção).
	c = Campeonato("Brasileirao")
	t1 = Time("Internacional")
	t2 = Time("Gremio")
	t3 = Time("Coritiba")

	# Nenhum gol, nenhum ponto: todos iguais
	c.adicionar_time(t1)
	c.adicionar_time(t2)
	c.adicionar_time(t3)

	cls = c.classificacao()
	# stable sort: deve manter a ordem de inserção
	assert cls[0] is t1
	assert cls[1] is t2
	assert cls[2] is t3

