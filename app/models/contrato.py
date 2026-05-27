from datetime import date
from sqlalchemy import String, Float, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions import db

class Contrato(db.Model):
    __tablename__ = "contratos"

    id_contrato: Mapped[int] = mapped_column(primary_key=True)
    tipo_contrato: Mapped[str] = mapped_column(String(20), nullable=False)
    valor_transacao: Mapped[float] = mapped_column(Float, nullable=False)
    data_assinatura: Mapped[date] = mapped_column(Date, nullable=False)

    id_cliente:Mapped[int | None] = mapped_column(
        ForeignKey("clientes.id_clientes"),nullable=True)
    id_corretor: Mapped[int | None] = mapped_column(
        ForeignKey("corretores.id_corretor"), nullable=True)
    
    cliente = relationship("Cliente", back_populates="contratos")
    imovel = relationship("Imovel", back_populates="contratos")
    corretor = relationship("Corretor", back_populates="contratos")

    def __repr__(self) -> str:
        return (
            f"Contrato(id={self.id_contrato!r}, "
            f"tipo={self.tipo_contrato!r}, "
            f"valor={self.valor_transacao!r})"
        )