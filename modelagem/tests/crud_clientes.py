from sqlalchemy import select 
from sqlalchemy.orm import Session
from models.cliente import Cliente

def criar_cliente(
        session: Session,
        nome: str,
        cpf: str,
        telefone: str | None = None,
):
    cliente = Cliente(
        nome = nome,
        cpf = cpf,
        telefone = telefone,
    )
    session.add(cliente)
    session.commit()
    session.refresh(cliente)

    return cliente

def buscar_cliente(session: Session, id_cliente:int):
    return session.get(Cliente, id_cliente)

def listar_clientes(session: Session):
    query = select(Cliente)
    return session.scalars(query).all()
def atualizar_cliente(
    session: Session,
    id_cliente:int,
    nome: str | None = None,
    cpf: str | None = None,
    telefone: str | None = None,
):
    cliente = buscar_cliente(session, id_cliente)

    if cliente is None:
        return None
    if nome is not None:
        cliente.nome = nome
    if cpf is not None:
        cliente.cpf = cpf
    if telefone is not None:
        cliente.telefone = telefone

    session.commit()
    session.refresh(cliente)

    return cliente                

def deletar_cliente(session: Session, id_cliente: int):
    cliente = buscar_cliente(session, id_cliente)

    if cliente is None:
        return False
    session.delete(cliente)
    session.commit()

    return True