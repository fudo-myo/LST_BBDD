from sqlalchemy import Table, Column, INTEGER, Date, Time, VARCHAR, FLOAT

from config.base import get_base, get_meta_data, get_engine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(get_engine(), LstTableNames.LST_SUBRUNS):
    class LstSubruns(get_base()):
        __tablename__ = Table(LstTableNames.LST_SUBRUNS, get_meta_data(), autoload=True, autoload_with=get_engine())
        id_subrun = Column('ID_SUBRUN', INTEGER, primary_key=True, autoincrement=True, nullable=False)
        subrun_number = Column('SUBRUN_NUMBER', INTEGER, nullable=False)
        id_run = Column('ID_RUN', INTEGER, nullable=False)
        date = Column('DATE', Date, nullable=True)
        hour = Column('HOUR', Time, nullable=True)
        stream = Column('STREAM', VARCHAR(20), nullable=True)
        events = Column('EVENTS', INTEGER, nullable=True)
        length = Column('LENGTH', FLOAT, nullable=True)
        rate = Column('RATE', FLOAT, nullable=True)
        size = Column('SIZE', VARCHAR(12), nullable=True)
        event_type = Column('EVENT_TYPE', VARCHAR(40), nullable=True)
        process_state = Column('PROCESS_STATE', VARCHAR(15), nullable=True)
        waveform_data = Column('WAVEFORM_DATA', VARCHAR(255), nullable=True)
        waveform_filter = Column('WAVEFORM_FILTER', VARCHAR(255), nullable=True)
        counter_data = Column('COUNTER_DATA', VARCHAR(255), nullable=True)
        counter_filter = Column('COUNTER_FILTER', VARCHAR(255), nullable=True)
