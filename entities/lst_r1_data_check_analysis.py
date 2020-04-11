from sqlalchemy import *

from config.base import getBase, getMetaData, getEngine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(getEngine(), LstTableNames.LST_R1_DATA_CHECK_ANALYSIS):
    class LstR1DataCheckAnalysis(getBase()):
        __tablename__ = Table(LstTableNames.LST_R1_DATA_CHECK_ANALYSIS, getMetaData(), autoload=True, autoload_with=getEngine())
        id_record = Column('ID_RECORD', INTEGER, primary_key=True,autoincrement=True, nullable=False)
        id_r1_data_check = Column('ID_R1_DATA_CHECK', INTEGER, primary_key=True, autoincrement=False, nullable=False)
        run_number = Column('RUN_NUMBER', INTEGER, nullable=False)
        id_r1_data_check_specific = Column('ID_R1_DATA_CHECK_SPECIFIC', INTEGER, nullable=False)
