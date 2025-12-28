from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Imovel(Base):
    __tablename__ = "imoveis"

    id_imovel = Column(Integer, primary_key=True)
    endereco = Column(String, nullable=False)
    tipo_imovel = Column(String)
    valor_base = Column(Float)

    id_proprietario = Column(Integer, ForeignKey("proprietarios.id_proprietario"))

    proprietario = relationship("Proprietario", back_populates="imoveis")
    contratos = relationship("Contrato", back_populates="imovel")
