from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions import db

class Cliente(db.Model):
    __tablename__ = "clientes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100),nullable=False)
    cpf: Mapped[str] = mapped_column(String(14),unique=True, nullable=False)
    telefone: Mapped[str | None] = mapped_column(String(20),nullable=True)

    contratos = relationship("Contrato", back_populates="cliente")

    def __repr__(self) -> str:
        return (
            f"Cliente(id={self.id_cliente!r}, "
            f"nome={self.nome!r}, "
            f"cpf={self.cpf!r})")
        