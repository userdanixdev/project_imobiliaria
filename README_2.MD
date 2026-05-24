## Release v0.1.0

A versao `v0.1.0` marca a primeira entrega técnica da camada de persistência do sistema imobiliário.

### Implementado

- Conexão com banco SQLite utilizando SQLAlchemy
- Criação das tabelas a partir dos modelos ORM
- CRUD de Cliente
- CRUD de Proprietário
- CRUD de Corretor
- CRUD de Imóvel
- CRUD de Contrato
- Testes manuais para validação dos CRUDs
- Registro de logs dos testes
- Script para execução geral dos testes
- README técnico na pasta `modelagem`

### Testes

Os testes da camada de modelagem podem ser executados pela pasta `modelagem`:

```bash
python run_tests.py