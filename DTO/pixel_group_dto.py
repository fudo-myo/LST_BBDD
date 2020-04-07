class PixelGroupDto:

    def __init__(self, id_pixel_group=None, pixel_group_number=None, id_config=None, other_data=None):
        self.__id_pixel_group = id_pixel_group
        self.__pixel_group_number = pixel_group_number
        self.__id_config = id_config
        self.__other_data = other_data

    @property
    def id_pixel_group(self):
        return self.__id_pixel_group

    @property
    def pixel_group_number(self):
        return self.__pixel_group_number

    @property
    def id_config(self):
        return self.__id_config

    @property
    def other_data(self):
        return self.__other_data

    @id_pixel_group.setter
    def id_pixel_group(self, value):
        self.__id_pixel_group = value

    @pixel_group_number.setter
    def pixel_group_number(self, value):
        self.__pixel_group_number = value

    @id_config.setter
    def id_config(self, value):
        self.__id_config = value

    @other_data.setter
    def other_data(self, value):
        self.__other_data = value

def create_pixel_group(id_pixel_group, pixel_group_number, id_config, other_data):
    dto = PixelGroupDto()
    dto.id_pixel_group = id_pixel_group
    dto.pixel_group_number = pixel_group_number
    dto.id_config = id_config
    dto.other_data = other_data
    return dto
