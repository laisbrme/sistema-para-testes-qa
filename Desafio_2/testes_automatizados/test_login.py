'''
Função para testes automatizados para o fluxo de login do sistema.
'''
import time

# Caso de teste CT-01:
def test_login_CT01(browser, path_login):
    browser.get(path_login)  # Atualize o caminho conforme necessário
    time.sleep(1)
    browser.find_element("id", "btn-entrar").click()
    time.sleep(3)
    assert "login" in browser.current_url or "Login" in browser.page_source

# Caso de teste CT-02:
def test_login_CT02(browser, path_login):
    browser.get(path_login)  # Atualize o caminho conforme necessário
    browser.find_element("id", "email").send_keys("admin@admin.com")
    time.sleep(1)
    browser.find_element("id", "btn-entrar").click()
    time.sleep(3)
    assert "login" in browser.current_url or "Login" in browser.page_source

# Caso de teste CT-03:
def test_login_CT03(browser, path_login):
    browser.get(path_login)  # Atualize o caminho conforme necessário
    browser.find_element("id", "senha").send_keys("admin@123")
    time.sleep(1)
    browser.find_element("id", "btn-entrar").click()
    time.sleep(3)
    assert "login" in browser.current_url or "Login" in browser.page_source

# Caso de teste CT-04:
def test_login_CT04(browser, path_login):
    browser.get(path_login)  # Atualize o caminho conforme necessário
    browser.find_element("id", "email").send_keys("admin")
    time.sleep(1)
    browser.find_element("id", "senha").send_keys("admin")
    time.sleep(1)
    browser.find_element("id", "btn-entrar").click()
    time.sleep(3)
    assert "login" in browser.current_url or "Login" in browser.page_source

# Caso de teste CT-05:
def test_login_CT05(browser, path_login):
    browser.get(path_login)  # Atualize o caminho conforme necessário
    browser.find_element("id", "email").send_keys(" admin@admin.com ")
    time.sleep(5)
    browser.find_element("id", "senha").send_keys("admin@123")
    time.sleep(1)
    browser.find_element("id", "btn-entrar").click()
    time.sleep(3)
    assert "produtos" in browser.current_url or "Produtos" in browser.page_source

# Caso de teste CT-06:
def test_login_sucesso(browser, path_login):
    browser.get(path_login)  # Atualize o caminho conforme necessário
    browser.find_element("id", "email").send_keys("admin@admin.com")
    time.sleep(1)
    browser.find_element("id", "senha").send_keys("admin@123")
    time.sleep(1)
    browser.find_element("id", "btn-entrar").click()
    time.sleep(3)
    assert "produtos" in browser.current_url or "Produtos" in browser.page_source