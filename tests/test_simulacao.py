import pytest
import random

from src.models.campeonato import Campeonato
from src.models.time import Time


def criar_campeonato_20_times():
    campeonato = Campeonato("Brasileirão Série A 2025")
    
    times = [
    "Atlético-MG",
    "Bahia",
    "Botafogo",
    "Bragantino",
    "Ceará",
    "Corinthians",
    "Cruzeiro",
    "Flamengo",
    "Fluminense",
    "Fortaleza",
    "Grêmio",
    "Internacional",
    "Juventude",
    "Mirassol",
    "Palmeiras",
    "Santos",
    "São Paulo",
    "Sport",
    "Vasco",
    "Vitória"
]

    
    for nome in times:
        campeonato.adicionar_time(Time(nome))
    
    return campeonato


def simular_placar_aleatorio():
    placares_possiveis = [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (0, 1), (1, 1), (2, 1), (3, 1),
        (0, 2), (1, 2), (2, 2), (3, 2),
        (0, 3), (1, 3), (2, 3),
        (0, 4), (1, 4), (2, 4)
    ]
    return random.choice(placares_possiveis)


def test_gerar_38_rodadas_com_20_times():
    campeonato = criar_campeonato_20_times()
    campeonato.criar_rodada()
    
    assert len(campeonato.rodadas) == 38, \
        f"Esperado 38 rodadas, mas encontrou {len(campeonato.rodadas)}"


def test_cada_rodada_tem_10_partidas():
    campeonato = criar_campeonato_20_times()
    campeonato.criar_rodada()
    
    for i, rodada in enumerate(campeonato.rodadas, start=1):
        assert len(rodada.partidas) == 10, \
            f"Rodada {i} deveria ter 10 partidas, mas tem {len(rodada.partidas)}"


def test_todos_os_times_jogam_em_cada_rodada():
    campeonato = criar_campeonato_20_times()
    campeonato.criar_rodada()
    
    for i, rodada in enumerate(campeonato.rodadas, start=1):
        times_na_rodada = set()
        for partida in rodada.partidas:
            times_na_rodada.add(partida.mandante)
            times_na_rodada.add(partida.visitante)
        
        assert len(times_na_rodada) == 20, \
            f"Rodada {i} não tem todos os 20 times jogando"


def test_total_de_380_partidas_no_campeonato():
    campeonato = criar_campeonato_20_times()
    campeonato.criar_rodada()
    
    total_partidas = sum(len(rodada.partidas) for rodada in campeonato.rodadas)
    
    assert total_partidas == 380, \
        f"Esperado 380 partidas no total, mas encontrou {total_partidas}"


def test_cada_time_joga_38_partidas():
    campeonato = criar_campeonato_20_times()
    campeonato.criar_rodada()
    
    contagem_jogos = {time: 0 for time in campeonato.times}
    
    for rodada in campeonato.rodadas:
        for partida in rodada.partidas:
            contagem_jogos[partida.mandante] += 1
            contagem_jogos[partida.visitante] += 1
    
    for time, num_jogos in contagem_jogos.items():
        assert num_jogos == 38, \
            f"{time.nome} jogou {num_jogos} partidas, esperado 38"


def test_cada_time_joga_19_vezes_em_casa():
    campeonato = criar_campeonato_20_times()
    campeonato.criar_rodada()
    
    jogos_em_casa = {time: 0 for time in campeonato.times}
    
    for rodada in campeonato.rodadas:
        for partida in rodada.partidas:
            jogos_em_casa[partida.mandante] += 1
    
    for time, num_jogos in jogos_em_casa.items():
        assert num_jogos == 19, \
            f"{time.nome} foi mandante em {num_jogos} jogos, esperado 19"


def test_simulacao_completa_com_resultados():
    campeonato = criar_campeonato_20_times()
    campeonato.criar_rodada()
    
    random.seed(42)
    
    for rodada in campeonato.rodadas:
        for partida in rodada.partidas:
            gols_mandante, gols_visitante = simular_placar_aleatorio()
            partida.registrar_placar(gols_mandante, gols_visitante)
    
    for time in campeonato.times:
        total_jogos = time.vitorias + time.empates + time.derrotas
        assert total_jogos == 38, \
            f"{time.nome}: total de jogos inconsistente ({total_jogos})"
        
        pontos_calculados = (time.vitorias * 3) + (time.empates * 1)
        assert time.pontos == pontos_calculados, \
            f"{time.nome}: pontos inconsistentes"
        
        assert time.saldo_gols() == time.gols_marcados - time.gols_sofridos, \
            f"{time.nome}: saldo de gols inconsistente"


def test_classificacao_apos_simulacao_completa():
    campeonato = criar_campeonato_20_times()
    campeonato.criar_rodada()
    
    random.seed(42)
    for rodada in campeonato.rodadas:
        for partida in rodada.partidas:
            gols_mandante, gols_visitante = simular_placar_aleatorio()
            partida.registrar_placar(gols_mandante, gols_visitante)
    
    classificacao = campeonato.classificacao()
    
    assert len(classificacao) == 20, \
        f"Classificação deveria ter 20 times, mas tem {len(classificacao)}"
    
    for i in range(len(classificacao) - 1):
        time_atual = classificacao[i]
        time_seguinte = classificacao[i + 1]
        
        assert time_atual.pontos >= time_seguinte.pontos, \
            f"Classificação incorreta: {time_atual.nome} ({time_atual.pontos}pts) " \
            f"está acima de {time_seguinte.nome} ({time_seguinte.pontos}pts)"


def test_campeao_tem_mais_pontos_ou_melhor_criterio():
    campeonato = criar_campeonato_20_times()
    campeonato.criar_rodada()
    
    random.seed(42)
    for rodada in campeonato.rodadas:
        for partida in rodada.partidas:
            gols_mandante, gols_visitante = simular_placar_aleatorio()
            partida.registrar_placar(gols_mandante, gols_visitante)
    
    classificacao = campeonato.classificacao()
    campeao = classificacao[0]
    
    for time in classificacao[1:]:
        criterios_campeao = (campeao.pontos, campeao.vitorias, 
                            campeao.saldo_gols(), campeao.gols_marcados)
        criterios_time = (time.pontos, time.vitorias, 
                         time.saldo_gols(), time.gols_marcados)
        
        assert criterios_campeao >= criterios_time, \
            f"Campeão {campeao.nome} não é melhor que {time.nome}"
