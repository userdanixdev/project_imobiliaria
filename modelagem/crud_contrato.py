from sqlalchemy import select
from sqlalchemy.orm import Session

from models.cliente import Cliente
from models.contrato import Contrato
from models.corretor import Corretor
from models.imovel import Imovel
from models.proprietario import Proprietario


def criar_contrato(
    session: Session,
    tipo_contrato: str,
    valor_transacao: float,
    data_assinatura,
    id_cliente: int | None = None,
    id_imovel: int | None = None,
    id_corretor: int | None = None,
):
    contrato = Contrato(
        tipo_contrato=tipo_contrato,
        valor_transacao=valor_transacao,
        data_assinatura=data_assinatura,
        id_cliente=id_cliente,
        id_imovel=id_imovel,
        id_corretor=id_corretor,
    )

    session.add(contrato)
    session.commit()
    session.refresh(contrato)

    return contrato


def listar_contratos(session: Session):
    query = select(Contrato)
    return session.scalars(query).all()


def buscar_contrato_por_id(session: Session, id_contrato: int):
    return session.get(Contrato, id_contrato)


def atualizar_contrato(
    session: Session,
    id_contrato: int,
    tipo_contrato: str | None = None,
    valor_transacao: float | None = None,
    data_assinatura=None,
    id_cliente: int | None = None,
    id_imovel: int | None = None,
    id_corretor: int | None = None,
):
    contrato = buscar_contrato_por_id(session, id_contrato)

    if contrato is None:
        return None

    if tipo_contrato is not None:
        contrato.tipo_contrato = tipo_contrato

    if valor_transacao is not None:
        contrato.valor_transacao = valor_transacao

    if data_assinatura is not None:
        contrato.data_assinatura = data_assinatura

    if id_cliente is not None:
        contrato.id_cliente = id_cliente

    if id_imovel is not None:
        contrato.id_imovel = id_imovel

    if id_corretor is not None:
        contrato.id_corretor = id_corretor

    session.commit()
    session.refresh(contrato)

    return contrato


def deletar_contrato(session: Session, id_contrato: int):
    contrato = buscar_contrato_por_id(session, id_contrato)

    if contrato is None:
        return False

    session.delete(contrato)
    session.commit()

    return True