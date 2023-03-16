import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec

from settings import settings

SqlAlchemyBase = dec.declarative_base()

__factory = None


# Создание и подключение к БД
def global_init():
    global __factory

    if __factory:
        return

    conn_str = settings.DB_URL
    print(f"Подключение к базе данных по адресу {conn_str}")

    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    SqlAlchemyBase.metadata.create_all(engine)


# Создание ссесии с БД
def create_session() -> Session:
    global __factory
    return __factory()
