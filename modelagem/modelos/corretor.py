from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Corretor(Base):
    __tablename__ = "corretores"

    id_corretor = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    creci = Column(String, unique=True)

    contratos = relationship("Contrato", back_populates="corretor")
