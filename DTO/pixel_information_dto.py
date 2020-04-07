class PixelInformationDto:

    def __init__(self, id_record=None, pixel_id=None, pixel_group_number=None, pixel_pos_x=None, pixel_pos_y=None,
                 pixel_pos_z=None):
        self.__id_record = id_record
        self.__pixel_id = pixel_id
        self.__pixel_group_number = pixel_group_number
        self.__pixel_pos_x = pixel_pos_x
        self.__pixel_pos_y = pixel_pos_y
        self.__pixel_pos_z = pixel_pos_z

    @property
    def id_record(self):
        return self.__id_record

    @property
    def pixel_id(self):
        return self.__pixel_id

    @property
    def pixel_group_number(self):
        return self.__pixel_group_number

    @property
    def pixel_pos_x(self):
        return self.__pixel_pos_x

    @property
    def pixel_pos_y(self):
        return self.__pixel_pos_y

    @property
    def pixel_pos_z(self):
        return self.__pixel_pos_z

    @id_record.setter
    def id_record(self, value):
        self.__id_record = value

    @pixel_id.setter
    def pixel_id(self, value):
        self.__pixel_id = value

    @pixel_group_number.setter
    def pixel_group_number(self, value):
        self.__pixel_group_number = value

    @pixel_pos_x.setter
    def pixel_pos_x(self, value):
        self.__pixel_pos_x = value

    @pixel_pos_y.setter
    def pixel_pos_y(self, value):
        self.__pixel_pos_y = value

    @pixel_pos_z.setter
    def pixel_pos_z(self, value):
        self.__pixel_pos_z = value


def create_pixel_information(id_record, pixel_id, pixel_group_number, pixel_pos_x, pixel_pos_y, pixel_pos_z):
    dto = PixelInformationDto()
    dto.id_record = id_record
    dto.pixel_id = pixel_id
    dto.pixel_group_number = pixel_group_number
    dto.pixel_pos_x = pixel_pos_x
    dto.pixel_pos_y = pixel_pos_y
    dto.pixel_pos_z = pixel_pos_z
    return dto
