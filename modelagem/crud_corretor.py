from sqlalchemy import select
from sqlalchemy.orm import Session

from models.cliente import Cliente
from models.contrato import Contrato
from models.corretor import Corretor
from models.imovel import Imovel
from models.proprietario import Proprietario


def criar_corretor(
    session: Session,
    nome: str,
    creci: str | None = None,
):
    corretor = Corretor(
        nome=nome,
        creci=creci,
    )

    session.add(corretor)
    session.commit()
    session.refresh(corretor)

    return corretor


def listar_corretores(session: Session):
    query = select(Corretor)
    return session.scalars(query).all()


def buscar_corretor_por_id(session: Session, id_corretor: int):
    return session.get(Corretor, id_corretor)


def atualizar_corretor(
    session: Session,
    id_corretor: int,
    nome: str | None = None,
    creci: str | None = None,
):
    corretor = buscar_corretor_por_id(session, id_corretor)

    if corretor is None:
        return None

    if nome is not None:
        corretor.nome = nome

    if creci is not None:
        corretor.creci = creci

    session.commit()
    session.refresh(corretor)

    return corretor


def deletar_corretor(session: Session, id_corretor: int):
    corretor = buscar_corretor_por_id(session, id_corretor)

    if corretor is None:
        return False

    session.delete(corretor)
    session.commit()

    return True