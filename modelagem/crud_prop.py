from sqlalchemy import select
from sqlalchemy.orm import Session

from models.cliente import Cliente
from models.contrato import Contrato
from models.corretor import Corretor
from models.imovel import Imovel
from models.proprietario import Proprietario


def criar_proprietario(
    session: Session,
    nome: str,
    cpf: str | None = None,
):
    proprietario = Proprietario(
        nome=nome,
        cpf=cpf,
    )

    session.add(proprietario)
    session.commit()
    session.refresh(proprietario)

    return proprietario


def listar_proprietarios(session: Session):
    query = select(Proprietario)
    return session.scalars(query).all()


def buscar_proprietario_por_id(session: Session, id_proprietario: int):
    return session.get(Proprietario, id_proprietario)


def atualizar_proprietario(
    session: Session,
    id_proprietario: int,
    nome: str | None = None,
    cpf: str | None = None,
):
    proprietario = buscar_proprietario_por_id(session, id_proprietario)

    if proprietario is None:
        return None

    if nome is not None:
        proprietario.nome = nome

    if cpf is not None:
        proprietario.cpf = cpf

    session.commit()
    session.refresh(proprietario)

    return proprietario


def deletar_proprietario(session: Session, id_proprietario: int):
    proprietario = buscar_proprietario_por_id(session, id_proprietario)

    if proprietario is None:
        return False

    session.delete(proprietario)
    session.commit()

    return True