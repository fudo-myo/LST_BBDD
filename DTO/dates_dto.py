class DatesDto:

    def __init__(self, id_date=None, date_dto=None):
        self.__id_date = id_date
        self.__date_dto = date_dto

    @property
    def id_date(self):
        return self.__id_date

    @property
    def date_dto(self):
        return self.__date_dto

    @id_date.setter
    def id_date(self, value):
        self.__id_date = value

    @date_dto.setter
    def date_dto(self, value):
        self.__date_dto = value


def create_date(id_date, date_dto):
    dto = DatesDto()
    dto.id_date = id_date
    dto.date_dto = date_dto
    return dto
