## 📋 Requisitos do Negócio

A imobiliária segue as seguintes regras de negócio, que orientam a modelagem dos
dados do sistema:

1. Um cliente pode alugar ou comprar **vários imóveis** ao longo do tempo.
2. Cada imóvel pertence a **um único proprietário**, porém pode ser alugado ou
   vendido para **diferentes clientes** em momentos distintos.
3. Cada contrato deve registrar informações como:
   - Dados do imóvel
   - Dados do cliente
   - Valor da transação
   - Data de assinatura
4. Os corretores são responsáveis por **intermediar as negociações** entre clientes
   e proprietários.

Com base nessas regras de negócio, foi elaborado um **Modelo de
Entidade-Relacionamento (MER)**, com o objetivo de representar de forma clara e
estruturada as **entidades**, seus **atributos** e os **relacionamentos** existentes
no sistema da imobiliária.
