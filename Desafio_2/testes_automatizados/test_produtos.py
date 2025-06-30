'''
Função para testes automatizados para cadastro de produtos.
'''

import time

# Caso de teste CT-07:
def test_produto_CT07(browser, path_login):
    browser.get(path_login)  # Atualize o caminho conforme necessário
    browser.find_element("id", "email").send_keys("admin@admin.com")
    browser.find_element("id", "senha").send_keys("admin@123")
    browser.find_element("id", "btn-entrar").click()
    # time.sleep(1)

    browser.find_element("class name", "nav-link").click()
    # time.sleep(3)
    assert "login" in browser.current_url or "Login" in browser.page_source

# Caso de teste CT-08:
def test_produto_CT08(browser, path_login):
    browser.get(path_login)  # Atualize o caminho conforme necessário
    browser.find_element("id", "email").send_keys("admin@admin.com")
    browser.find_element("id", "senha").send_keys("admin@123")
    browser.find_element("id", "btn-entrar").click()
    # time.sleep(1)

    browser.find_element("id", "btn-adicionar").click()
    browser.find_element("id", "btn-adicionar").click()
    # time.sleep(1)
    browser.find_element("id", "codigo").send_keys("001")
    # time.sleep(1)
    browser.find_element("id", "nome").send_keys("Produto Teste")
    # time.sleep(1)
    browser.find_element("id", "quantidade").send_keys("10")
    # time.sleep(1)
    browser.find_element("id", "valor").send_keys("99.99")
    # time.sleep(1)
    browser.find_element("id", "data").send_keys("25062025")
    # time.sleep(1)
    browser.find_element("id", "btn-salvar").click()
    # time.sleep(1)
    browser.find_element("id", "btn-sair").click()
    # time.sleep(3)
    assert "Produto Teste" in browser.page_source

# Caso de teste CT-09:
def test_produto_CT09(browser, path_login):
    browser.get(path_login)  # Atualize o caminho conforme necessário
    browser.find_element("id", "email").send_keys("admin@admin.com")
    browser.find_element("id", "senha").send_keys("admin@123")
    browser.find_element("id", "btn-entrar").click()
    # time.sleep(1)

    browser.find_element("id", "btn-adicionar").click()
    browser.find_element("id", "btn-adicionar").click()
    # time.sleep(1)
    browser.find_element("id", "btn-salvar").click()
    # time.sleep(3)
    assert "Todos os campos são obrigatórios para o cadastro!" in browser.page_source
    
# Caso de teste CT-10:
def test_produto_CT10(browser, path_login):
    browser.get(path_login)  # Atualize o caminho conforme necessário
    browser.find_element("id", "email").send_keys("admin@admin.com")
    browser.find_element("id", "senha").send_keys("admin@123")
    browser.find_element("id", "btn-entrar").click()
    # time.sleep(1)

    quantidade = -10
    valor = -15

    browser.find_element("id", "btn-adicionar").click()
    browser.find_element("id", "btn-adicionar").click()
    # time.sleep(1)
    browser.find_element("id", "codigo").send_keys("001")
    # time.sleep(1)
    browser.find_element("id", "nome").send_keys("Produto Teste")
    # time.sleep(1)
    browser.find_element("id", "quantidade").send_keys(quantidade)
    # time.sleep(1)
    browser.find_element("id", "valor").send_keys(valor)
    # time.sleep(1)
    browser.find_element("id", "data").send_keys("25062025")
    # time.sleep(1)
    browser.find_element("id", "btn-salvar").click()
    # time.sleep(1)
    browser.find_element("id", "btn-sair").click()
    # time.sleep(3)
    assert not (quantidade < 0) or not (valor < 0)

# Caso de teste CT-11:
def test_produto_CT11(browser, path_login):
    browser.get(path_login)  # Atualize o caminho conforme necessário
    browser.find_element("id", "email").send_keys("admin@admin.com")
    browser.find_element("id", "senha").send_keys("admin@123")
    browser.find_element("id", "btn-entrar").click()
    # time.sleep(1)

    browser.find_element("id", "btn-adicionar").click()
    browser.find_element("id", "btn-adicionar").click()
    # time.sleep(1)
    browser.find_element("id", "codigo").send_keys("001")
    # time.sleep(1)
    browser.find_element("id", "nome").send_keys("Produto Teste")
    # time.sleep(1)
    browser.find_element("id", "quantidade").send_keys(10)
    # time.sleep(1)
    browser.find_element("id", "valor").send_keys(15)
    # time.sleep(1)
    browser.find_element("id", "data").send_keys("32132025")
    # time.sleep(1)
    browser.find_element("id", "btn-salvar").click()
    # time.sleep(1)
    browser.find_element("id", "btn-sair").click()
    # time.sleep(3)
    assert "2025-13-32" not in browser.page_source
