from sqlalchemy import Table, Column, INTEGER, VARCHAR

from config.base import get_base, get_meta_data, get_engine
from utils.checkers import Checkers
from utils.table_names import LstTableNames

if Checkers.check_table_exists(get_engine(), LstTableNames.LST_R1_DATA_CHECK_PLOT):
    class LstR1DataCheckPlot(get_base()):
        __tablename__ = Table(LstTableNames.LST_R1_DATA_CHECK_PLOT, get_meta_data(), autoload=True,
                              autoload_with=get_engine())
        id_record = Column('ID_RECORD', INTEGER, primary_key=True, autoincrement=True, nullable=False)
        id_lst_r1_data_check_plot = Column('ID_LST_R1_DATA_CHECK_PLOT', INTEGER, primary_key=True, autoincrement=False,
                                           nullable=False)
        id_r1_data_check = Column('ID_R1_DATA_CHECK', INTEGER, nullable=True)
        lst_r1_data_check_plot_path = Column('LST_R1_DATA_CHECK_PLOT_PATH', VARCHAR(120), nullable=False)
        lst_r1_data_check_plot_description = Column('LST_R1_DATA_CHECK_PLOT_DESCRIPTION', VARCHAR(100), nullable=False)
