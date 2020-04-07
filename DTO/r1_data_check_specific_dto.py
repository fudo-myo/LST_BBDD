class R1DataCheckSpecificDto:

    def __init__(self, id_r1_data_check_specific=None, init_event=None, end_event=None, init_pixel=None, end_pixel=None,
                 init_sample=None, end_sample=None,
                 init_subrun=None, end_subrun=None, type_of_gap_calc=None, list_of_module_in_detail=None):
        self.__id_r1_data_check_specific = id_r1_data_check_specific
        self.__init_event = init_event
        self.__end_event = end_event
        self.__init_pixel = init_pixel
        self.__end_pixel = end_pixel
        self.__init_sample = init_sample
        self.__end_sample = end_sample
        self.__init_subrun = init_subrun
        self.__end_subrun = end_subrun
        self.__type_of_gap_calc = type_of_gap_calc
        self.__list_of_module_in_detail = list_of_module_in_detail

    @property
    def id_r1_data_check_specific(self):
        return self.__id_r1_data_check_specific

    @property
    def init_event(self):
        return self.__init_event

    @property
    def end_event(self):
        return self.__end_event

    @property
    def init_pixel(self):
        return self.__init_pixel

    @property
    def end_pixel(self):
        return self.__end_pixel

    @property
    def init_sample(self):
        return self.__init_sample

    @property
    def end_sample(self):
        return self.__end_sample

    @property
    def init_subrun(self):
        return self.__init_subrun

    @property
    def end_subrun(self):
        return self.__end_subrun

    @property
    def type_of_gap_calc(self):
        return self.__type_of_gap_calc

    @property
    def list_of_module_in_detail(self):
        return self.__list_of_module_in_detail

    @id_r1_data_check_specific.setter
    def id_r1_data_check_specific(self, value):
        self.__id_r1_data_check_specific = value

    @init_event.setter
    def init_event(self, value):
        self.__init_event = value

    @end_event.setter
    def end_event(self, value):
        self.__end_event = value

    @init_pixel.setter
    def init_pixel(self, value):
        self.__init_pixel = value

    @end_pixel.setter
    def end_pixel(self, value):
        self.__end_pixel = value

    @init_sample.setter
    def init_sample(self, value):
        self.__init_sample = value

    @end_sample.setter
    def end_sample(self, value):
        self.__end_sample = value

    @init_subrun.setter
    def init_subrun(self, value):
        self.__init_subrun = value

    @end_subrun.setter
    def end_subrun(self, value):
        self.__end_subrun = value

    @type_of_gap_calc.setter
    def type_of_gap_calc(self, value):
        self.__type_of_gap_calc = value

    @list_of_module_in_detail.setter
    def list_of_module_in_detail(self, value):
        self.__list_of_module_in_detail = value


def create_r1_data_check_specific(id_r1_data_check_specific, init_event, end_event, init_pixel, end_pixel, init_sample,
                                  end_sample,
                                  init_subrun, end_subrun, type_of_gap_calc, list_of_module_in_detail):
    dto = R1DataCheckSpecificDto()
    dto.id_r1_data_check_specific = id_r1_data_check_specific
    dto.init_event = init_event
    dto.end_event = end_event
    dto.init_pixel = init_pixel
    dto.end_pixel = end_pixel
    dto.init_sample = init_sample
    dto.end_sample = end_sample
    dto.init_subrun = init_subrun
    dto.end_subrun = end_subrun
    dto.type_of_gap_calc = type_of_gap_calc
    dto.list_of_module_in_detail = list_of_module_in_detail
    return dto
