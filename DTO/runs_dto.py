class RunsDto:

    def __init__(self, id_run=None, run_number=None, id_run_type=None, date=None, id_config=None, id_production=None,
                 path_file=None, init_ra=None, end_ra=None,
                 init_dec=None, end_dec=None, init_altitude=None, end_altitude=None, init_azimuth=None,
                 end_azimuth=None, init_time_collect_data=None,
                 end_time_collect_data=None):
        self.__id_run = id_run
        self.__run_number = run_number
        self.__id_run_type = id_run_type
        self.__date = date
        self.__id_config = id_config
        self.__id_production = id_production
        self.__path_file = path_file
        self.__init_ra = init_ra
        self.__end_ra = end_ra
        self.__init_dec = init_dec
        self.__end_dec = end_dec
        self.__init_altitude = init_altitude
        self.__end_altitude = end_altitude
        self.__init_azimuth = init_azimuth
        self.__end_azimuth = end_azimuth
        self.__init_time_collect_data = init_time_collect_data
        self.__end_time_collect_data = end_time_collect_data

    @property
    def id_run(self):
        return self.__id_run

    @property
    def run_number(self):
        return self.__run_number

    @property
    def id_run_type(self):
        return self.__id_run_type

    @property
    def date(self):
        return self.__date

    @property
    def id_config(self):
        return self.__id_config

    @property
    def id_production(self):
        return self.__id_production

    @property
    def path_file(self):
        return self.__path_file

    @property
    def init_ra(self):
        return self.__init_ra

    @property
    def end_ra(self):
        return self.__end_ra

    @property
    def init_dec(self):
        return self.__init_dec

    @property
    def end_dec(self):
        return self.__end_dec

    @property
    def init_altitude(self):
        return self.__init_altitude

    @property
    def end_altitude(self):
        return self.__end_altitude

    @property
    def init_azimuth(self):
        return self.__init_azimuth

    @property
    def end_azimuth(self):
        return self.__end_azimuth

    @property
    def init_time_collect_data(self):
        return self.__init_time_collect_data

    @property
    def end_time_collect_data(self):
        return self.__end_time_collect_data

    @id_run.setter
    def id_run(self, value):
        self.__id_run = value

    @run_number.setter
    def run_number(self, value):
        self.__run_number = value

    @id_run_type.setter
    def id_run_type(self, value):
        self.__id_run_type = value

    @date.setter
    def date(self, value):
        self.__date = value

    @id_config.setter
    def id_config(self, value):
        self.__id_config = value

    @id_production.setter
    def id_production(self, value):
        self.__id_production = value

    @path_file.setter
    def path_file(self, value):
        self.__path_file = value

    @init_ra.setter
    def init_ra(self, value):
        self.__init_ra = value

    @end_ra.setter
    def end_ra(self, value):
        self.__end_ra = value

    @init_dec.setter
    def init_dec(self, value):
        self.__init_dec = value

    @end_dec.setter
    def end_dec(self, value):
        self.__end_dec = value

    @init_altitude.setter
    def init_altitude(self, value):
        self.__init_altitude = value

    @end_altitude.setter
    def end_altitude(self, value):
        self.__end_altitude = value

    @init_azimuth.setter
    def init_azimuth(self, value):
        self.__init_azimuth = value

    @end_azimuth.setter
    def end_azimuth(self, value):
        self.__end_azimuth = value

    @init_time_collect_data.setter
    def init_time_collect_data(self, value):
        self.__init_time_collect_data = value

    @end_time_collect_data.setter
    def end_time_collect_data(self, value):
        self.__end_time_collect_data = value


def create_runs(id_run, run_number, id_run_type, date, id_config, id_production, path_file, init_ra, end_ra,
                init_dec, end_dec, init_altitude, end_altitude, init_azimuth, end_azimuth, init_time_collect_data,
                end_time_collect_data):
    dto = RunsDto()
    dto.id_run = id_run
    dto.run_number = run_number
    dto.id_run_type = id_run_type
    dto.date = date
    dto.id_config = id_config
    dto.id_production = id_production
    dto.path_file = path_file
    dto.init_ra = init_ra
    dto.end_ra = end_ra
    dto.init_dec = init_dec
    dto.end_dec = end_dec
    dto.init_altitude = init_altitude
    dto.end_altitude = end_altitude
    dto.init_azimuth = init_azimuth
    dto.end_azimuth = end_azimuth
    dto.init_time_collect_data = init_time_collect_data
    dto.end_time_collect_data = end_time_collect_data
    return dto
