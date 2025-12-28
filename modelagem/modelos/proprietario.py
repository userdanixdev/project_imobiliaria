from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Proprietario(Base):
    __tablename__ = "proprietarios"

    id_proprietario = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, unique=True)

    imoveis = relationship("Imovel", back_populates="proprietario")
