'''
Função para testes automatizados para cadastro, edição e exclusão de produtos.
'''

def test_cadastro_produto(browser, path_login):
    browser.get(path_login)  # Atualize o caminho conforme necessário
    browser.find_element("id", "email").send_keys("admin@admin.com")
    browser.find_element("id", "senha").send_keys("admin@123")
    browser.find_element("id", "btnEntrar").click()
    browser.find_element("id", "btnCriar").click()
    browser.find_element("id", "codigo").send_keys("001")
    browser.find_element("id", "nome").send_keys("Produto Teste")
    browser.find_element("id", "quantidade").send_keys("10")
    browser.find_element("id", "valor").send_keys("99.99")
    browser.find_element("id", "btnSalvar").click()
    assert "Produto Teste" in browser.page_source