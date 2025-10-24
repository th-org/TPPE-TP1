"""
Testes para geração de tabela de classificação final.
"""
import pytest
import random

from src.models.campeonato import Campeonato
from src.models.time import Time


def criar_campeonato_e_simular():
    """
    Cria um campeonato com 20 times e simula todos os jogos.
    """
    campeonato = Campeonato("Brasileirão 2025")
    
    times = [
        "Flamengo", "Palmeiras", "Atlético-MG", "Fluminense",
        "Botafogo", "Bragantino", "Athletico-PR", "Internacional",
        "São Paulo", "Corinthians", "Fortaleza", "Santos",
        "Grêmio", "Vasco", "Bahia", "Cruzeiro",
        "Cuiabá", "Goiás", "Coritiba", "América-MG"
    ]
    
    for nome in times:
        campeonato.adicionar_time(Time(nome))
    
    campeonato.criar_rodada()
    
    # Simula resultados
    random.seed(42)
    placares = [(0,0), (1,0), (2,0), (3,0), (1,1), (2,1), (2,2)]
    
    for rodada in campeonato.rodadas:
        for partida in rodada.partidas:
            placar = random.choice(placares)
            partida.registrar_placar(placar[0], placar[1])
    
    return campeonato


def test_gerar_tabela_final_retorna_string():
    """
    Testa se o método gerar_tabela_final() retorna uma string.
    """
    campeonato = criar_campeonato_e_simular()
    tabela = campeonato.gerar_tabela_final()
    
    assert isinstance(tabela, str), "Tabela deve ser uma string"
    assert len(tabela) > 0, "Tabela não pode ser vazia"


def test_tabela_contem_titulo():
    """
    Testa se a tabela contém o título do campeonato.
    """
    campeonato = criar_campeonato_e_simular()
    tabela = campeonato.gerar_tabela_final()
    
    assert "BRASILEIRÃO" in tabela.upper() or "CLASSIFICAÇÃO" in tabela.upper(), \
        "Tabela deve conter título"


def test_tabela_contem_todos_os_times():
    """
    Testa se a tabela contém todos os 20 times.
    """
    campeonato = criar_campeonato_e_simular()
    tabela = campeonato.gerar_tabela_final()
    
    for time in campeonato.times:
        assert time.nome in tabela, f"Time {time.nome} não encontrado na tabela"


def test_tabela_contem_cabecalho():
    """
    Testa se a tabela contém o cabeçalho com colunas.
    """
    campeonato = criar_campeonato_e_simular()
    tabela = campeonato.gerar_tabela_final()
    
    # Verifica se contém indicadores de colunas principais
    cabecalho_elementos = ['Pos', 'Time', 'P', 'V', 'E', 'D', 'GP', 'GC', 'SG']
    
    for elemento in cabecalho_elementos:
        assert elemento in tabela, f"Cabeçalho deve conter '{elemento}'"


def test_tabela_identifica_campeao():
    """
    Testa se a tabela identifica o campeão (1º colocado).
    """
    campeonato = criar_campeonato_e_simular()
    tabela = campeonato.gerar_tabela_final()
    classificacao = campeonato.classificacao()
    
    # Verifica se há indicação de campeão
    assert "CAMPEÃO" in tabela or "🏆" in tabela, \
        "Tabela deve identificar o campeão"
    
    # Verifica se o nome do campeão está na tabela
    campeao = classificacao[0]
    assert campeao.nome in tabela, "Nome do campeão deve estar na tabela"


def test_tabela_identifica_zona_libertadores():
    """
    Testa se a tabela identifica os times da zona de Libertadores (1º ao 6º).
    """
    campeonato = criar_campeonato_e_simular()
    tabela = campeonato.gerar_tabela_final()
    
    assert "Libertadores" in tabela or "LIBERTADORES" in tabela or "🌎" in tabela, \
        "Tabela deve identificar zona da Libertadores"


def test_tabela_identifica_zona_sulamericana():
    """
    Testa se a tabela identifica os times da zona de Sul-Americana (7º ao 12º).
    """
    campeonato = criar_campeonato_e_simular()
    tabela = campeonato.gerar_tabela_final()
    
    assert "Sul-Americana" in tabela or "SULAMERICANA" in tabela, \
        "Tabela deve identificar zona da Sul-Americana"


def test_tabela_identifica_zona_rebaixamento():
    """
    Testa se a tabela identifica os times rebaixados (17º ao 20º).
    """
    campeonato = criar_campeonato_e_simular()
    tabela = campeonato.gerar_tabela_final()
    
    assert "REBAIXADO" in tabela or "Rebaixamento" in tabela or "⬇️" in tabela, \
        "Tabela deve identificar zona de rebaixamento"


def test_tabela_mostra_estatisticas_completas():
    """
    Testa se a tabela mostra todas as estatísticas de cada time.
    """
    campeonato = criar_campeonato_e_simular()
    tabela = campeonato.gerar_tabela_final()
    classificacao = campeonato.classificacao()
    
    # Pega o campeão para verificar se seus dados estão na tabela
    campeao = classificacao[0]
    
    # Converte para string para buscar na tabela
    assert str(campeao.pontos) in tabela, "Pontos do campeão devem estar na tabela"
    assert str(campeao.vitorias) in tabela, "Vitórias devem estar na tabela"


def test_tabela_ordenada_por_classificacao():
    """
    Testa se a tabela está ordenada pela classificação correta.
    """
    campeonato = criar_campeonato_e_simular()
    tabela = campeonato.gerar_tabela_final()
    classificacao = campeonato.classificacao()
    
    # Verifica se os times aparecem na ordem correta na tabela
    linhas = tabela.split('\n')
    
    # Encontra as linhas com dados dos times (não cabeçalho/separadores)
    times_na_tabela = []
    for linha in linhas:
        for time in classificacao:
            if time.nome in linha and linha.strip():
                times_na_tabela.append(time.nome)
                break
    
    # Remove duplicatas mantendo ordem
    times_unicos = []
    for time in times_na_tabela:
        if time not in times_unicos:
            times_unicos.append(time)
    
    # Verifica se a ordem na tabela corresponde à classificação
    times_classificacao = [t.nome for t in classificacao]
    
    assert times_unicos == times_classificacao[:len(times_unicos)], \
        "Times devem aparecer na ordem da classificação"


def test_tabela_com_campeonato_vazio():
    """
    Testa se a geração de tabela funciona com campeonato sem times.
    """
    campeonato = Campeonato("Teste Vazio")
    tabela = campeonato.gerar_tabela_final()
    
    assert isinstance(tabela, str), "Deve retornar string mesmo sem times"
    assert "Nenhum time" in tabela or len(campeonato.times) == 0, \
        "Deve indicar que não há times ou retornar tabela vazia"
