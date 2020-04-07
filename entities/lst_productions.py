from sqlalchemy import *

from config.base import getBase, getMetaData, getEngine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(getEngine(), LstTableNames.LST_PRODUCTIONS):
    class LstProductions(getBase()):
        __tablename__ = Table(LstTableNames.LST_PRODUCTIONS, getMetaData(), autoload=True, autoload_with=getEngine())
        id_production = Column('ID_PRODUCTION', INTEGER, primary_key=True, nullable=False)
        run_number = Column('RUN_NUMBER', INTEGER, nullable=False)
        id_run_type = Column('ID_RUN_TYPE', INTEGER, nullable=False)
        r1_check_build = Column('R1_CHECK_BUILD', INTEGER, nullable=True)
        dl1a_check_build = Column('DL1A_CHECK_BUILD', INTEGER, nullable=True)
        dl1b_check_build = Column('DL1B_CHECK_BUILD', INTEGER, nullable=True)
        dl2_check_build = Column('DL2_CHECK_BUILD', INTEGER, nullable=True)
        number_production = Column('NUMBER_PRODUCTION', INTEGER, nullable=True)
