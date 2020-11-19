from sqlalchemy import Table, Column, INTEGER, VARCHAR, FLOAT

from config.base import get_engine, get_base, get_meta_data
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(get_engine(), LstTableNames.LST_SOURCES):
    class LstSources(get_base()):
        __tablename__ = Table(LstTableNames.LST_SOURCES, get_meta_data(), autoload=True, autoload_with=get_engine())
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

