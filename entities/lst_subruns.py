from sqlalchemy import *

from config.base import getBase, getMetaData, getEngine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(getEngine(), LstTableNames.LST_SUBRUNS):
    class LstSubruns(getBase()):
        __tablename__ = Table(LstTableNames.LST_SUBRUNS, getMetaData(), autoload=True, autoload_with=getEngine())
        id_subrun = Column('ID_SUBRUN', INTEGER, primary_key=True, autoincrement=True, nullable=False)
        subrun_number = Column('SUBRUN_NUMBER', INTEGER, primary_key=True, autoincrement=False, nullable=False)
        run_number = Column('RUN_NUMBER', INTEGER, nullable=False)
        id_run_type = Column('ID_RUN_TYPE', INTEGER, nullable=False)
