from sqlalchemy import Table, Column, INTEGER, VARCHAR
from sqlalchemy.dialects.mysql import DOUBLE

from config.base import get_base, get_meta_data, get_engine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(get_engine(), LstTableNames.LST_ANALYSIS_EVALUATION):
    class LstAnalysisEvaluation(get_base()):
        """This class is the entity is associated with the table `LST_ANALYSIS_EVALUATION`

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
        id_analysis_evaluation: int
            primary identifier of the table
        id_lst_r1_data_check_plot: int
            TODO include description
        parameter_description: str
            TODO include description
        parameter_value: double
            TODO include description
        """
        __tablename__ = Table(LstTableNames.LST_ANALYSIS_EVALUATION, get_meta_data(), autoload=True,
                              autoload_with=get_engine())
        id_analysis_evaluation = Column('ID_ANALYSIS_EVALUATION', INTEGER, primary_key=True, nullable=False)
        id_lst_r1_data_check_plot = Column('ID_LST_R1_DATA_CHECK_PLOT', INTEGER, nullable=False)
        parameter_description = Column('PARAMETER_DESCRIPTION', VARCHAR(30), nullable=False)
        parameter_value = Column('PARAMETER_VALUE', DOUBLE(), nullable=False)
