class Dl1aDto:

    def __init__(self, id_dl1a=None, subrun_number=None, dl1a_path_file=None):
        self.__id_dl1a = id_dl1a
        self.__subrun_number = subrun_number
        self.__dl1a_path_file = dl1a_path_file

    @property
    def id_dl1a(self):
        return self.__id_dl1a

    @property
    def subrun_number(self):
        return self.__subrun_number

    @property
    def dl1a_path_file(self):
        return self.__dl1a_path_file

    @id_dl1a.setter
    def id_dl1a(self, value):
        self.__id_dl1a = value

    @subrun_number.setter
    def subrun_number(self, value):
        self.__subrun_number = value

    @dl1a_path_file.setter
    def dl1a_path_file(self, value):
        self.__dl1a_path_file = value


def create_dl1a(id_dl1a, subrun_number, dl1a_path_file):
    dto = Dl1aDto()
    dto.id_dl1a = id_dl1a
    dto.subrun_number = subrun_number
    dto.dl1a_path_file = dl1a_path_file
    return dto
