class SubrunsDto:

    def __init__(self, id_subrun=None, subrun_number=None, run_number=None, id_run_type=None):
        self.__id_subrun = id_subrun
        self.__subrun_number = subrun_number
        self.__run_number = run_number
        self.__id_run_type = id_run_type

    @property
    def id_subrun(self):
        return self.__id_subrun

    @property
    def subrun_number(self):
        return self.__subrun_number

    @property
    def run_number(self):
        return self.__run_number

    @property
    def id_run_type(self):
        return self.__id_run_type

    @id_subrun.setter
    def id_subrun(self, value):
        self.__id_subrun = value

    @subrun_number.setter
    def subrun_number(self, value):
        self.__subrun_number = value

    @run_number.setter
    def run_number(self, value):
        self.__run_number = value

    @id_run_type.setter
    def id_run_type(self, value):
        self.__id_run_type = value


def create_subrun(id_subrun, subrun_number, run_number, id_run_type):
    dto = SubrunsDto()
    dto.id_subrun = id_subrun
    dto.subrun_number = subrun_number
    dto.run_number = run_number
    dto.id_run_type = id_run_type
    return dto
