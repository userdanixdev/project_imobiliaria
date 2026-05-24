from database import SessionLocal
from crud_imovel import (
    criar_imovel,
    listar_imoveis,
    buscar_imovel_por_id,
    atualizar_imovel,
    deletar_imovel,
)
from crud_prop import (
    criar_proprietario,
    deletar_proprietario,
)
from test_logger import log_info, log_sucess, log_error


try:
    with SessionLocal() as session:
        log_info("Iniciando teste de CRUD de imovel")

        proprietario = criar_proprietario(
            session=session,
            nome="Proprietario Teste Imovel",
            cpf="99988877766",
        )

        log_sucess(
            f"Proprietario criado para teste: id={proprietario.id_proprietario}, "
            f"nome={proprietario.nome}"
        )

        imovel = criar_imovel(
            session=session,
            endereco="Rua das Flores, 100",
            tipo_imovel="Apartamento",
            valor_base=350000.00,
            id_proprietario=proprietario.id_proprietario,
        )

        log_sucess(
            f"Imovel criado: id={imovel.id_imovel}, "
            f"endereco={imovel.endereco}, tipo={imovel.tipo_imovel}, "
            f"valor_base={imovel.valor_base}, id_proprietario={imovel.id_proprietario}"
        )

        imoveis = listar_imoveis(session)

        log_sucess(
            f"Listagem de imoveis executada. Total encontrado: {len(imoveis)}"
        )

        imovel_encontrado = buscar_imovel_por_id(
            session=session,
            id_imovel=imovel.id_imovel,
        )

        if imovel_encontrado is None:
            raise Exception("Imovel criado nao foi encontrado por ID")

        log_sucess(
            f"Imovel encontrado por ID: id={imovel_encontrado.id_imovel}, "
            f"endereco={imovel_encontrado.endereco}"
        )

        imovel_atualizado = atualizar_imovel(
            session=session,
            id_imovel=imovel.id_imovel,
            endereco="Rua das Flores, 200",
            valor_base=375000.00,
        )

        if imovel_atualizado is None:
            raise Exception("Falha ao atualizar imovel")

        log_sucess(
            f"Imovel atualizado: id={imovel_atualizado.id_imovel}, "
            f"endereco={imovel_atualizado.endereco}, "
            f"valor_base={imovel_atualizado.valor_base}"
        )

        imovel_deletado = deletar_imovel(
            session=session,
            id_imovel=imovel.id_imovel,
        )

        if not imovel_deletado:
            raise Exception("Falha ao deletar imovel")

        log_sucess("Imovel deletado com sucesso")

        proprietario_deletado = deletar_proprietario(
            session=session,
            id_proprietario=proprietario.id_proprietario,
        )

        if not proprietario_deletado:
            raise Exception("Falha ao deletar proprietario usado no teste de imovel")

        log_sucess("Proprietario usado no teste de imovel deletado com sucesso")
        log_info("Teste de CRUD de imovel finalizado")

except Exception as error:
    log_error(f"Erro no teste de CRUD de imovel: {error}")
    raise