"""
Suíte de testes que executa todos os testes do projeto.

Para executar:
    pytest tests/all_tests.py -v
    
ou simplesmente:
    pytest tests/ -v
"""
import pytest


def test_suite_completa():
    """
    Executa toda a suíte de testes do projeto.
    
    Esta suíte inclui:
    - Testes de modelos (Time, Partida, Rodada, Campeonato)
    - Testes de classificação e critérios de desempate
    - Testes de sorteio de rodadas
    - Testes de registro de resultados
    """
    exit_code = pytest.main([
        'tests/',
        '-v',
        '--tb=short',
        '--disable-warnings'
    ])
    assert exit_code == 0, "Alguns testes falharam na suíte completa"


if __name__ == '__main__':
    # Permite executar diretamente: python tests/all_tests.py
    pytest.main([
        'tests/',
        '-v',
        '--tb=short'
    ])
