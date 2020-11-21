from sqlalchemy import Table, Column, INTEGER, DATE

from config.base import get_base, get_meta_data, get_engine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(get_engine(), LstTableNames.LST_DATES):
    class LstDates(get_base()):
        """This class is the entity is associated with the table `LST_DATES`

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
        id_date: int
            primary identifier of the table
        date_entity: Date
            date field
        """
        __tablename__ = Table(LstTableNames.LST_DATES, get_meta_data(), autoload=True, autoload_with=get_engine())

        id_date = Column('ID_DATE', INTEGER, primary_key=True, autoincrement=True, nullable=False)
        date_entity = Column('DATE', DATE, nullable=False)

