from test_project import db
from pecan import conf
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
#import sqlite
import sqlalchemy
from sqlalchemy import Boolean, Column
from sqlalchemy import ForeignKey, Integer
from sqlalchemy import schema, String, Text
from sqlalchemy.ext.declarative import declarative_base
from test_project.model import  model

Base = declarative_base()


Session = scoped_session(sessionmaker())
metadata = MetaData()

def _engine_from_config(configuration):
    configuration = dict(configuration)
    url = configuration.pop('url')
    return create_engine(url, **configuration)

def init_model():
    db.createDataBase()
    conf.sqlalchemy.engine = _engine_from_config(conf.sqlalchemy)
    Base.metadata.create_all(bind=conf.sqlalchemy.engine)

def start():
    Session.bind = conf.sqlalchemy.engine
    metadata.bind = Session.bind

def commit():
    Session.commit()

def rollback():
    Session.rollback()

def clear():
    Session.remove()

