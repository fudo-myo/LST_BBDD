from sqlalchemy import Table, Column, INTEGER

from config.base import get_base, get_meta_data, get_engine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(get_engine(), LstTableNames.LST_PRODUCTIONS):
    class LstProductions(get_base()):
        __tablename__ = Table(LstTableNames.LST_PRODUCTIONS, get_meta_data(), autoload=True, autoload_with=get_engine())
        id_production = Column('ID_PRODUCTION', INTEGER, primary_key=True, nullable=False)
        run_number = Column('RUN_NUMBER', INTEGER, nullable=False)
        id_run_type = Column('ID_RUN_TYPE', INTEGER, nullable=False)
        r1_check_build = Column('R1_CHECK_BUILD', INTEGER, nullable=True)
        dl1a_check_build = Column('DL1A_CHECK_BUILD', INTEGER, nullable=True)
        dl1b_check_build = Column('DL1B_CHECK_BUILD', INTEGER, nullable=True)
        dl2_check_build = Column('DL2_CHECK_BUILD', INTEGER, nullable=True)
        number_production = Column('NUMBER_PRODUCTION', INTEGER, nullable=True)
