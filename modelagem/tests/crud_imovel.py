from sqlalchemy import select
from sqlalchemy.orm import Session

from models.cliente import Cliente
from models.contrato import Contrato
from models.corretor import Corretor
from models.imovel import Imovel
from models.proprietario import Proprietario


def criar_imovel(
    session: Session,
    endereco: str,
    tipo_imovel: str | None = None,
    valor_base: float | None = None,
    id_proprietario: int | None = None,
):
    imovel = Imovel(
        endereco=endereco,
        tipo_imovel=tipo_imovel,
        valor_base=valor_base,
        id_proprietario=id_proprietario,
    )

    session.add(imovel)
    session.commit()
    session.refresh(imovel)

    return imovel


def listar_imoveis(session: Session):
    query = select(Imovel)
    return session.scalars(query).all()


def buscar_imovel_por_id(session: Session, id_imovel: int):
    return session.get(Imovel, id_imovel)


def atualizar_imovel(
    session: Session,
    id_imovel: int,
    endereco: str | None = None,
    tipo_imovel: str | None = None,
    valor_base: float | None = None,
    id_proprietario: int | None = None,
):
    imovel = buscar_imovel_por_id(session, id_imovel)

    if imovel is None:
        return None

    if endereco is not None:
        imovel.endereco = endereco

    if tipo_imovel is not None:
        imovel.tipo_imovel = tipo_imovel

    if valor_base is not None:
        imovel.valor_base = valor_base

    if id_proprietario is not None:
        imovel.id_proprietario = id_proprietario

    session.commit()
    session.refresh(imovel)

    return imovel


def deletar_imovel(session: Session, id_imovel: int):
    imovel = buscar_imovel_por_id(session, id_imovel)

    if imovel is None:
        return False

    session.delete(imovel)
    session.commit()

    return True