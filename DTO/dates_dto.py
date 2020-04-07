class DatesDto:

    def __init__(self, id_date=None, date=None):
        self.__id_date = id_date
        self.__date = date

    @property
    def id_date(self):
        return self.__id_date

    @property
    def date(self):
        return self.__date

    @id_date.setter
    def id_date(self, value):
        self.__id_date = value

    @date.setter
    def date(self, value):
        self.__date = value


def create_date(id_date, date):
    dto = DatesDto()
    dto.id_date = id_date
    dto.date = date
    return dto
