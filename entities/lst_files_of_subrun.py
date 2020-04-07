from sqlalchemy import *

from config.base import getBase, getMetaData, getEngine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(getEngine(), LstTableNames.LST_FILES_OF_SUBRUN):
    class LstFilesOfSubrun(getBase()):
        __tablename__ = Table(LstTableNames.LST_FILES_OF_SUBRUN, getMetaData(), autoload=True,
                              autoload_with=getEngine())
        id_file_subrun = Column('ID_FILE_SUBRUN', INTEGER, primary_key=True, nullable=False)
        subrun_number = Column('SUBRUN_NUMBER', INTEGER, nullable=False)
        path_file = Column('PATH_FILE', VARCHAR(100), nullable=True)
        num_events = Column('NUM_EVENTS', INTEGER, nullable=True)
        array_num_files = Column('ARRAY_NUM_FILES', VARCHAR(50), nullable=True)
