from flask_sqlalchemy import SQLAlchemy


class User(db.Model):
    __tablename__ = "users"

    uuid = db.Column(db.UUID(as_uuid=True), unique=True, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password_hash = db.Column(db.String)
    # children = relationship('ChildrenClass', back_populates='parent', foreign_keys='Children.uuid', cascade="all")
