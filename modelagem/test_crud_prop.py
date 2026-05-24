from database import SessionLocal
from crud_prop import (
    criar_proprietario,
    listar_proprietarios,
    buscar_proprietario_por_id,
    atualizar_proprietario,
    deletar_proprietario,
)
from test_logger import log_info, log_sucess, log_error


try:
    with SessionLocal() as session:
        log_info("Iniciando teste de CRUD de proprietario")

        proprietario = criar_proprietario(
            session=session,
            nome="Joao Proprietario",
            cpf="11122233344",
        )

        log_sucess(
            f"Proprietario criado: id={proprietario.id_proprietario}, "
            f"nome={proprietario.nome}, cpf={proprietario.cpf}"
        )

        proprietarios = listar_proprietarios(session)

        log_sucess(
            f"Listagem de proprietarios executada. Total encontrado: {len(proprietarios)}"
        )

        proprietario_encontrado = buscar_proprietario_por_id(
            session=session,
            id_proprietario=proprietario.id_proprietario,
        )

        if proprietario_encontrado is None:
            raise Exception("Proprietario criado nao foi encontrado por ID")

        log_sucess(
            f"Proprietario encontrado por ID: id={proprietario_encontrado.id_proprietario}, "
            f"nome={proprietario_encontrado.nome}"
        )

        proprietario_atualizado = atualizar_proprietario(
            session=session,
            id_proprietario=proprietario.id_proprietario,
            nome="Joao Silva",
        )

        if proprietario_atualizado is None:
            raise Exception("Falha ao atualizar proprietario")

        log_sucess(
            f"Proprietario atualizado: id={proprietario_atualizado.id_proprietario}, "
            f"nome={proprietario_atualizado.nome}"
        )

        deletado = deletar_proprietario(
            session=session,
            id_proprietario=proprietario.id_proprietario,
        )

        if not deletado:
            raise Exception("Falha ao deletar proprietario")

        log_sucess("Proprietario deletado com sucesso")
        log_info("Teste de CRUD de proprietario finalizado")

except Exception as error:
    log_error(f"Erro no teste de CRUD de proprietario: {error}")
    raise