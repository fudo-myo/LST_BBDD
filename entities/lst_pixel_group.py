from sqlalchemy import Table, Column, INTEGER, VARCHAR

from config.base import get_base, get_meta_data, get_engine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(get_engine(), LstTableNames.LST_PIXEL_GROUP):
    class LstPixelGroup(get_base()):
        __tablename__ = Table(LstTableNames.LST_PIXEL_GROUP, get_meta_data(), autoload=True, autoload_with=get_engine())
        id_pixel_group = Column('ID_PIXEL_GROUP', INTEGER, primary_key=True, autoincrement=True, nullable=False)
        pixel_group_number = Column('PIXEL_GROUP_NUMBER', INTEGER, primary_key=True, autoincrement=False,
                                    nullable=False)
        id_config = Column('ID_CONFIG', INTEGER, primary_key=True, autoincrement=False, nullable=False)
        other_data = Column('OTHER_DATA', VARCHAR(50), nullable=True)
