from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions import db

class Corretor(db.Model):
    __tablename__ = "corretores"

    id_corretor: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    creci: Mapped[str | None] = mapped_column(String(30), unique=True, nullable=True)

    contratos = relationship("Contrato", back_populates="corretor")

    def __repr__(self) -> str:
        return (
            f"Corretor(id={self.id_corretor!r}, "
            f"nome={self.nome!r}, "
            f"creci={self.creci!r})"
        )