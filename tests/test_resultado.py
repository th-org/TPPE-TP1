import pytest

from src.models.time import Time
from src.models.partida import Partida

def test_registrar_placar_vitoria_mandante():
    flamengo = Time("Flamengo")
    corinthians = Time("Corinthians")
    p = Partida(flamengo, corinthians)

    p.registrar_placar(3, 1)

    assert flamengo.pontos == 3
    assert flamengo.vitorias == 1
    assert flamengo.empates == 0
    assert flamengo.derrotas == 0
    assert flamengo.gols_marcados == 3
    assert flamengo.gols_sofridos == 1
    assert flamengo.saldo_gols() == 2

    assert corinthians.pontos == 0
    assert corinthians.vitorias == 0
    assert corinthians.empates == 0
    assert corinthians.derrotas == 1
    assert corinthians.gols_marcados == 1
    assert corinthians.gols_sofridos == 3
    assert corinthians.saldo_gols() == -2

    assert p.jogada is True
    assert p.vencedor() is flamengo

def test_registrar_placar_vitoria_visitante():
    corinthians = Time("Corinthians")
    flamengo = Time("Flamengo")
    p = Partida(corinthians, flamengo)

    p.registrar_placar(0, 4)

    assert corinthians.pontos == 0
    assert corinthians.vitorias == 0
    assert corinthians.empates == 0
    assert corinthians.derrotas == 1
    assert corinthians.gols_marcados == 0
    assert corinthians.gols_sofridos == 4
    assert corinthians.saldo_gols() == -4

    assert flamengo.pontos == 3
    assert flamengo.vitorias == 1
    assert flamengo.empates == 0
    assert flamengo.derrotas == 0
    assert flamengo.gols_marcados == 4
    assert flamengo.gols_sofridos == 0
    assert flamengo.saldo_gols() == 4

    assert p.jogada is True
    assert p.vencedor() is flamengo

def test_nao_deve_registrar_placar_duas_vezes():
    flamengo = Time("Flamengo")
    corinthians = Time("Corinthians")
    p = Partida(flamengo, corinthians)

    p.registrar_placar(2, 0)

    with pytest.raises(ValueError, match="Placar já registrado"):
        p.registrar_placar(3, 1)

def test_nao_deve_registrar_gols_negativos():
    flamengo = Time("Flamengo")
    corinthians = Time("Corinthians")
    p = Partida(flamengo, corinthians)

    with pytest.raises(ValueError, match="Gols não podem ser negativos"):
        p.registrar_placar(-1, 0)

    with pytest.raises(ValueError, match="Gols não podem ser negativos"):
        p.registrar_placar(0, -5)

def test_vencedor_antes_da_partida():
    flamengo = Time("Flamengo")
    corinthians = Time("Corinthians")
    p = Partida(flamengo, corinthians)

    assert p.jogada is False
    assert p.vencedor() is None

def test_registrar_placar_empate():
    flamengo = Time("Flamengo")
    corinthians = Time("Corinthians")
    p = Partida(flamengo, corinthians)

    p.registrar_placar(1, 1)

    assert flamengo.pontos == 1
    assert flamengo.vitorias == 0
    assert flamengo.empates == 1
    assert flamengo.derrotas == 0
    assert flamengo.gols_marcados == 1
    assert flamengo.gols_sofridos == 1
    assert flamengo.saldo_gols() == 0

    assert corinthians.pontos == 1
    assert corinthians.vitorias == 0
    assert corinthians.empates == 1
    assert corinthians.derrotas == 0
    assert corinthians.gols_marcados == 1
    assert corinthians.gols_sofridos == 1
    assert corinthians.saldo_gols() == 0

    assert p.jogada is True
    assert p.vencedor() is None