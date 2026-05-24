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
- **DBML (Database Markup Language)** – códigos da modelagem
- **SQLite** – banco de dados para ambiente de desenvolvimento
- **Conda** – gerenciamento de pacotes e do ambiente virtual
- **Git e GitHub** – versionamento e controle do código-fonte
- **DB Designer Web** - modelagem de dados
- **BR Modelo Web** - modelagem de dados

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
|   ├── mer_james_martin.png
|   ├── mer_peter_chen.jpg
|── .gitignore
|── requirements.txt

```
## ⚙️ Ambiente Virtual:

O projeto utiliza um ambiente virtual gerenciado pelo Conda.

### Criação do ambiente:
```bash
conda create -n imobiliaria-env python=3.11
```
## Evolução do Projeto:

O projeto evoluiu da etapa inicial de modelagem de dados para a implementacao da primeira camada funcional de persistência.

A versão atual contempla a criação da estrutura ORM com SQLAlchemy, a conexao com banco SQLite, a criação das tabelas, os CRUDs das entidades principais e testes manuais com registro em log.

## Camada de Persistência:

Foram implementadas operações CRUD para as principais entidades do sistema imobiliario:

- Cliente
- Proprietario
- Corretor
- Imovel
- Contrato

Cada entidade possui um arquivo especifico de CRUD dentro da pasta `modelagem`, permitindo criar, listar, buscar por ID, atualizar e deletar registros.

## Testes:

Foram criados testes manuais para validar os CRUDs implementados.

Os testes podem ser executados a partir da pasta `modelagem`:

```bash
python run_tests.py
```

### Logs:

A execução dos testes gera arquivos de log na pasta:

```modelagem/logs/```

Logs principais:

```
testes.log
run_tests.log
```

Esses logs ajudam a acompanhar as validações realizadas durante o desenvolvimento.

### Release v0.1.0:
A release v0.1.0 representa a primeira entrega técnica do projeto, contendo:

```
Conexao com banco SQLite
Modelos ORM com SQLAlchemy
Criacao das tabelas
CRUD de Cliente
CRUD de Proprietario
CRUD de Corretor
CRUD de Imovel
CRUD de Contrato
Testes manuais dos CRUDs
Registro de logs
Execucao geral dos testes com run_tests.py
README tecnico na pasta modelagem
```
### Link da release:

https://github.com/userdanixdev/project_imobiliaria/releases/tag/v0.1.0

### Estrutura do projeto atualizada:

```
project_imobiliaria/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── docs/
│   ├── intro.md
│   ├── requisitos.md
│   ├── justificativa_dbml.md
│   └── model_logic.md
│
└── modelagem/
    ├── README.md
    ├── database.py
    ├── create_tables.py
    ├── modelo.dbml
    ├── mer_james_martin.png
    ├── mer_peter_chen.jpg
    │
    ├── crud_clientes.py
    ├── crud_proprietario.py
    ├── crud_corretor.py
    ├── crud_imovel.py
    ├── crud_contrato.py
    │
    ├── test_connection_db.py
    ├── test_crud_cliente.py
    ├── test_crud_proprietario.py
    ├── test_crud_corretor.py
    ├── test_crud_imovel.py
    ├── test_crud_contrato.py
    ├── test_logger.py
    ├── run_tests.py
    │
    ├── logs/
    │   ├── testes.log
    │   └── run_tests.log
    │
    └── models/
        ├── __init__.py
        ├── base.py
        ├── cliente.py
        ├── proprietario.py
        ├── corretor.py
        ├── imovel.py
        └── contrato.py
```

### Proximos Passos:

As próximas etapas previstas são:

- Criar uma API com Flask.
- Conectar as rotas da API aos CRUDs existentes.
- Testar os endpoints da API.
- Criar uma interface web para o sistema imobiliario.
- Evoluir os testes para uma estrutura mais automatizada.

## 📌 Autor
Daniel Martins França

**email:** f.daniel.m@gmail.com  
**Linkedin:** www.linkedin.com/in/danixdev  
**Portifólio:** https://danixdev.blogspot.com/  
**+ Portifólio:** https://padlet.com/fdanielm/danix_dev
