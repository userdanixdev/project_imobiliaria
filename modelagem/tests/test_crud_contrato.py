from datetime import date

from modelagem.tests.database import SessionLocal
from modelagem.tests.crud_clientes import criar_cliente, deletar_cliente
from modelagem.tests.crud_prop import criar_proprietario, deletar_proprietario
from modelagem.tests.crud_imovel import criar_imovel, deletar_imovel
from modelagem.tests.crud_corretor import criar_corretor, deletar_corretor
from modelagem.tests.crud_contrato import (
    criar_contrato,
    listar_contratos,
    buscar_contrato_por_id,
    atualizar_contrato,
    deletar_contrato,
)
from modelagem.tests.test_logger import log_info, log_sucess, log_error


try:
    with SessionLocal() as session:
        log_info("Iniciando teste de CRUD de contrato")

        cliente = criar_cliente(
            session=session,
            nome="Cliente Teste Contrato",
            cpf="22233344455",
            telefone="11977777777",
        )

        log_sucess(
            f"Cliente criado para teste: id={cliente.id_cliente}, nome={cliente.nome}"
        )

        proprietario = criar_proprietario(
            session=session,
            nome="Proprietario Teste Contrato",
            cpf="33344455566",
        )

        log_sucess(
            f"Proprietario criado para teste: id={proprietario.id_proprietario}, "
            f"nome={proprietario.nome}"
        )

        imovel = criar_imovel(
            session=session,
            endereco="Avenida Central, 500",
            tipo_imovel="Casa",
            valor_base=500000.00,
            id_proprietario=proprietario.id_proprietario,
        )

        log_sucess(
            f"Imovel criado para teste: id={imovel.id_imovel}, endereco={imovel.endereco}"
        )

        corretor = criar_corretor(
            session=session,
            nome="Corretor Teste Contrato",
            creci="CRECI-99999",
        )

        log_sucess(
            f"Corretor criado para teste: id={corretor.id_corretor}, nome={corretor.nome}"
        )

        contrato = criar_contrato(
            session=session,
            tipo_contrato="venda",
            valor_transacao=485000.00,
            data_assinatura=date.today(),
            id_cliente=cliente.id_cliente,
            id_imovel=imovel.id_imovel,
            id_corretor=corretor.id_corretor,
        )

        log_sucess(
            f"Contrato criado: id={contrato.id_contrato}, "
            f"tipo={contrato.tipo_contrato}, valor={contrato.valor_transacao}"
        )

        contratos = listar_contratos(session)

        log_sucess(
            f"Listagem de contratos executada. Total encontrado: {len(contratos)}"
        )

        contrato_encontrado = buscar_contrato_por_id(
            session=session,
            id_contrato=contrato.id_contrato,
        )

        if contrato_encontrado is None:
            raise Exception("Contrato criado nao foi encontrado por ID")

        log_sucess(
            f"Contrato encontrado por ID: id={contrato_encontrado.id_contrato}, "
            f"tipo={contrato_encontrado.tipo_contrato}"
        )

        contrato_atualizado = atualizar_contrato(
            session=session,
            id_contrato=contrato.id_contrato,
            valor_transacao=490000.00,
        )

        if contrato_atualizado is None:
            raise Exception("Falha ao atualizar contrato")

        log_sucess(
            f"Contrato atualizado: id={contrato_atualizado.id_contrato}, "
            f"valor={contrato_atualizado.valor_transacao}"
        )

        contrato_deletado = deletar_contrato(
            session=session,
            id_contrato=contrato.id_contrato,
        )

        if not contrato_deletado:
            raise Exception("Falha ao deletar contrato")

        log_sucess("Contrato deletado com sucesso")

        imovel_deletado = deletar_imovel(
            session=session,
            id_imovel=imovel.id_imovel,
        )

        if not imovel_deletado:
            raise Exception("Falha ao deletar imovel usado no teste de contrato")

        log_sucess("Imovel usado no teste de contrato deletado com sucesso")

        proprietario_deletado = deletar_proprietario(
            session=session,
            id_proprietario=proprietario.id_proprietario,
        )

        if not proprietario_deletado:
            raise Exception("Falha ao deletar proprietario usado no teste de contrato")

        log_sucess("Proprietario usado no teste de contrato deletado com sucesso")

        cliente_deletado = deletar_cliente(
            session=session,
            id_cliente=cliente.id_cliente,
        )

        if not cliente_deletado:
            raise Exception("Falha ao deletar cliente usado no teste de contrato")

        log_sucess("Cliente usado no teste de contrato deletado com sucesso")

        corretor_deletado = deletar_corretor(
            session=session,
            id_corretor=corretor.id_corretor,
        )

        if not corretor_deletado:
            raise Exception("Falha ao deletar corretor usado no teste de contrato")

        log_sucess("Corretor usado no teste de contrato deletado com sucesso")
        log_info("Teste de CRUD de contrato finalizado")

except Exception as error:
    log_error(f"Erro no teste de CRUD de contrato: {error}")
    raise