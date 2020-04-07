from sqlalchemy import *

from config.base import getBase, getMetaData, getEngine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(getEngine(), LstTableNames.LST_RUN_TYPE):
    class LstRuns(getBase()):
        __tablename__ = Table(LstTableNames.LST_RUN_TYPE, getMetaData(), autoload=True, autoload_with=getEngine())
        id_run = Column('ID_RUN', INTEGER, primary_key=True, nullable=False)
        run_number = Column('RUN_NUMBER', INTEGER, nullable=False)
        id_run_type = Column('ID_RUN_TYPE', INTEGER, nullable=False)
        date = Column('DATE', DATE, nullable=False)
        id_config = Column('ID_CONFIG', INTEGER, nullable=False)
        id_production = Column('ID_PRODUCTION', INTEGER, nullable=True)
        path_file = Column('PATH_FILE', VARCHAR(100), nullable=True)
        init_ra = Column('INIT_RA', FLOAT, nullable=True)
        end_ra = Column('END_RA', FLOAT, nullable=True)
        init_dec = Column('INIT_DEC', FLOAT, nullable=True)
        end_dec = Column('END_DEC', FLOAT, nullable=True)
        init_altitude = Column('INIT_ALTITUDE', FLOAT, nullable=True)
        end_altitude = Column('END_ALTITUDE', FLOAT, nullable=True)
        init_azimuth = Column('INIT_AZIMUTH', FLOAT, nullable=True)
        end_azimuth = Column('END_AZIMUTH', FLOAT, nullable=True)
        init_time_collect_data = Column('INIT_TIME_COLLECT_DATA', DATETIME, nullable=True)
        end_time_collect_data = Column('END_TIME_COLLECT_DATA', DATETIME, nullable=True)
