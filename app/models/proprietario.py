from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions import db

class Proprietario(db.Model):
    __tablename__ = "proprietarios"

    id_proprietario: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100),nullable=False)
    cpf: Mapped[str | None] = mapped_column(String(14), unique=True, nullable=True)

    imoveis = relationship("Imovel", back_populates="proprietario")

    def __repr__(self) -> str:
        return (
            f"Proprietario(id={self.id_proprietario!r}, "
            f"nome={self.nome!r}, "
            f"cpf={self.cpf!r})"
        )