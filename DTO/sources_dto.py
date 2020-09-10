class SourcesDto:

    def __init__(self, id_source=None, source_des=None, right_asc=None, declination=None, altitude=None, azimuth=None,
                 right_asc_off_set=None,
                 declination_off_set=None, altitude_off_set=None, azimuth_off_set=None):
        self.__id_source = id_source
        self.__source_des = source_des
        self.__right_asc = right_asc
        self.__declination = declination
        self.__altitude = altitude
        self.__azimuth = azimuth
        self.__right_asc_off_set = right_asc_off_set
        self.__declination_off_set = declination_off_set
        self.__altitude_off_set = altitude_off_set
        self.__azimuth_off_set = azimuth_off_set

    @property
    def id_source(self):
        return self.__id_source

    @property
    def source_des(self):
        return self.__source_des

    @property
    def right_asc(self):
        return self.__right_asc

    @property
    def declination(self):
        return self.__declination

    @property
    def altitude(self):
        return self.__altitude

    @property
    def azimuth(self):
        return self.__azimuth

    @property
    def right_asc_off_set(self):
        return self.__right_asc_off_set

    @property
    def declination_off_set(self):
        return self.__declination_off_set

    @property
    def altitude_off_set(self):
        return self.__altitude_off_set

    @property
    def azimuth_off_set(self):
        return self.__azimuth_off_set

    @id_source.setter
    def id_source(self, value):
        self.__id_source = value

    @source_des.setter
    def source_des(self, value):
        self.__source_des = value

    @right_asc.setter
    def right_asc(self, value):
        self.__right_asc = value

    @declination.setter
    def declination(self, value):
        self.__declination = value

    @altitude.setter
    def altitude(self, value):
        self.__altitude = value

    @azimuth.setter
    def azimuth(self, value):
        self.__azimuth = value

    @right_asc_off_set.setter
    def right_asc_off_set(self, value):
        self.__right_asc_off_set = value

    @declination_off_set.setter
    def declination_off_set(self, value):
        self.__declination_off_set = value

    @altitude_off_set.setter
    def altitude_off_set(self, value):
        self.__altitude_off_set = value

    @azimuth_off_set.setter
    def azimuth_off_set(self, value):
        self.__azimuth_off_set = value


def create_source(id_source, source_des, right_asc, declination, altitude, azimuth, right_asc_off_set,
                  declination_off_set, altitude_off_set, azimuth_off_set):
    dto = SourcesDto()
    dto.id_source = id_source
    dto.source_des = source_des
    dto.right_asc = right_asc
    dto.declination = declination
    dto.altitude = altitude
    dto.azimuth = azimuth
    dto.right_asc_off_set = right_asc_off_set
    dto.declination_off_set = declination_off_set
    dto.altitude_off_set = altitude_off_set
    dto.azimuth_off_set = azimuth_off_set
    return dto
