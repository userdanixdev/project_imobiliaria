from database import SessionLocal
from crud_corretor import (
    criar_corretor,
    listar_corretores,
    buscar_corretor_por_id,
    atualizar_corretor,
    deletar_corretor,
)
from test_logger import log_info, log_sucess, log_error


try:
    with SessionLocal() as session:
        log_info("Iniciando teste de CRUD de corretor")

        corretor = criar_corretor(
            session=session,
            nome="Carlos Corretor",
            creci="CRECI-12345",
        )

        log_sucess(
            f"Corretor criado: id={corretor.id_corretor}, "
            f"nome={corretor.nome}, creci={corretor.creci}"
        )

        corretores = listar_corretores(session)

        log_sucess(
            f"Listagem de corretores executada. Total encontrado: {len(corretores)}"
        )

        corretor_encontrado = buscar_corretor_por_id(
            session=session,
            id_corretor=corretor.id_corretor,
        )

        if corretor_encontrado is None:
            raise Exception("Corretor criado nao foi encontrado por ID")

        log_sucess(
            f"Corretor encontrado por ID: id={corretor_encontrado.id_corretor}, "
            f"nome={corretor_encontrado.nome}"
        )

        corretor_atualizado = atualizar_corretor(
            session=session,
            id_corretor=corretor.id_corretor,
            nome="Carlos Silva",
        )

        if corretor_atualizado is None:
            raise Exception("Falha ao atualizar corretor")

        log_sucess(
            f"Corretor atualizado: id={corretor_atualizado.id_corretor}, "
            f"nome={corretor_atualizado.nome}, creci={corretor_atualizado.creci}"
        )

        deletado = deletar_corretor(
            session=session,
            id_corretor=corretor.id_corretor,
        )

        if not deletado:
            raise Exception("Falha ao deletar corretor")

        log_sucess("Corretor deletado com sucesso")
        log_info("Teste de CRUD de corretor finalizado")

except Exception as error:
    log_error(f"Erro no teste de CRUD de corretor: {error}")
    raise