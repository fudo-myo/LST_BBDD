from sqlalchemy import *

from config.base import getEngine, getBase, getMetaData
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(getEngine(), LstTableNames.LST_SOURCES):
    class LstSources(getBase()):
        __tablename__ = Table(LstTableNames.LST_SOURCES, getMetaData(), autoload=True, autoload_with=getEngine())
        id_source = Column('ID_SOURCE', INTEGER, primary_key=True, autoincrement=True, nullable=False)
        source_des = Column('SOURCE_DES', VARCHAR(50), nullable=False)
        right_asc = Column('RIGHT_ASC', FLOAT, nullable=True)
        declination = Column('DECLINATION', FLOAT, nullable=True)
        altitude = Column('ALTITUDE', FLOAT, nullable=True)
        azimuth = Column('AZIMUTH', FLOAT, nullable=True)
        right_asc_off_set = Column('RIGHT_ASC_OFF_SET', FLOAT, nullable=True)
        declination_off_set = Column('DECLINATION_OFF_SET', FLOAT, nullable=True)
        altitude_off_set = Column('ALTITUDE_OFF_SET', FLOAT, nullable=True)
        azimuth_off_set = Column('AZIMUTH_OFF_SET', FLOAT, nullable=True)

