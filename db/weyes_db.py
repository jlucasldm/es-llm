import enum

from config import settings
from sqlalchemy import VARCHAR, ForeignKey
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import asyncio

from db.annotations import big_intpk, datetime_default_now

DATABASE_URL = (
    f"mysql+asyncmy://{settings.weyes.USERNAME}:"
    f"{settings.weyes.PASSWORD}@"
    f"{settings.weyes.HOST}:"
    f"{settings.weyes.PORT}/weyes"
)


async_engine = create_async_engine(DATABASE_URL, echo=False, future=True)

WeyesAsyncSession = async_sessionmaker(
    async_engine, expire_on_commit=False, autoflush=False
)


class VaidationStatusEnum(enum.Enum):
    PENDING = "pending"
    PASSED = "passed"
    FAILED = "failed"


class BaseModel(DeclarativeBase):
    pass


class Questao(BaseModel):
    __tablename__ = "questao"
    id: Mapped[big_intpk]
    codigo: Mapped[str] = mapped_column(VARCHAR(50))
    enunciado: Mapped[str] = mapped_column(VARCHAR(1500))
    entrada: Mapped[str] = mapped_column(VARCHAR(1000))
    saida: Mapped[str] = mapped_column(VARCHAR(1000))
    resolucao: Mapped[str] = mapped_column(VARCHAR(1000))

    exemplos: Mapped[list["Exemplo"]] = relationship(
        "Exemplo", back_populates="questao"
    )
    casos_teste: Mapped[list["CasoTeste"]] = relationship(
        "CasoTeste", back_populates="questao"
    )


class Exemplo(BaseModel):
    __tablename__ = "exemplo"

    id: Mapped[big_intpk]
    questao_id: Mapped[int] = mapped_column(ForeignKey("questao.id"))
    entrada: Mapped[str] = mapped_column(VARCHAR(1000))
    saida: Mapped[str] = mapped_column(VARCHAR(1000))

    questao: Mapped[Questao] = relationship("Questao", back_populates="exemplos")


class CasoTeste(BaseModel):
    __tablename__ = "caso_teste"

    id: Mapped[big_intpk]
    questao_id: Mapped[int] = mapped_column(ForeignKey("questao.id"))
    entrada: Mapped[str] = mapped_column(VARCHAR(1000))
    saida: Mapped[str] = mapped_column(VARCHAR(1000))
    created_at: Mapped[datetime_default_now]
    updated_at: Mapped[datetime_default_now]
    validation_status: Mapped[VaidationStatusEnum] = mapped_column(
        default=VaidationStatusEnum.PENDING
    )

    questao: Mapped[Questao] = relationship("Questao", back_populates="casos_teste")


async def create_all():
    async with async_engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(create_all())
