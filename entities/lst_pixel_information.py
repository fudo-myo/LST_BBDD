from sqlalchemy import Table, Column, INTEGER, FLOAT

from config.base import get_base, get_meta_data, get_engine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(get_engine(), LstTableNames.LST_PIXEL_INFORMATION):
    class LstPixelInformation(get_base()):
        __tablename__ = Table(LstTableNames.LST_PIXEL_INFORMATION, get_meta_data(), autoload=True,
                              autoload_with=get_engine())
        id_record = Column('ID_RECORD', INTEGER, primary_key=True, autoincrement=True, nullable=False)
        pixel_id = Column('PIXEL_ID', INTEGER, primary_key=True, autoincrement=False, nullable=False)
        pixel_group_number = Column('PIXEL_GROUP_NUMBER', INTEGER, primary_key=True, autoincrement=False,
                                    nullable=False)
        pixel_pos_x = Column('PIXEL_POS_X', FLOAT, nullable=True)
        pixel_pos_y = Column('PIXEL_POS_Y', FLOAT, nullable=True)
        pixel_pos_z = Column('PIXEL_POS_Z', FLOAT, nullable=True)
