from sqlalchemy import Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions import db

class Imovel(db.Model):
    __tablename__ = "imoveis"

    id_imovel: Mapped[int] = mapped_column(primary_key=True)
    endereco: Mapped[str] = mapped_column(String(255), nullable=False)
    tipo_imovel: Mapped[str | None] = mapped_column(String(50), nullable=True)
    valor_base: Mapped[float | None] = mapped_column(Float, nullable=True)

    id_proprietario: Mapped[int | None] = mapped_column(
        ForeignKey("proprietarios.id_proprietario"), nullable=True)
    
    proprietario = relationship("Proprietario", back_populates="imoveis")
    contratos = relationship("Contrato", back_populates="imovel")

    def __repr__(self) -> str:
        return (
            f"Imovel(id={self.id_imovel!r}, "
            f"endereco={self.endereco!r}, "
            f"tipo={self.tipo_imovel!r})"
        )