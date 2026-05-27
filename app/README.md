![Flask](https://img.shields.io/badge/Flask-Application%20Factory-000000?style=for-the-badge&logo=flask&logoColor=white)
![Flask SQLAlchemy](https://img.shields.io/badge/Flask--SQLAlchemy-3.x-D71F00?style=for-the-badge)
![Flask Migrate](https://img.shields.io/badge/Flask--Migrate-4.x-blue?style=for-the-badge)
![Alembic](https://img.shields.io/badge/Alembic-Migrations-6BA539?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-Development-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![API](https://img.shields.io/badge/API-em%20construção-orange?style=for-the-badge)

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

### Arquivo app/```__init__.py:```

> Este arquivo inicializa a aplicação Flask usando o padrão Application Factory.

### Objetivo:

- Criar a função create_app().
- Carregar as configurações da aplicação.
- Inicializar o Flask-SQLAlchemy com db.init_app(app).
- Inicializar o Flask-Migrate com migrate.init_app(app, db).
- Preparar o projeto para uso do comando flask.

> Esse padrão facilita testes, organização e crescimento da aplicação.

### A estrutura com app/, extensions.py, config.py e create_app() prepara o projeto para:

- criar uma API Flask organizada;
- integrar SQLAlchemy com Flask;
- utilizar Flask-Migrate para controle de migrações;
- gerar migrations com Alembic;
- evoluir os modelos atuais para uma estrutura compatível com Flask-SQLAlchemy;
- criar rotas e blueprints nas próximas etapas.

### Referências Oficiais:

Documentações utilizadas como base:

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

Os modelos atuais do projeto foram criados com **SQLAlchemy puro**, usando uma classe `Base` própria. Com isso, as tabelas ficam registradas no metadata de uma base nova.

Na nova etapa do projeto, usando Flask-SQLAlchemy e Flask-Migrate, a aplicação passa a trabalhar com uma instância central do banco. Isso significa que o Alembic/Flask-Migrate usa o metadata associado ao db para detectar os modelos e gerar as migrations.
Os modelos antigos foram registrados em outro metadata. Na prática, isso pode fazer com que o Flask-Migrate não detecte corretamente as tabelas, alterações de colunas, relacionamentos e demais mudanças do schema. Dessa forma adaptar os modelos para usarem o 'db' da aplicação Flask deixa tudo centralizado.

## Vantagens:

- O Flask-Migrate consegue detectar os modelos corretamente.
- O Alembic gera migrations com base no metadata correto.
- A estrutura fica mais alinhada com o padrão oficial do Flask.
- A futura API fica mais organizada.
- A fase antiga de modelagem fica separada da nova fase de aplicação Flask.
- Reduz o risco de inconsistências entre modelos, banco e migrations.

*Para este projeto, o caminho mais simples, organizado e aderente à documentação oficial é criar/adaptar os modelos da pasta app.*

> Dessa forma, Flask, Flask-SQLAlchemy, Flask-Migrate e Alembic passam a trabalhar sobre o mesmo metadata.

## Justificativas da mudança:

### 1. Mistura de responsabilidades

- A pasta modelagem/ nasceu como camada de estudo/modelagem, CRUD e testes manuais.
- A pasta app/ seria a aplicação Flask/API.

*Isso pode deixar o projeto mais difícil de evoluir...*

### 2. Imports obrigatórios para migrations

O Flask-Migrate só detecta modelos que foram importados. Se você esquecer de importar algum model antes de rodar o Alembic pode gerar uma migration incompleta. 
Exemplo: se Contrato não foi importado, ele pode não aparecer na migration.

### 3. Dois estilos no mesmo projeto:

Os modelos antigos usam SQLAlchemy puro:

```python
Column(Integer, primary_key=True)
```

O Flask-SQLAlchemy moderno costuma usar:

```python
Mapped
mapped_column
```

*Misturar estilos pode funcionar, mas prejudica padronização e aprendizado.*

### 4. Dependência da app em uma pasta antiga:

Se no futuro você quiser reorganizar ou remover a pasta modelagem/, a aplicação Flask quebra.
> A app fica acoplada à estrutura antiga.

### 5. Risco de migrations estranhas:

Se o metadata não for exatamente o mesmo, ou se parte dos modelos for registrada em outro lugar, o Alembic pode:

- não detectar tabelas;
- detectar diferenças inexistentes;
- tentar recriar tabelas;
- não perceber mudanças em colunas;
- gerar migrations incompletas.

### 6. Menos alinhado com documentação Flask:

A documentação de Flask, Flask-SQLAlchemy e Flask-Migrate favorece uma estrutura onde a aplicação fica centralizada.

### Resumo:

```
Reaproveitar o metadata antigo é possível, mas exige cuidado com imports, organização e consistência. Para aprendizado, manutenção e evolução para API, o melhor padrão é com modelos ligados diretamente ao db da aplicação Flask. Assim o Flask-Migrate trabalha com o metadata correto, e o projeto fica mais claro.
```

Dessa forma temos então esse fluxo lógico:

```
modelagem/ -> fase inicial do banco e testes
app/       -> aplicação Flask e API
```

## Validação das Rotas Flask:

Para validar se a aplicação Flask está sendo carregada corretamente, foi utilizado o comando:

```python
flask --app app:create_app routes
```

Esse comando usa a CLI do Flask para carregar a aplicação e listar todas as rotas registradas. A opção ```--app app:create_app``` informa ao Flask que a aplicação deve ser criada a partir da função ```create_app```, localizada no módulo/pacote app.

Esse padrão é conhecido como ```Application Factory```, no qual a instância da aplicação Flask é criada dentro de uma função, em vez de ficar declarada diretamente como variável global. Segundo a documentação oficial do Flask, esse padrão facilita testes, configurações diferentes e melhor organização do projeto. 

> Referência: Flask Application Factories.

### A saída obtida foi:


Endpoint |  Methods | Rule
-------- | ------- | -----------------------
index  |   GET |     /
static |   GET |     /static/<path:filename>

> Essa saída indica que o Flask conseguiu carregar a aplicação sem erro e identificou duas rotas:

Endpoint |	Método |	Rota |	Descrição
--- | --- | --- | ---
index |	GET	| /	| Rota principal da aplicação, geralmente responsável por exibir a página inicial.
static |	GET	|/ |static/<path:filename>	Rota automática criada pelo Flask para servir arquivos estáticos, como CSS, JavaScript e imagens.

### Portanto, a validação confirma que:

- A aplicação Flask foi carregada corretamente pela função create_app.
- A rota principal / está registrada.
- O método HTTP permitido para a rota principal é GET.
- A configuração padrão de arquivos estáticos do Flask está ativa.

> Não foram identificadas, nesse momento, outras rotas cadastradas no projeto.

*É importante destacar que esse comando não testa o funcionamento interno da página, banco de dados, formulários ou regras de negócio. Ele apenas valida o registro das rotas dentro da aplicação Flask. Para uma validação mais completa, também podem ser feitos testes acessando a aplicação no navegador ou utilizando testes automatizados com pytest e o test_client do Flask.*

A documentação da CLI do Flask explica que --app define como o Flask deve localizar e carregar a aplicação, podendo apontar para uma instância ou para uma factory como create_app. 

*Referência: Flask Command Line Interface.*

## Etapa 2 - Criação dos Models com Flask-SQLAlchemy

Nesta etapa, os modelos da aplicação foram criados dentro da pasta `app/models/`, utilizando o `db` central definido em `app/extensions.py`.

*O objetivo é adaptar a estrutura de entidades da fase inicial de modelagem para o padrão usado pelo Flask-SQLAlchemy, permitindo que o Flask-Migrate e o Alembic detectem corretamente as tabelas e gerem as migrations do banco de dados.*

## Etapa 03 - Validação e criação das tabelas e do banco:

```flask --app app:create_app db migrate -m "create initial tables"```

O comando é usado para gerar uma nova migration do banco de dados com base nas diferenças entre os models da aplicação Flask e o estado atual do banco.

A opção ```--app app:create_app```informa ao Flask que a aplicação deve ser carregada a partir da função ```create_app```, dentro do pacote app.

O trecho ```db migrate``` vem do Flask-Migrate e executa o processo de autogeração de migration usando o Alembic. A opção -m ```"create initial tables"``` adiciona uma mensagem descritiva à migration. Nesse caso, a mensagem indica que a migration tem como objetivo criar as tabelas iniciais do projeto.

### Em resumo:

- carrega a aplicação Flask;
- acessa a configuração do banco;
- lê os models registrados no db.metadata;
- compara os models com o banco atual;
- gera um arquivo de migration dentro da pasta migrations/versions;

*No seu caso, o comando foi importante porque validou que o Flask-Migrate estava configurado e conseguia iniciar o processo de autogeração. Porém, ele também revelou inconsistências nas ForeignKey, como referências para colunas inexistentes em clientes.*

> Assim o comando não apenas cria migrations; ele também ajuda a validar se os relacionamentos entre os models estão coerentes.

## Aplicação da Migration com `db upgrade`

Após gerar uma migration com o comando `db migrate`, é necessário aplicar essa migration no banco de dados. Para isso, utiliza-se o comando:

```bash
flask --app app:create_app db upgrade
```

Esse comando faz parte do Flask-Migrate e utiliza o Alembic para executar, no banco de dados, as alterações descritas nos arquivos de migration.

Enquanto o comando db migrate gera o arquivo de migration com base nas diferenças entre os models e o banco, o comando db upgrade aplica essas alterações de fato.

### Observação Importante:

O comando ```**db upgrade**``` deve ser executado somente depois que uma migration for gerada com sucesso.

Se o comando ```db migrate``` apresentar erros, como inconsistências em **ForeignKey** ou models não importados corretamente, esses problemas devem ser corrigidos antes da aplicação da migration no banco.

> Caso contrário, o banco pode não ser atualizado ou a migration pode nem chegar a ser criada.

## Etapa 4 - Criação das Rotas da API Flask

Após a criação e validação dos models com Flask-SQLAlchemy e Flask-Migrate, a próxima etapa será a criação das rotas da API.

As rotas serão responsáveis por expor as operações da aplicação para acesso via HTTP, permitindo consultar, cadastrar, atualizar e remover registros relacionados à imobiliária.

Nesta etapa, o Flask será utilizado para registrar endpoints da API, enquanto o comando `flask --app app:create_app routes` será usado para validar se as rotas foram carregadas corretamente.