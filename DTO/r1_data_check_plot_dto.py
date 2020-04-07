class R1DataCheckPlotDto:

    def __init__(self, id_record=None, id_lst_r1_data_check_plot=None, id_r1_data_check=None,
                 lst_r1_data_check_plot_path=None,
                 lst_r1_data_check_plot_description=None):
        self.__id_record = id_record
        self.__id_lst_r1_data_check_plot = id_lst_r1_data_check_plot
        self.__id_r1_data_check = id_r1_data_check
        self.__lst_r1_data_check_plot_path = lst_r1_data_check_plot_path
        self.__lst_r1_data_check_plot_description = lst_r1_data_check_plot_description

    @property
    def id_record(self):
        return self.__id_record

    @property
    def id_lst_r1_data_check_plot(self):
        return self.__id_lst_r1_data_check_plot

    @property
    def id_r1_data_check(self):
        return self.__id_r1_data_check

    @property
    def lst_r1_data_check_plot_path(self):
        return self.__lst_r1_data_check_plot_path

    @property
    def lst_r1_data_check_plot_description(self):
        return self.__lst_r1_data_check_plot_description

    @id_record.setter
    def id_record(self, value):
        self.__id_record = value

    @id_lst_r1_data_check_plot.setter
    def id_lst_r1_data_check_plot(self, value):
        self.__id_lst_r1_data_check_plot = value

    @id_r1_data_check.setter
    def id_r1_data_check(self, value):
        self.__id_r1_data_check = value

    @lst_r1_data_check_plot_path.setter
    def lst_r1_data_check_plot_path(self, value):
        self.__lst_r1_data_check_plot_path = value

    @lst_r1_data_check_plot_description.setter
    def lst_r1_data_check_plot_description(self, value):
        self.__lst_r1_data_check_plot_description = value


def create_r1_data_check_plot(id_record, id_lst_r1_data_check_plot, id_r1_data_check, lst_r1_data_check_plot_path,
                              lst_r1_data_check_plot_description):
    dto = R1DataCheckPlotDto()
    dto.id_record = id_record
    dto.id_lst_r1_data_check_plot = id_lst_r1_data_check_plot
    dto.id_r1_data_check = id_r1_data_check
    dto.lst_r1_data_check_plot_path = lst_r1_data_check_plot_path
    dto.lst_r1_data_check_plot_description = lst_r1_data_check_plot_description
    return dto
