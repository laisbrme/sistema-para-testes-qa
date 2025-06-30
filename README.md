# Sistema para Testes QA

Este repositório foi desenvolvido para a entrega dos desafios da disciplina **SOFTWARE QUALITY ASSURANCE (SQA) - GARANTINDO A QUALIDADE DOS SOFTWARES**. O objetivo é demonstrar a aplicação de técnicas de testes manuais e automatizados em um sistema de cadastro de produtos.

---

## Objetivo

O repositório contempla dois desafios principais:

### Desafio 1: Testes Manuais

> **Descrição:**  
> Testar o sistema para cadastro de produtos.  
> Anotar o máximo de casos de testes possíveis para esta aplicação.  
> Documentar o máximo de testes possíveis.
>
> [Sistema CRUD para cadastro de produtos](sistema)
>
> **Para iniciar o sistema:**  
> Basta clicar no arquivo `login.html`.
>
> **Dados de acesso:**  
> - Email: `admin@admin.com`  
> - Senha: `admin@123`

Neste desafio, foram aplicadas diversas técnicas de teste, incluindo caixa branca, caixa preta, testes funcionais, de segurança, performance, entre outros. Todos os casos de teste estão documentados na planilha [Casos de teste.xlsx](https://github.com/laisbrme/sistema-para-testes-qa/blob/7016e40c9128a69d2f5176e9011593150aea762d/Casos%20de%20testes.xlsx).

---

### Desafio 2: Testes Automatizados

> **Descrição:**  
> Com base no desafio 1, criar um projeto automatizado para testar os casos que foram criados no desafio anterior.  
> Automatizar utilizando **Selenium**.  
> São esperados um mínimo de 10 casos de testes automatizados.

Neste desafio, foi criado um projeto de automação utilizando Selenium, cobrindo os principais fluxos do sistema, como login, cadastro, validação de campos obrigatórios, entre outros.

---

## Estrutura do Repositório

```
├── Desafio_1
│   └── sistema
│   │   ├── login.html
│   │   ├── produtos.html
│   │   └── src
│   │       ├── css
│   │       │   ├── base.css
│   │       │   ├── login.css
│   │       │   └── produtos.css
│   │       └── js
│   │           ├── Produto.js
│   │           ├── base.js
│   │           ├── credenciais.js
│   │           ├── login.js
│   │           └── produtos.js
│   └── Casos de teste.xlsx
│
├── Desafio_2
│   ├── README.md
│   └── testes_automatizados
│       ├── conftest.py
│       ├── test_login.py
│       ├── test_produtos.py
│       └── requirements.txt
│
└── README.md
```

---

## Tecnologias Utilizadas

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=fff&style=for-the-badge)](https://developer.mozilla.org/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=fff&style=for-the-badge)](https://developer.mozilla.org/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=000&style=for-the-badge)](https://developer.mozilla.org/docs/Web/JavaScript)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-43B02A?logo=selenium&logoColor=fff&style=for-the-badge)](https://www.selenium.dev/)

---

## Considerações Finais

Os testes são parte essencial do desenvolvimento de software, garantindo a qualidade e a funcionalidade do sistema. Este repositório demonstra a importância dos testes manuais e automatizados, bem como a aplicação de diferentes técnicas de teste.

---

## Contato

- Nome: Laís Brum
- Email: [eng.laisb@gmail.com](mailto:eng.laisb@gmail.com)
- LinkedIn: [linkedin.com/in/lais-brum](https://linkedin.com/in/lais-brum)