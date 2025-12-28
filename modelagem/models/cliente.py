from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id_cliente = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    telefone = Column(String)

    contratos = relationship("Contrato", back_populates="cliente")
