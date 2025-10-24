import pytest


def test_suite_completa():
    exit_code = pytest.main([
        'tests/',
        '-v',
        '--tb=short',
        '--disable-warnings'
    ])
    assert exit_code == 0, "Alguns testes falharam na suíte completa"


if __name__ == '__main__':
    pytest.main([
        'tests/',
        '-v',
        '--tb=short'
    ])
