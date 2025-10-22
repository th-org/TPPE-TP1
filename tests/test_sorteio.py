import pytest

from src.models.campeonato import Campeonato
from src.models.time import Time

# teste de models/campeonato.py
def criar_campeonato_basico():
    camp = Campeonato("Brasileirão")
    camp.adicionar_time(Time("Flamengo"))
    camp.adicionar_time(Time("Vasco"))
    camp.adicionar_time(Time("Botafogo"))
    camp.adicionar_time(Time("Fluminense"))
    return camp

# teste de models/campeonato.py
def test_gera_rodadas_corretamente():
    camp = criar_campeonato_basico()
    camp.gerar_rodadas()
    # se for ter um número impar de times
    n_times = len(camp.times)
    total_rodadas_esperado = 0
    if n_times % 2 == 0:
        total_rodadas_esperado = (n_times - 1) * 2
    else:
        total_rodadas_esperado = n_times * 2
    assert len(camp.rodadas) == total_rodadas_esperado

# teste de models/campeonato.py
def test_numero_partidas_por_rodada():
    camp = criar_campeonato_basico()
    camp.gerar_rodadas()
    for rodada in camp.rodadas:
        assert len(rodada.partidas) == len(camp.times) // 2

# teste de models/campeonato.py
def test_todos_times_jogam_por_rodada():
    camp = criar_campeonato_basico()
    camp.gerar_rodadas()
    for rodada in camp.rodadas:
        participantes = set()
        for partida in rodada.partidas:
            participantes.add(partida.mandante)
            participantes.add(partida.visitante)
        assert participantes == set(camp.times)

# teste de models/campeonato.py
def test_sem_confrontos_duplicados():
    camp = criar_campeonato_basico()
    camp.gerar_rodadas()
    todos_confrontos = set()
    for rodada in camp.rodadas:
        for partida in rodada.partidas:
            confronto = (partida.mandante, partida.visitante) 
            assert confronto not in todos_confrontos, f"Confronto duplicado: {partida.mandante.nome} x {partida.visitante.nome}"
            todos_confrontos.add(confronto)
    assert len(todos_confrontos) == len(camp.times) * (len(camp.times) - 1)
