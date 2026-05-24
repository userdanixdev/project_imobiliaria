# Modelagem e CRUD do Sistema Imobiliario

Esta pasta concentra a implementacao da camada de persistencia do sistema imobiliario, incluindo a conexao com o banco SQLite, os modelos ORM com SQLAlchemy, os scripts de criacao das tabelas, as operacoes CRUD e os testes manuais com registro em log.

## Estrutura

```text
modelagem/
  database.py
  create_tables.py
  crud_cliente.py
  crud_proprietario.py
  crud_corretor.py
  crud_imovel.py
  crud_contrato.py
  test_logger.py
  run_tests.py
  logs/
  models/
    base.py
    cliente.py
    proprietario.py
    corretor.py
    imovel.py
    contrato.py
 ```

### Banco de Dados
A conexao com o banco esta centralizada no arquivo ```database.py.```

O projeto utiliza SQLite em ambiente de desenvolvimento:

> DATABASE_URL = "sqlite:///imobiliaria.db"

A criacao das tabelas e feita pelo script:

```python create_tables.py```

Esse script importa todos os modelos e executa:

> Base.metadata.create_all(bind=engine)

### Modelos ORM
Os modelos foram implementados com SQLAlchemy e representam as principais entidades do sistema:

```
Cliente
Proprietario
Corretor
Imovel
Contrato
```
### Os relacionamentos principais são:

 - Um Proprietario pode possuir varios Imoveis.
 - Um Imovel pertence a um Proprietario.
 - Um Cliente pode possuir varios Contratos.
 - Um Corretor pode intermediar varios Contratos.
 - Um Contrato relaciona Cliente, Imovel e Corretor.

### Camada CRUD:

Foi criada uma camada CRUD separada por entidade:

```
crud_cliente.py
crud_proprietario.py
crud_corretor.py
crud_imovel.py
crud_contrato.py
```
### Cada arquivo possui funcoes para:

- criar registros;
- listar registros;
- buscar registros por ID;
- atualizar registros;
- deletar registros.

>Exemplo de padrao utilizado:

```python
def buscar_cliente_por_id(session, id_cliente):
    return session.get(Cliente, id_cliente)
```

> As funcoes recebem uma Session do SQLAlchemy como dependencia, permitindo reutilizacao futura na API Flask.

### Testes Manuais
Foram criados testes manuais para validar as operacoes CRUD de cada entidade:

```
test_crud_cliente.py
test_crud_proprietario.py
test_crud_corretor.py
test_crud_imovel.py
test_crud_contrato.py
```
### Cada teste executa o ciclo basico:

```
cria um registro;
lista os registros;
busca por ID;
atualiza o registro;
remove o registro criado.
```

> Nos testes com dependencias, os registros auxiliares tambem sao criados e removidos.

Exemplo:

- O teste de Imovel cria antes um Proprietario.
- O teste de Contrato cria antes Cliente, - Proprietario, Imovel e Corretor.

### Logs
Os testes registram a execucao em arquivo de log usando o modulo logging.

O logger esta centralizado em:

```test_logger.py```

O arquivo principal de log dos testes e:

```logs/testes.log```

### Nele sao registrados eventos como:

- inicio do teste;
- criacao de registros;
- listagens;
- buscas por ID;
- atualizacoes;
- exclusoes;
- erros durante a execucao.
- Execucao Geral dos Testes

Foi criado o script:
```
run_tests.py
```

Ele executa todos os testes CRUD em sequencia:

```python run_tests.py```

A execucao geral gera um log separado em:

```logs/run_tests.log```

Esse arquivo registra:

- inicio da execucao geral;
- teste executado;
- sucesso ou falha de cada teste;
- mensagens de erro quando houver;
- duracao total da execucao.

