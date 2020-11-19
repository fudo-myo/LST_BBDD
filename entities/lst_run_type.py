from sqlalchemy import Table, Column, INTEGER, VARCHAR

from config.base import get_base, get_meta_data, get_engine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(get_engine(), LstTableNames.LST_RUN_TYPE):
    class LstRunType(get_base()):
        __tablename__ = Table(LstTableNames.LST_RUN_TYPE, get_meta_data(), autoload=True, autoload_with=get_engine())
        id_run_type = Column('ID_RUN_TYPE', INTEGER, primary_key=True, nullable=False)
        description_run_type = Column('DESCRIPTION_RUN_TYPE', VARCHAR(45), nullable=True)
