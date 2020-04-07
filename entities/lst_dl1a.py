from sqlalchemy import *

from config.base import getBase, getMetaData, getEngine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(getEngine(), LstTableNames.LST_DL1A):
    class LstDl1a(getBase()):
        __tablename__ = Table(LstTableNames.LST_DL1A, getMetaData(), autoload=True, autoload_with=getEngine())
        id_dl1a = Column('ID_DL1A', INTEGER, primary_key=True, nullable=False)
        subrun_number = Column('SUBRUN_NUMBER', INTEGER, nullable=False)
        dl1a_path_file = Column('DL1A_PATH_FILE', VARCHAR(100), nullable=True)
