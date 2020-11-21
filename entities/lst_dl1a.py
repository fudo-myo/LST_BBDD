from sqlalchemy import Table, Column, INTEGER, VARCHAR
from config.base import get_base, get_meta_data, get_engine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(get_engine(), LstTableNames.LST_DL1A):
    class LstDl1a(get_base()):
        """This class is the entity is associated with the table `LST_DL1A`

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
        id_dl1a: int
            primary identifier of the table
        subrun_number: int
            subrun number
        dl1a_path_file: str
            dl1a file path
        """
        __tablename__ = Table(LstTableNames.LST_DL1A, get_meta_data(), autoload=True, autoload_with=get_engine())
        id_dl1a = Column('ID_DL1A', INTEGER, primary_key=True, nullable=False)
        subrun_number = Column('SUBRUN_NUMBER', INTEGER, nullable=False)
        dl1a_path_file = Column('DL1A_PATH_FILE', VARCHAR(100), nullable=True)
