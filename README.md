# 📊 Sistema Imobiliário – Modelagem de Dados (MER + DBML)

Este projeto apresenta a modelagem de dados de um sistema imobiliário,
desenvolvida a partir de regras de negócio reais, utilizando:

- Modelo Entidade-Relacionamento (MER)
- Database Markup Language (DBML)
- Modelo lógico relacional (SQL)

## 🧩 Problema:

A imobiliária realizava o controle de clientes, imóveis, contratos e corretores
de forma manual, o que gerava inconsistências, retrabalho e dificuldade na
geração de relatórios.

# 🏢 Projeto – Sistema de Banco de Dados Imobiliário

## 📌 Contexto

No setor imobiliário, onde há um alto volume de cadastros, contratos e transações,
a ausência de uma estrutura adequada para os dados pode gerar problemas como
informações duplicadas, inconsistentes ou de difícil acesso. A dependência de
registros manuais compromete a agilidade nas consultas, a confiabilidade dos
relatórios e a tomada de decisões estratégicas.

Diante desse cenário, este projeto propõe a modelagem de um banco de dados para
uma imobiliária que enfrenta dificuldades na organização de seus registros,
com dados de imóveis, clientes, contratos e corretores armazenados de forma manual.
A solução tem como foco a informatização do processo a partir de uma modelagem
bem definida.

---

## 🎯 Objetivo

Estruturar os dados do negócio por meio de um **Modelo Entidade-Relacionamento (MER)**,
garantindo a **organização**, a **integridade das informações** e uma **base sólida**
para a informatização e evolução do sistema imobiliário.

---

## 🧭 Escopo do Projeto

O projeto contempla:

- Levantamento e análise das regras de negócio do setor imobiliário
- Definição das entidades, atributos e relacionamentos
- Elaboração do **Modelo Entidade-Relacionamento (MER)**
- Tradução do modelo conceitual para o **modelo lógico**
- Implementação do modelo lógico utilizando **SQLAlchemy**
- Preparação da base para consultas e relatórios futuros

O projeto **não contempla**, neste momento:
- Interface gráfica
- Integração com sistemas externos
- Camada de aplicação web ou mobile

---

## 🛠️ Tecnologias Utilizadas

- **Python** – linguagem principal do projeto
- **SQLAlchemy** – ORM para implementação do modelo lógico do banco de dados
- **DBML (Database Markup Language)** – documentação e visualização da modelagem
- **SQLite** – banco de dados para ambiente de desenvolvimento
- **Conda** – gerenciamento de ambiente virtual
- **Git e GitHub** – versionamento e controle do código-fonte

---

## 📐 Modelagem de Dados

A modelagem de dados segue uma abordagem incremental:

1. **Modelo Conceitual (MER)** – identificação das entidades, atributos e relacionamentos
2. **Modelo Lógico** – definição das tabelas, chaves primárias, chaves estrangeiras e restrições
3. **Implementação Física** – criação do banco de dados utilizando SQLAlchemy

Essa abordagem garante que as regras de negócio sejam corretamente refletidas na
estrutura do banco de dados.

---

## 📈 Benefícios Esperados

- Dados organizados e padronizados
- Redução de inconsistências e erros manuais
- Consultas mais rápidas e confiáveis
- Relatórios mais precisos para tomada de decisão
- Base escalável para evolução futura do sistema


## 🏗️ Estrutura do Projeto
```
projeto-imobiliaria/
│
├── README.md
├── docs/
│   ├── intro.md
│   ├── requisitos_negocio.md
│   ├── justificativa_dbml.md
│   └── model_logic.md
│   
├── modelagem/
│   ├── models
│   |    └── __init__.py
|   |    └── base.py
|   |    └── cliente.py
|   |    └── contrato.py
|   |    └── corretor.py
|   |    └── imovel.py
|   |    └── proprietario.py
|   ├── create_tables.py
|   ├── data.base.py
|   ├── modelo.dbml
|── requirements.txt

```

## 📌 Autor
Daniel M. F.

## ⚙️ Ambiente Virtual

O projeto utiliza um ambiente virtual gerenciado pelo Conda.

### Criação do ambiente
```bash
conda create -n imobiliaria-env python=3.11
```