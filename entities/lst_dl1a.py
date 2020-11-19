from sqlalchemy import Table, Column, INTEGER, VARCHAR
from config.base import get_base, get_meta_data, get_engine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(get_engine(), LstTableNames.LST_DL1A):
    class LstDl1a(get_base()):
        __tablename__ = Table(LstTableNames.LST_DL1A, get_meta_data(), autoload=True, autoload_with=get_engine())
        id_dl1a = Column('ID_DL1A', INTEGER, primary_key=True, nullable=False)
        subrun_number = Column('SUBRUN_NUMBER', INTEGER, nullable=False)
        dl1a_path_file = Column('DL1A_PATH_FILE', VARCHAR(100), nullable=True)
