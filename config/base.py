# coding=utf-8
import sys

from sqlalchemy import create_engine, MetaData
from sqlalchemy.exc import OperationalError, SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from utils.checkers import Checkers

engine = create_engine('mysql://franrome:g.4lan_SB]IpRVYs@muon.gae.ucm.es:3306/DataBase_LST_1_franrome', echo=True)
# engine = create_engine('mysql://root:LST1-bigtelescope@muon.gae.ucm.es:3306/DataBase_LST_1_franrome', echo=True)
try:
    conn = engine.connect()
    session_maker = sessionmaker(bind=engine)
    session = session_maker()
    metadata = MetaData()
except OperationalError as error:
    Checkers.print_exception_two_params(error.orig.args[1], error.orig.args[0])
    engine.dispose()
    sys.exit()


def getSession():
    return session


def getBase():
    try:
        return declarative_base()
    except SQLAlchemyError as error:
        Checkers.print_exception_two_params(error, error)
def getBase2(name):
    if Checkers.check_table_exists(getEngine(), name):
        return declarative_base()


def getEngine():
    return engine


def getMetaData():
    return metadata
