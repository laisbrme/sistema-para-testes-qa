# Testes Automatizados - Desafio 2

Este diretório contém o projeto de automação de testes utilizando Selenium, conforme o Desafio 2 da disciplina SQA.

## Como executar

1. Instale as dependências:
   ```
   pip install -r testes_automatizados/requirements.txt
   ```
2. Execute os testes:
   ```
   cd testes_automatizados/
   pytest
   ```
3. Para executar os testes em paralelo, utilize:
   ```
   pytest test_login.py
   ```
4. Para um teste específico, utilize:
   ```
   pytest test_produtos.py::test_produto_CT08
   ```

## Estrutura

- `conftest.py`: Configurações e fixtures do pytest.
- `test_login.py`: Testes automatizados para o fluxo de login.
- `test_produtos.py`: Testes automatizados para o cadastro e manipulação de produtos.
- `requirements.txt`: Dependências do projeto de automação.

### Observações importantes

- Os testes automatizados utilizam o navegador Microsoft Edge. Certifique-se de que o Edge e o Edge WebDriver estejam instalados e configurados no PATH do sistema.
- O sistema a ser testado deve estar disponível em `http://127.0.0.1:3000/Desafio_1/sistema/login.html`. Basta iniciar o servidor local para que os testes funcionem corretamente:
   ```
   Desafio_1\sistema\login.html
   ```
- As pastas `__pycache__` e `.pytest_cache` são geradas automaticamente pelo Python/pytest e podem ser ignoradas.