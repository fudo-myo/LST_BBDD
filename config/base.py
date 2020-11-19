# coding=utf-8
import os
import sys

from sqlalchemy import create_engine, MetaData
from sqlalchemy.exc import OperationalError, SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from utils.checkers import Checkers

if os.getenv("TEST_PROFILE") == "test_mode":
    engine = create_engine('mysql://franrome:g.4lan_SB]IpRVYs@muon.gae.ucm.es:3306/DataBase_LST_1_franrome_test',
                           echo=True)
else:
    engine = create_engine('mysql://franrome:g.4lan_SB]IpRVYs@muon.gae.ucm.es:3306/DataBase_LST_1_franrome', echo=True)
    # engine = create_engine('mysql://root:LST1-bigtelescranrome:g.4lan_SB]IpRope@muon.gae.ucm.es:3306/DataBase_LST_1_franrome', echo=True)

try:
    conn = engine.connect()
    session_maker = sessionmaker(bind=engine)
    session = session_maker()
    metadata = MetaData()
except OperationalError as error:
    Checkers.print_exception_two_params(error.orig.args[1], error.orig.args[0])
    engine.dispose()
    sys.exit()


def get_session():
    return session


def get_base():
    try:
        return declarative_base()
    except SQLAlchemyError as error:
        Checkers.print_exception_two_params(error, error)


def get_engine():
    return engine


def get_meta_data():
    return metadata
