import uuid
import sqlalchemy as sa
from db.db_session import SqlAlchemyBase
from sqlalchemy.orm import relationship, backref


class User(SqlAlchemyBase):
    __tablename__ = "users"

    uuid = sa.Column(
        sa.Text(length=36),
        default=lambda: str(uuid.uuid4()),
        primary_key=True,
        unique=True,
    )
    username = sa.Column(sa.String)
    email = sa.Column(sa.String)
    password_hash = sa.Column(sa.String)
    # children = relationship('ChildrenClass', back_populates='parent', foreign_keys='Children.uuid', cascade="all")
