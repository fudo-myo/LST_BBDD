class ProductionsDto:

    def __init__(self, id_production=None, run_number=None, id_run_type=None, r1_check_build=None,
                 dl1a_check_build=None, dl1b_check_build=None, dl2_check_build=None, number_production=None):
        self.__id_production = id_production
        self.__run_number = run_number
        self.__id_run_type = id_run_type
        self.__r1_check_build = r1_check_build
        self.__dl1a_check_build = dl1a_check_build
        self.__dl1b_check_build = dl1b_check_build
        self.__dl2_check_build = dl2_check_build
        self.__number_production = number_production

    @property
    def id_production(self):
        return self.__id_production

    @property
    def run_number(self):
        return self.__run_number

    @property
    def id_run_type(self):
        return self.__id_run_type

    @property
    def r1_check_build(self):
        return self.__r1_check_build

    @property
    def dl1a_check_build(self):
        return self.__dl1a_check_build

    @property
    def dl1b_check_build(self):
        return self.__dl1b_check_build

    @property
    def dl2_check_build(self):
        return self.__dl2_check_build

    @property
    def number_production(self):
        return self.__number_production

    @id_production.setter
    def id_production(self, value):
        self.__id_production = value

    @run_number.setter
    def run_number(self, value):
        self.__run_number = value

    @id_run_type.setter
    def id_run_type(self, value):
        self.__id_run_type = value

    @r1_check_build.setter
    def r1_check_build(self, value):
        self.__r1_check_build = value

    @dl1a_check_build.setter
    def dl1a_check_build(self, value):
        self.__dl1a_check_build = value

    @dl1b_check_build.setter
    def dl1b_check_build(self, value):
        self.__dl1b_check_build = value

    @dl2_check_build.setter
    def dl2_check_build(self, value):
        self.__dl2_check_build = value

    @number_production.setter
    def number_production(self, value):
        self.__number_production = value


def create_productions(id_production, run_number, id_run_type, r1_check_build,
                       dl1a_check_build, dl1b_check_build, dl2_check_build, number_production):
    dto = ProductionsDto()
    dto.id_production = id_production
    dto.run_number = run_number
    dto.id_run_type = id_run_type
    dto.r1_check_build = r1_check_build
    dto.dl1a_check_build = dl1a_check_build
    dto.dl1b_check_build = dl1b_check_build
    dto.dl2_check_build = dl2_check_build
    dto.number_production = number_production
    return dto
