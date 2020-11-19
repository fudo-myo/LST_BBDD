from sqlalchemy import Table, Column, INTEGER

from config.base import get_base, get_meta_data, get_engine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(get_engine(), LstTableNames.LST_R1_DATA_CHECK_ANALYSIS):
    class LstR1DataCheckAnalysis(get_base()):
        __tablename__ = Table(LstTableNames.LST_R1_DATA_CHECK_ANALYSIS, get_meta_data(), autoload=True, autoload_with=get_engine())
        id_record = Column('ID_RECORD', INTEGER, primary_key=True,autoincrement=True, nullable=False)
        id_r1_data_check = Column('ID_R1_DATA_CHECK', INTEGER, primary_key=True, autoincrement=False, nullable=False)
        run_number = Column('RUN_NUMBER', INTEGER, nullable=False)
        id_r1_data_check_specific = Column('ID_R1_DATA_CHECK_SPECIFIC', INTEGER, nullable=False)
