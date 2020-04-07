class QpDataDto:

    def __init__(self, id_qp_data=None, pixel_id=None, id_dl1a=None, q_average=None, q_rms=None, time_average=None,
                 time_rms=None, dl1a_check_build=None):
        self.__id_qp_data = id_qp_data
        self.__pixel_id = pixel_id
        self.__id_dl1a = id_dl1a
        self.__q_average = q_average
        self.__q_rms = q_rms
        self.__time_average = time_average
        self.__time_rms = time_rms
        self.__dl1a_check_build = dl1a_check_build

    @property
    def id_qp_data(self):
        return self.__id_qp_data

    @property
    def pixel_id(self):
        return self.__pixel_id

    @property
    def id_dl1a(self):
        return self.__id_dl1a

    @property
    def q_average(self):
        return self.__q_average

    @property
    def q_rms(self):
        return self.__q_rms

    @property
    def time_average(self):
        return self.__time_average

    @property
    def time_rms(self):
        return self.__time_rms

    @property
    def dl1a_check_build(self):
        return self.__dl1a_check_build

    @id_qp_data.setter
    def id_qp_data(self, value):
        self.__id_qp_data = value

    @pixel_id.setter
    def pixel_id(self, value):
        self.__pixel_id = value

    @id_dl1a.setter
    def id_dl1a(self, value):
        self.__id_dl1a = value

    @q_average.setter
    def q_average(self, value):
        self.__q_average = value

    @q_rms.setter
    def q_rms(self, value):
        self.__q_rms = value

    @time_average.setter
    def time_average(self, value):
        self.__time_average = value

    @time_rms.setter
    def time_rms(self, value):
        self.__time_rms = value

    @dl1a_check_build.setter
    def dl1a_check_build(self, value):
        self.__dl1a_check_build = value


def create_qp_data(id_qp_data, pixel_id, id_dl1a, q_average, q_rms, time_average,
                   time_rms, dl1a_check_build):
    dto = QpDataDto()
    dto.id_qp_data = id_qp_data
    dto.pixel_id = pixel_id
    dto.id_dl1a = id_dl1a
    dto.q_average = q_average
    dto.q_rms = q_rms
    dto.time_average = time_average
    dto.time_rms = time_rms
    dto.dl1a_check_build = dl1a_check_build
    return dto
