from sqlalchemy import *

from config.base import getBase, getMetaData, getEngine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(getEngine(), LstTableNames.LST_R1_DATA_CHECK_PLOT):
    class LstR1DataCheckPlot(getBase()):
        __tablename__ = Table(LstTableNames.LST_R1_DATA_CHECK_PLOT, getMetaData(), autoload=True, autoload_with=getEngine())
        id_record = Column('ID_RECORD', INTEGER, primary_key=True, nullable=False)
        id_lst_r1_data_check_plot = Column('ID_LST_R1_DATA_CHECK_PLOT', INTEGER, primary_key=True, autoincrement=False,
                                           nullable=False)
        id_r1_data_check = Column('ID_R1_DATA_CHECK', INTEGER, nullable=True)
        lst_r1_data_check_plot_path = Column('LST_R1_DATA_CHECK_PLOT_PATH', VARCHAR(120), nullable=False)
        lst_r1_data_check_plot_description = Column('LST_R1_DATA_CHECK_PLOT_DESCRIPTION', VARCHAR(100), nullable=False)
