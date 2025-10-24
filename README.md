## 🧪 Suíte de Testes Completa — TPPE TP1

Este projeto utiliza **[pytest](https://docs.pytest.org/)** para garantir a qualidade e o correto funcionamento de todos os componentes do sistema.  
A suíte de testes foi projetada para ser simples de executar, cobrindo desde os **modelos** até as **simulações completas** do campeonato.

---

### ⚙️ Estrutura dos Testes

Os testes estão localizados dentro da pasta [`tests/`](tests/) e são executados em conjunto pelo arquivo [`all_tests.py`](tests/all_tests.py).

| Arquivo | Descrição | Nº de Testes |
|:-------------------------|:---------------------------------------------|:---:|
| `test_modelos.py` | Testes unitários dos modelos básicos (`Time`, `Partida`, `Rodada`, `Campeonato`) | 6 |
| `test_classificacao.py` | Testes de ordenação e critérios de desempate | 6 |
| `test_sorteio.py` | Testes de geração de rodadas sem repetição | 4 |
| `test_resultado.py` | Testes de registro de placares e atualização de resultados | 6 |
| `test_simulacao.py` | Testes de simulação completa das 38 rodadas do campeonato | 9 |
| `test_tabela.py` | Testes da geração da tabela de classificação final, campeões, zonas e estatísticas | 11 |
| **Total** |  | **42** |

---

### ▶️ Como Executar os Testes

Você pode executar toda a suíte ou testes específicos usando os comandos abaixo:

#### 🧩 1. Executar todos os testes
```bash
pytest tests/ -v

```

#### 🧱 2. Executar apenas o arquivo principal (tests/all_tests.py)

```bash
pytest tests/all_tests.py -v

```

#### 🧾 3. Gerar relatório de cobertura

```bash
pytest tests/ --cov=src --cov-report=html

```

#### 🐍 4. Executar diretamente via Python

```bash
python tests/all_tests.py

```

#### ⚡ 5. Parar no primeiro erro encontrado

```bash
pytest tests/ -x

```

#### ⚡ 🎯 6. Executar testes específicos

```bash
pytest tests/test_classificacao.py -v
pytest tests/test_simulacao.py::test_gerar_38_rodadas_com_20_times -v


```

#### 🧠 O que o arquivo all_tests.py faz

O script tests/all_tests.py funciona como um ponto de entrada para executar toda a suíte de testes.
Ele utiliza a API do pytest para rodar os testes com opções configuradas:

```python
exit_code = pytest.main([
    'tests/',
    '-v',
    '--tb=short',
    '--disable-warnings'
])
assert exit_code == 0, "Alguns testes falharam na suíte completa"

```

Caso algum teste falhe, o script retorna uma mensagem de erro, garantindo que o pipeline ou o ambiente de CI detecte falhas automaticamente.

### Script de Demonstração da Tabela de Classificação Final

Este script serve para demonstrar a **tabela de classificação final**.

#### Como Executar

Use o seguinte comando no terminal:

```bash
python demo_tabela.py

```

### Requisitos 
 - Python 3.10+
 - pytest


#### Instalação:

```bash
pip install pytest

```