class DatesDto:

    def __init__(self, id_date=None, date_time=None):
        self.__id_date = id_date
        self.__date_time = date_time

    @property
    def id_date(self):
        return self.__id_date

    @property
    def date_time(self):
        return self.__date_time

    @id_date.setter
    def id_date(self, value):
        self.__id_date = value

    @date_time.setter
    def date_time(self, value):
        self.__date_time = value


def create_date(id_date, date_time):
    dto = DatesDto()
    dto.id_date = id_date
    dto.date_time = date_time
    return dto
