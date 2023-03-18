import sqlalchemy
from db.db_session import SqlAlchemyBase
from sqlalchemy.orm import relationship, backref


class User(SqlAlchemyBase):
    __tablename__ = "users"

    uuid = sqlalchemy.Column(sqlalchemy.UUID(as_uuid=True), unique=True, primary_key=True)
    username = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String)
    password_hash = sqlalchemy.Column(sqlalchemy.String)
    # children = relationship('ChildrenClass', back_populates='parent', foreign_keys='Children.uuid', cascade="all")
