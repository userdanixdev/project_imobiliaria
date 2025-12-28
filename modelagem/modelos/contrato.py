from sqlalchemy import Column, Integer, Float, Date, ForeignKey, String
from sqlalchemy.orm import relationship
from .base import Base

class Contrato(Base):
    __tablename__ = "contratos"

    id_contrato = Column(Integer, primary_key=True)
    tipo_contrato = Column(String, nullable=False)  # aluguel ou venda
    valor_transacao = Column(Float, nullable=False)
    data_assinatura = Column(Date, nullable=False)

    id_cliente = Column(Integer, ForeignKey("clientes.id_cliente"))
    id_imovel = Column(Integer, ForeignKey("imoveis.id_imovel"))
    id_corretor = Column(Integer, ForeignKey("corretores.id_corretor"))

    cliente = relationship("Cliente", back_populates="contratos")
    imovel = relationship("Imovel", back_populates="contratos")
    corretor = relationship("Corretor", back_populates="contratos")
