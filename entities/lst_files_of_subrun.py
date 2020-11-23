from sqlalchemy import Table, Column, INTEGER, VARCHAR

from config.base import get_base, get_meta_data, get_engine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(get_engine(), LstTableNames.LST_FILES_OF_SUBRUN):
    class LstFilesOfSubrun(get_base()):
        """This class is the entity is associated with the table `LST_FILES_OF_SUBRUN`

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
        id_file_subrun: int
            primary identifier of the table
        subrun_number: int
            subrun number
        path_file: str
            file path
        num_events: int
            number of events
        array_num_files: str
            TODO include description
        """
        __tablename__ = Table(LstTableNames.LST_FILES_OF_SUBRUN, get_meta_data(), autoload=True,
                              autoload_with=get_engine())
        id_file_subrun = Column('ID_FILE_SUBRUN', INTEGER, primary_key=True, nullable=False)
        subrun_number = Column('SUBRUN_NUMBER', INTEGER, nullable=False)
        path_file = Column('PATH_FILE', VARCHAR(100), nullable=True)
        num_events = Column('NUM_EVENTS', INTEGER, nullable=True)
        array_num_files = Column('ARRAY_NUM_FILES', VARCHAR(50), nullable=True)
