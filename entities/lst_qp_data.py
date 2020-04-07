from sqlalchemy import *

from config.base import getBase, getMetaData, getEngine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(getEngine(), LstTableNames.LST_QP_DATA):
    class LstQpData(getBase()):
        __tablename__ = Table(LstTableNames.LST_QP_DATA, getMetaData(), autoload=True, autoload_with=getEngine())
        id_qp_data = Column('ID_QP_DATA', INTEGER, primary_key=True, nullable=False)
        pixel_id = Column('PIXEL_ID', INTEGER, nullable=False)
        id_dl1a = Column('ID_DL1A', INTEGER, nullable=False)
        q_average = Column('Q_AVERAGE', FLOAT, nullable=True)
        q_rms = Column('Q_RMS', FLOAT, nullable=True)
        time_average = Column('TIME_AVERAGE', FLOAT, nullable=True)
        time_rms = Column('TIME_RMS', FLOAT, nullable=True)
        dl1a_check_build = Column('DL1A_CHECK_BUILD', INTEGER, nullable=True)
