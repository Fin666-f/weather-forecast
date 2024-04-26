import datetime
import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase


class Data(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'data'

    tempreture = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    speed = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    precipitation = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    pressure = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    humidity = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    home = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)