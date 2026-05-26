# Etapa 1 - Estrutura Inicial Flask, Flask-SQLAlchemy e Flask-Migrate

Nesta etapa foi iniciada a evolução do projeto para uma API com Flask, seguindo a documentação oficial do Flask, Flask-SQLAlchemy, Flask-Migrate e Alembic.

O objetivo desta fase é preparar a estrutura base da aplicação, sem alterar ainda os CRUDs existentes na pasta `modelagem`.

## 1. Dependências Adicionadas

Foram adicionadas novas dependências ao arquivo `requirements.txt`:

```python
Flask>=3.0
Flask-SQLAlchemy>=3.1
Flask-Migrate>=4.0
```

### Estrutura inicial:

```
project_imobiliaria/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│   └── models/
│       └── __init__.py
│
├── modelagem/
│   └── ...
│
├── requirements.txt
└── README.md
```

###  Arquivo app/extensions.py:

Este arquivo centraliza as extensões utilizadas pela aplicação.

### Objetivo:

- Criar a instância db do Flask-SQLAlchemy.
- Criar a instância migrate do Flask-Migrate.
- Manter as extensões separadas da aplicação principal.
- Permitir que sejam inicializadas posteriormente com init_app().

> Esse padrão segue a recomendação do Flask para uso de extensões com Application Factory.

### Arquivo app/config.py:

> Este arquivo centraliza as configurações da aplicação.

### Objetivo:

- Definir o caminho do banco SQLite.
- Manter a configuração isolada em uma classe.
- Facilitar futuras configurações por ambiente, como desenvolvimento, teste e produção.

> O banco configurado fica na raiz do projeto: ```imobiliaria.db```

### Arquivo app/__init__.py:

> Este arquivo inicializa a aplicação Flask usando o padrão Application Factory.

### Objetivo:

- Criar a função create_app().
- Carregar as configurações da aplicação.
- Inicializar o Flask-SQLAlchemy com db.init_app(app).
- Inicializar o Flask-Migrate com migrate.init_app(app, db).
- Preparar o projeto para uso do comando flask.

> Esse padrão facilita testes, organização e crescimento da aplicação.

> A estrutura com app/, extensions.py, config.py e create_app() prepara o projeto para:

- criar uma API Flask organizada;
- integrar SQLAlchemy com Flask;
- utilizar Flask-Migrate para controle de migrações;
- gerar migrations com Alembic;
- evoluir os modelos atuais para uma estrutura compatível com Flask-SQLAlchemy;
- criar rotas e blueprints nas próximas etapas.

### Referências Oficiais:

> Documentações utilizadas como base:

- Flask - Application Factory
https://flask.palletsprojects.com/en/stable/patterns/appfactories/

- Flask-SQLAlchemy - Quickstart
https://flask-sqlalchemy.palletsprojects.com/en/stable/quickstart/

- Flask-Migrate - Documentation
https://flask-migrate.readthedocs.io/en/latest/

- Alembic - Tutorial
https://alembic.sqlalchemy.org/en/latest/tutorial.html

## Trade-off:

### Por que não usar diretamente os modelos antigos?

Os modelos atuais do projeto foram criados com **SQLAlchemy puro**, usando uma classe `Base` própria.
Com isso, as tabelas ficam registradas no metadata de uma base nova.
Na nova etapa do projeto, usando Flask-SQLAlchemy e Flask-Migrate, a aplicação passa a trabalhar com uma instância central do banco. Isso significa que o Alembic/Flask-Migrate usa o metadata associado ao db para detectar os modelos e gerar as migrations.
Os modelos antigos foram registrados em outro metadata. Na prática, isso pode fazer com que o Flask-Migrate não detecte corretamente as tabelas, alterações de colunas, relacionamentos e demais mudanças do schema. Dessa forma adaptar os modelos para usarem o 'db' da aplicação Flask deixa tudo centralizado.

## Vantagens:

- O Flask-Migrate consegue detectar os modelos corretamente.
- O Alembic gera migrations com base no metadata correto.
- A estrutura fica mais alinhada com o padrão oficial do Flask.
- A futura API fica mais organizada.
- A fase antiga de modelagem fica separada da nova fase de aplicação Flask.
- Reduz o risco de inconsistências entre modelos, banco e migrations.

Para este projeto, o caminho mais simples, organizado e aderente à documentação oficial é criar/adaptar os modelos da pasta app.

Dessa forma, Flask, Flask-SQLAlchemy, Flask-Migrate e Alembic passam a trabalhar sobre o mesmo metadata.

## Justificativas da mudança:

1. Mistura de responsabilidades

- A pasta modelagem/ nasceu como camada de estudo/modelagem, CRUD e testes manuais.
- A pasta app/ seria a aplicação Flask/API.

> Isso pode deixar o projeto mais difícil de evoluir

2. Imports obrigatórios para migrations

O Flask-Migrate só detecta modelos que foram importados. Se você esquecer de importar algum model antes de rodar o Alembic pode gerar uma migration incompleta. 
Exemplo: se Contrato não foi importado, ele pode não aparecer na migration.

3. Dois estilos no mesmo projeto:

Os modelos antigos usam SQLAlchemy puro.

```python
Column(Integer, primary_key=True)
```

O Flask-SQLAlchemy moderno costuma usar:

```python
Mapped
mapped_column
```

> Misturar estilos pode funcionar, mas prejudica padronização e aprendizado.

4. Dependência da app em uma pasta antiga:

> Se no futuro você quiser reorganizar ou remover a pasta modelagem/, a aplicação Flask quebra.
> A app fica acoplada à estrutura antiga.

5. Risco de migrations estranhas:

Se o metadata não for exatamente o mesmo, ou se parte dos modelos for registrada em outro lugar, o Alembic pode:

- não detectar tabelas;
- detectar diferenças inexistentes;
- tentar recriar tabelas;
- não perceber mudanças em colunas;
- gerar migrations incompletas.

6. Menos alinhado com documentação Flask:

A documentação de Flask, Flask-SQLAlchemy e Flask-Migrate favorece uma estrutura onde a aplicação fica centralizada.

### Resumo:

Reaproveitar o metadata antigo é possível, mas exige cuidado com imports, organização e consistência.
Para aprendizado, manutenção e evolução para API, o melhor padrão é com modelos ligados diretamente ao db da aplicação Flask. Assim o Flask-Migrate trabalha com o metadata correto, e o projeto fica mais claro.

Dessa forma temos então esse fluxo lógico:

```
modelagem/ -> fase inicial do banco e testes
app/       -> aplicação Flask e API
```