from sqlalchemy import Table, Column, INTEGER, VARCHAR

from config.base import get_base, get_meta_data, get_engine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(get_engine(), LstTableNames.LST_CONFIGURATION):
    class LstConfiguration(get_base()):
        __tablename__ = Table(LstTableNames.LST_CONFIGURATION, get_meta_data(), autoload=True, autoload_with=get_engine())
        id_config = Column('ID_CONFIG', INTEGER, primary_key=True)
        config_description = Column('CONFIG_DESCRIPTION', VARCHAR(50), nullable=True)
        param_1 = Column('PARAM_1', VARCHAR(45), nullable=True)
        param_2 = Column('PARAM_2', VARCHAR(45), nullable=True)
        param_3 = Column('PARAM_3', VARCHAR(45), nullable=True)

