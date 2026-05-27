from modelagem.tests.crud_clientes import (
    criar_cliente,
    listar_clientes,
    buscar_cliente,
    atualizar_cliente,
    deletar_cliente,
)
from modelagem.tests.database import SessionLocal
from models.cliente import Cliente
from models.contrato import Contrato
from models.imovel import Imovel
from models.corretor import Corretor
from models.proprietario import Proprietario

from modelagem.tests.test_logger import log_info, log_sucess, log_error

try:
    with SessionLocal() as session:
        log_info("Iniciando teste de CRUD de cliente")
        cliente = criar_cliente(
            session = session,
            nome="Maria Silva",
            cpf='1234578900',
            telefone='119999999',
        )
        log_sucess(
            f"Cliente criado: id={cliente.id_cliente},"
            f"nome={cliente.nome}, cpf={cliente.cpf}, telefone={cliente.telefone}"
        )
        clientes = listar_clientes(session)
        log_sucess(
            f"Listagem de clientes executada. Total encontrado: {len(clientes)}"
        )
        cliente_encontrado = buscar_cliente(session=session,id_cliente=cliente.id_cliente)
        if cliente_encontrado is None:
            raise Exception(" Cliente criado não foi encontrado por ID")
        log_sucess(
            f"Cliente encontrado por ID: id={cliente_encontrado.id_cliente},"
            f"nome={cliente_encontrado.nome}"
        )
        cliente_atualizado = atualizar_cliente(session=session,id_cliente=cliente.id_cliente,
                                               telefone="11888888888")
        if cliente_atualizado is None:
            raise Exception("Falha ao atualizar cliente.")
        log_sucess(
            f"Cliente Atualizado: id ={cliente_atualizado.id_cliente},"
            f"telefone={cliente_atualizado.telefone}"
        )
        deletado = deletar_cliente(session=session,id_cliente=cliente.id_cliente)
        if not deletado:
            raise Exception("Falha ao deletar cliente")
        log_sucess("Cliente deletado com sucesso")
        log_info("Teste de CRUD de cliente finalizado")
except Exception as error:
        log_error(f"Erro no teste de CRUD de cliente: {error}")        
        raise