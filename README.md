<!-- Este é um comentário: omitir os tópidos redundantes -->
<!--  **| [Brazil](README.md) | [asdf](README_en.md) |** -->

# Restaurant Orders

REST API em Python que simula pedidos de um restaurante. O programa foi elaborado para exercitar conceitos importantes de programação, como Programação Orientada a Objetos (POO), arrays, nós, listas encadeadas, pilhas, filas e conceitos de programação Web para construção de api Rest.

## Estrutura do Projeto

```python
.
├── src
│   ├──🔸__init__.py
│   └──🔹 app.py
│   ├── models
│   │   ├──🔸 __init__.py
│   │   ├──🔹 dish.py
│   │   └──🔹 ingredient.py
│   ├── services
│   │   ├──🔸 __init__.py
│   │   ├──🔹 inventory_control.py
│   │   ├──🔹 menu_builder.py
│   │   └──🔹 menu_data.py
├── data
│   ├──🔹 inventory_base_data.csv
│   └──🔹 menu_base_data.csv
├── tests
│   ├── dish
│   │   ├──🔸 __init__.py
│   │   └──🔹 test_priority_queue.py
│   ├── ingredient
│   │   ├──🔸 __init__.py
│   │   └──🔹 test_ingredient.py
│   └──🔸 __init__.py
├──🔸 dev-requirements.txt
├──🔸 pyproject.toml
├──🔸 README.md
├──🔸 requirements.txt
└──🔸...
```

## Instalação

1.Clone o repositório:

  ```bash
  git clone git@github.com:lionelsu/restaurant-orders.git && cd restaurant-orders
  ```

2.Crie um ambiente virtual:

  ```bash
  python3 -m venv .venv
  ```

3.Ative o ambiente virtual:

  ```bash
  source .venv/bin/activate
  ```

4.Instale as dependências:

  ```bash
  python3 -m pip install -r dev-requirements.txt
  ```

## Habilidades desenvolvidas

Este projeto `Python` foi desenvolvido para aprimorar as habilidades de programação e aplicar conceitos fundamentais. A implementação é baseada em `Python` e utiliza funções para resolver desafios do dia a dia usando das boas práticas da programação web.
