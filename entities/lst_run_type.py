from sqlalchemy import *

from config.base import getBase, getMetaData, getEngine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(getEngine(), LstTableNames.LST_RUN_TYPE):
    class LstRunType(getBase()):
        __tablename__ = Table(LstTableNames.LST_RUN_TYPE, getMetaData(), autoload=True, autoload_with=getEngine())
        id_run_type = Column('ID_RUN_TYPE', INTEGER, primary_key=True, nullable=False)
        description_run_type = Column('DESCRIPTION_RUN_TYPE', VARCHAR(45), nullable=True)
