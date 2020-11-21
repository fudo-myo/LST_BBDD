from sqlalchemy import Table, Column, INTEGER, VARCHAR

from config.base import get_base, get_meta_data, get_engine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(get_engine(), LstTableNames.LST_CONFIGURATION):
    class LstConfiguration(get_base()):
        """This class is the entity is associated with the table `LST_CONFIGURATION`

        Arguments
        ---------
        get_base(): declarative_base()
            The new base class will be given a metaclass that produces
            appropriate :class:`~sqlalchemy.schema.Table` objects and makes
            the appropriate :func:`~sqlalchemy.orm.mapper` calls based on the
            information provided declaratively in the class and any subclasses
            of the class.

        Attributes
        ----------
        tablename: str
            database table name
        id_config: int
            primary identifier of the table
        config_description: str
            Description of camera settings
        param_1: str
            auxiliary parameter to include relevant information
        param_2: str
            auxiliary parameter to include relevant information
        param_3: str
            auxiliary parameter to include relevant information
        """
        __tablename__ = Table(LstTableNames.LST_CONFIGURATION, get_meta_data(), autoload=True, autoload_with=get_engine())
        id_config = Column('ID_CONFIG', INTEGER, primary_key=True)
        config_description = Column('CONFIG_DESCRIPTION', VARCHAR(50), nullable=True)
        param_1 = Column('PARAM_1', VARCHAR(45), nullable=True)
        param_2 = Column('PARAM_2', VARCHAR(45), nullable=True)
        param_3 = Column('PARAM_3', VARCHAR(45), nullable=True)

