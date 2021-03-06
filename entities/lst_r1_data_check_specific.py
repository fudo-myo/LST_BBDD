from sqlalchemy import *

from config.base import getBase, getMetaData, getEngine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(getEngine(), LstTableNames.LST_R1_DATA_CHECK_SPECIFIC):
    class LstR1DataCheckSpecific(getBase()):
        __tablename__ = Table(LstTableNames.LST_R1_DATA_CHECK_SPECIFIC, getMetaData(), autoload=True, autoload_with=getEngine())
        id_r1_data_check_specific = Column('ID_R1_DATA_CHECK_SPECIFIC', INTEGER, primary_key=True, nullable=False)
        init_event = Column('INIT_EVENT', INTEGER, nullable=False)
        end_event = Column('END_EVENT', INTEGER, nullable=False)
        init_pixel = Column('INIT_PIXEL', INTEGER, nullable=False)
        end_pixel = Column('END_PIXEL', INTEGER, nullable=False)
        init_sample = Column('INIT_SAMPLE', INTEGER, nullable=False)
        end_sample = Column('END_SAMPLE', INTEGER, nullable=False)
        init_subrun = Column('INIT_SUBRUN', INTEGER, nullable=False)
        end_subrun = Column('END_SUB_RUN', INTEGER, nullable=False)
        type_of_gap_calc = Column('TYPE_OF_GAP_CALC', VARCHAR(50), nullable=False)
        list_of_module_in_detail = Column('LIST_OF_MODULE_IN_DETAIL', VARCHAR(1060), nullable=False)
