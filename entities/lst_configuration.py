from sqlalchemy import *

from config.base import getBase, getMetaData, getEngine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(getEngine(), LstTableNames.LST_CONFIGURATION):
    class LstConfiguration(getBase()):
        __tablename__ = Table(LstTableNames.LST_CONFIGURATION, getMetaData(), autoload=True, autoload_with=getEngine())
        id_config = Column('ID_CONFIG', Integer, primary_key=True)
        config_description = Column('CONFIG_DESCRIPTION', VARCHAR(50), nullable=True)
        param_1 = Column('PARAM_1', VARCHAR(45), nullable=True)
        param_2 = Column('PARAM_2', VARCHAR(45), nullable=True)
        param_3 = Column('PARAM_3', VARCHAR(45), nullable=True)

