# sample-python-package


Este repositório é um projeto exemplo para a construção de um pacote em python.

<br>

## Boas Práticas de desenvolvimento
<br>

👍 Crie um ambiente virtual. Dessa forma você terá controle de todas as bibliotecas e versões utilizadas no seu projeto.
```
python -m venv <nome-do-ambiente>
```

Ao final do seu desenvolvimento, armazene as lista de bibliotecas em um arquivo requirements
```
pip freeze > requirements.txt
```
👍 Utilize uma ferramenta de linter, como o pylit, para análise do código. 

👍 Utilize uma ferramenta de testes como o pytest.

👍 Utilize uma ferramenta de workflow para realizar o build & deploy do seu pacote. Neste repositório o workflow esta configurando apenas para o build, com code review e testes.

<br>

## Estrutura do projeto
<br>

```
project
│   README.md
│   conftest.py
|   setup.py
|   requirements.txt    
│
└───my_package
│   │   __init__.py
│   │   aula02.py
└───tests
│   │   test_aula02.py
└───workflows
│   │   python-package.yml
```






