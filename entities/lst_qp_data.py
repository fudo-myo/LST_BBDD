from sqlalchemy import Table, Column, INTEGER, FLOAT

from config.base import get_base, get_meta_data, get_engine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(get_engine(), LstTableNames.LST_QP_DATA):
    class LstQpData(get_base()):
        __tablename__ = Table(LstTableNames.LST_QP_DATA, get_meta_data(), autoload=True, autoload_with=get_engine())
        id_qp_data = Column('ID_QP_DATA', INTEGER, primary_key=True, nullable=False)
        pixel_id = Column('PIXEL_ID', INTEGER, nullable=False)
        id_dl1a = Column('ID_DL1A', INTEGER, nullable=False)
        q_average = Column('Q_AVERAGE', FLOAT, nullable=True)
        q_rms = Column('Q_RMS', FLOAT, nullable=True)
        time_average = Column('TIME_AVERAGE', FLOAT, nullable=True)
        time_rms = Column('TIME_RMS', FLOAT, nullable=True)
        dl1a_check_build = Column('DL1A_CHECK_BUILD', INTEGER, nullable=True)
