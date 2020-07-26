class ConfigurationDto:

    def __init__(self, id_config=None, config_description=None, param_1=None, param_2=None, param_3=None):
        self.__id_config = id_config
        self.__config_description = config_description
        self.__param_1 = param_1
        self.__param_2 = param_2
        self.__param_3 = param_3

    @property
    def id_config(self):
        return self.__id_config

    @property
    def config_description(self):
        return self.__config_description

    @property
    def param_1(self):
        return self.__param_1

    @property
    def param_2(self):
        return self.__param_2

    @property
    def param_3(self):
        return self.__param_3

    @config_description.setter
    def config_description(self, value):
        self.__config_description = value

    @param_1.setter
    def param_1(self, value):
        self.__param_1 = value

    @param_2.setter
    def param_2(self, value):
        self.__param_2 = value

    @param_3.setter
    def param_3(self, value):
        self.__param_3 = value

    @id_config.setter
    def id_config(self, value):
        self.__id_config = value




def create_configuration(id_config, config_description, param_1, param_2, param_3):
    dto = ConfigurationDto()
    dto.id_config = id_config
    dto.config_description = config_description
    dto.param_1 = param_1
    dto.param_2 = param_2
    dto.param_3 = param_3
    return dto
