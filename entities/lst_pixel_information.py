from sqlalchemy import *

from config.base import getBase, getMetaData, getEngine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(getEngine(), LstTableNames.LST_PIXEL_INFORMATION):
    class LstPixelInformation(getBase()):
        __tablename__ = Table(LstTableNames.LST_PIXEL_INFORMATION, getMetaData(), autoload=True, autoload_with=getEngine())
        id_record = Column('ID_RECORD', INTEGER, primary_key=True, nullable=False)
        pixel_id = Column('PIXEL_ID', INTEGER, primary_key=True, autoincrement=False, nullable=False)
        pixel_group_number = Column('PIXEL_GROUP_NUMBER', INTEGER, primary_key=True, nullable=False)
        pixel_pos_x = Column('PIXEL_POS_X', FLOAT, nullable=True)
        pixel_pos_y = Column('PIXEL_POS_Y', FLOAT, nullable=True)
        pixel_pos_z = Column('PIXEL_POS_Z', FLOAT, nullable=True)
