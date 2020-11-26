from sqlalchemy import Table, Column, INTEGER, VARCHAR

from config.base import get_base, get_meta_data, get_engine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(get_engine(), LstTableNames.LST_PIXEL_GROUP):
    class LstPixelGroup(get_base()):
        """This class is the entity is associated with the table `LST_PIXEL_GROUP`

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
        id_pixel_group: int
            primary identifier of the table
        pixel_group_number: int
            pixel group number
        id_config: int
            camera configuration identifier
        other_data: str
            auxiliary parameter to include any relevant data
        """
        __tablename__ = Table(LstTableNames.LST_PIXEL_GROUP, get_meta_data(), autoload=True, autoload_with=get_engine())
        id_pixel_group = Column('ID_PIXEL_GROUP', INTEGER, primary_key=True, autoincrement=True, nullable=False)
        pixel_group_number = Column('PIXEL_GROUP_NUMBER', INTEGER, primary_key=True, autoincrement=False,
                                    nullable=False)
        id_config = Column('ID_CONFIG', INTEGER, primary_key=True, autoincrement=False, nullable=False)
        other_data = Column('OTHER_DATA', VARCHAR(50), nullable=True)
