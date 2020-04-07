class RunTypeDto:

    def __init__(self, id_run_type=None, description_run_type=None):
        self.__id_run_type = id_run_type
        self.__description_run_type = description_run_type

    @property
    def id_run_type(self):
        return self.__id_run_type

    @property
    def description_run_type(self):
        return self.__description_run_type

    @id_run_type.setter
    def id_run_type(self, value):
        self.__id_run_type = value

    @description_run_type.setter
    def description_run_type(self, value):
        self.__description_run_type = value


def create_run_type(id_run_type, description_run_type):
    dto = RunTypeDto()
    dto.id_run_type = id_run_type
    dto.description_run_type = description_run_type
    return dto
