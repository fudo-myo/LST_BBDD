from sqlalchemy import *

from config.base import getBase, getMetaData, getEngine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(getEngine(), LstTableNames.LST_R1_DATA_CHECK_GENERIC):
    class LstR1DataCheckGeneric(getBase()):
        __tablename__ = Table(LstTableNames.LST_R1_DATA_CHECK_GENERIC, getMetaData(), autoload=True, autoload_with=getEngine())
        id_r1_data_check_generic = Column('ID_R1_DATA_CHECK_GENERIC', INTEGER, primary_key=True, nullable=False)
        init_event = Column('INIT_EVENT', INTEGER, nullable=True)
        end_event = Column('END_EVENT', INTEGER, nullable=True)
        init_pixel = Column('INIT_PIXEL', INTEGER, nullable=True)
        end_pixel = Column('END_PIXEL', INTEGER, nullable=True)
        init_sample = Column('INIT_SAMPLE', INTEGER, nullable=True)
        end_sample = Column('END_SAMPLE', INTEGER, nullable=True)
        init_subrun = Column('INIT_SUBRUN', INTEGER, nullable=True)
        end_subrun = Column('END_SUB_RUN', INTEGER, nullable=True)
        type_of_gap_calc = Column('TYPE_OF_GAP_CALC', VARCHAR(50), nullable=True)
        list_of_module_in_detail = Column('LIST_OF_MODULE_IN_DETAIL', VARCHAR(1060), nullable=True)
