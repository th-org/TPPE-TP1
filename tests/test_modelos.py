import pytest

from src.models.time import Time
from src.models.partida import Partida
from src.models.campeonato import Campeonato

# teste de models/time.py
def test_criacao_time():
    t = Time("Corinthians")
    assert t.nome == "Corinthians"
    assert t.pontos == 0
    assert t.vitorias == 0
    assert t.empates == 0
    assert t.derrotas == 0
    assert t.gols_marcados == 0
    assert t.gols_sofridos == 0
    assert t.saldo_gols() == 0

# teste de models/time.py
def test_registro_gols_e_saldo():
    t = Time("Corinthians")
    t.registrar_gols_marcados(10)
    t.registrar_gols_sofridos(4)
    assert t.gols_marcados == 10
    assert t.gols_sofridos == 4
    assert t.saldo_gols() == 6

# teste de models/time.py
def test_vitoria_empate_derrota():
    t = Time("Corinthians")
    t.adicionar_vitoria()
    assert t.vitorias == 1
    assert t.pontos == 3

    t.adicionar_empate()
    assert t.empates == 1
    assert t.pontos == 4

    t.adicionar_derrota()
    assert t.derrotas == 1
    assert t.pontos == 4

# teste de models/partida.py
def test_partida_vencedor_e_pontuacao():
    a = Time("Corinthians")
    b = Time("Corinthians Sub-20")
    p = Partida(a, b)
    p.registrar_placar(3, 1)

    assert p.vencedor() is a
    assert a.pontos == 3
    assert a.vitorias == 1

    assert b.derrotas == 1
    assert b.pontos == 0

    assert a.gols_marcados == 3
    assert a.gols_sofridos == 1

    assert b.gols_marcados == 1
    assert b.gols_sofridos == 3

    assert a.saldo_gols() == 2
    assert b.saldo_gols() == -2

    assert p.resultado(a, b) == "Corinthians 3x1 Corinthians Sub-20"

# teste de models/campeonato.py
def test_campeonato_classificacao_basica():
    c = Campeonato("Brasileirao")
    t1 = Time("Corinthians")
    t2 = Time("Corinthians Sub-20")
    
    c.adicionar_time(t1)
    c.adicionar_time(t2)
    p = c.criar_rodada(1)
    partida = Partida(t1, t2)
    partida.registrar_placar(2, 0)
    p.adicionar_partida(partida)
    cls = c.classificacao()
    assert cls[0] is t1
    assert cls[1] is t2

# teste de models/campeonato.py
def test_busca_time():
        c = Campeonato("Brasileirao")
        t1 = Time("Corinthians")
        t2 = Time("Vasco")
        c.adicionar_time(t1)
        c.adicionar_time(t2)

        encontrado = c.buscar_time("Corinthians")
        assert encontrado is t1

        nao_encontrado = c.buscar_time("Corinthians Sub-20")
        assert nao_encontrado is None