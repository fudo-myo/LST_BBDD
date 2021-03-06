from sqlalchemy import *
from sqlalchemy.dialects.mysql import DOUBLE

from config.base import getBase, getMetaData, getEngine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(getEngine(), LstTableNames.LST_ANALYSIS_EVALUATION):
    class LstAnalysisEvaluation(getBase()):
        __tablename__ = Table(LstTableNames.LST_ANALYSIS_EVALUATION, getMetaData(), autoload=True, autoload_with=getEngine())
        id_analysis_evaluation = Column('ID_ANALYSIS_EVALUATION', INTEGER, primary_key=True, nullable=False)
        id_lst_r1_data_check_plot = Column('ID_LST_R1_DATA_CHECK_PLOT', INTEGER, nullable=False)
        parameter_description = Column('PARAMETER_DESCRIPTION', VARCHAR(30), nullable=False)
        parameter_value = Column('PARAMETER_VALUE', DOUBLE(), nullable=False)
