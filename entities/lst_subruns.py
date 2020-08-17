from sqlalchemy import *

from config.base import getBase, getMetaData, getEngine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(getEngine(), LstTableNames.LST_SUBRUNS):
    class LstSubruns(getBase()):
        __tablename__ = Table(LstTableNames.LST_SUBRUNS, getMetaData(), autoload=True, autoload_with=getEngine())
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
