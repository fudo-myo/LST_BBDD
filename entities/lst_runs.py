from sqlalchemy import Column, Table, INTEGER, FLOAT, VARCHAR, DateTime, Date, Time

from config.base import get_base, get_meta_data, get_engine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(get_engine(), LstTableNames.LST_RUNS):
    class LstRuns(get_base()):
        __tablename__ = Table(LstTableNames.LST_RUNS, get_meta_data(), autoload=True, autoload_with=get_engine())
        id_run = Column('ID_RUN', INTEGER, primary_key=True, nullable=False)
        run_number = Column('RUN_NUMBER', INTEGER, nullable=False)
        id_run_type = Column('ID_RUN_TYPE', INTEGER, nullable=False)
        id_date = Column('ID_DATE', INTEGER, nullable=False)
        date = Column('DATE', Date, nullable=True)
        hour = Column('HOUR', Time, nullable=True)
        id_config = Column('ID_CONFIG', INTEGER, nullable=False)
        number_of_subrun = Column('NUMBER_OF_SUBRUN', INTEGER, nullable=True)
        events = Column('EVENTS', INTEGER, nullable=True)
        length = Column('LENGTH', FLOAT, nullable=True)
        rate = Column('RATE', FLOAT, nullable=True)
        size = Column('SIZE', VARCHAR(12), nullable=True)
        event_type = Column('EVENT_TYPE', VARCHAR(40), nullable=True)
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
        init_time_collect_data = Column('INIT_TIME_COLLECT_DATA', DateTime, nullable=True)
        end_time_collect_data = Column('END_TIME_COLLECT_DATA', DateTime, nullable=True)
        id_source = Column('ID_SOURCE', INTEGER, nullable=True)
        source_des = Column('SOURCE_DES', VARCHAR(50), nullable=True)
