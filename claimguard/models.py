from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()

@table_registry.mapped_as_dataclass
class Autorizacao:
    __tablename__ = 'autorizacoes'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    cod_beneficiario: Mapped[str]
    nome: Mapped[str]
    sobrenome: Mapped[str]
    celular: Mapped[int]
    transacao: Mapped[int] = mapped_column(unique=True)
    status: Mapped[str]
    data_solicitacao: Mapped[datetime]
    retorno_beneficiario: Mapped[str]
    registro_envio_em: Mapped[datetime] = mapped_column(init=False, server_default=func.now())