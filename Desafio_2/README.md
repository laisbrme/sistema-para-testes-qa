# Testes Automatizados - Desafio 2

Este diretório contém o projeto de automação de testes utilizando Selenium, conforme o Desafio 2 da disciplina SQA.

## Como executar

1. Instale as dependências:
   ```
   pip install -r testes_automatizados/requirements.txt
   ```
2. Execute os testes:
   ```
   pytest testes_automatizados/
   ```

## Estrutura

- `conftest.py`: Configurações e fixtures do pytest.
- `test_login.py`: Testes automatizados para o fluxo de login.
- `test_produtos.py`: Testes automatizados para o cadastro e manipulação de produtos.
- `requirements.txt`: Dependências do projeto de automação.