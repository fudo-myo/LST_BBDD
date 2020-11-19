from sqlalchemy import Table, Column, INTEGER, DATE

from config.base import get_base, get_meta_data, get_engine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(get_engine(), LstTableNames.LST_DATES):
    class LstDates(get_base()):
        __tablename__ = Table(LstTableNames.LST_DATES, get_meta_data(), autoload=True, autoload_with=get_engine())

        id_date = Column('ID_DATE', INTEGER, primary_key=True, autoincrement=True, nullable=False)
        date_entity = Column('DATE', DATE, nullable=False)

