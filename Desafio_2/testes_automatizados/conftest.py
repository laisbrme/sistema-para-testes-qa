'''
Este arquivo de configuração é utilizado pelo pytest para definir 
fixtures (função especial usada para preparar e fornecer recursos 
ou dados necessários) que serão usadas nos testes automatizados.
'''

import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Edge() # Inicializa o navegador do Edge
    driver.maximize_window() # Maximiza a janela do navegador
    yield driver
    driver.quit()