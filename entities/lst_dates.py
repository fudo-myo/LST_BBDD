from sqlalchemy import *

from config.base import getBase, getMetaData, getEngine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(getEngine(), LstTableNames.LST_DATES):
    class LstDates(getBase()):
        __tablename__ = Table(LstTableNames.LST_DATES, getMetaData(), autoload=True, autoload_with=getEngine())

        id_date = Column('ID_DATE', INTEGER, primary_key=True, nullable=False)
        date = Column('DATE', DATETIME, primary_key=True, autoincrement=False, nullable=False)
