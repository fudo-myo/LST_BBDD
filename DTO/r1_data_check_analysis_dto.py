class R1DataCheckAnalysisDto:

    def __init__(self,id_record=None, id_r1_data_check=None, run_number=None, id_r1_data_check_specific=None):
        self.__id_record = id_record
        self.__id_r1_data_check = id_r1_data_check
        self.__run_number = run_number
        self.__id_r1_data_check_specific = id_r1_data_check_specific

    @property
    def id_record(self):
        return self.__id_record

    @property
    def id_r1_data_check(self):
        return self.__id_r1_data_check

    @property
    def run_number(self):
        return self.__run_number

    @property
    def id_r1_data_check_specific(self):
        return self.__id_r1_data_check_specific

    @id_record.setter
    def id_record(self, value):
        self.__id_record = value

    @id_r1_data_check.setter
    def id_r1_data_check(self, value):
        self.__id_r1_data_check = value

    @run_number.setter
    def run_number(self, value):
        self.__run_number = value

    @id_r1_data_check_specific.setter
    def id_r1_data_check_specific(self, value):
        self.__id_r1_data_check_specific = value


def create_r1_data_check_analysis(id_record, id_r1_data_check, run_number, id_r1_data_check_specific):
    dto = R1DataCheckAnalysisDto()
    dto.id_record = id_record
    dto.id_r1_data_check = id_r1_data_check
    dto.run_number = run_number
    dto.id_r1_data_check_specific = id_r1_data_check_specific
    return dto
