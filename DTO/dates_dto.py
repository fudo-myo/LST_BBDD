class DatesDto:
    """
    This class is the transfer object of the `LST_DATES` table.

    Attributes
    ----------
    id_date: int
        primary identifier of the table
    date_dto: Date
        date field
    """
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
    """
    This method create a DTO for Dates and set every field with
    the paremeters given as arguments

    Arguments
    ---------
    id_date: int
        primary identifier of the table
    date_dto: Date
        date field

    Returns
    -------
    DatesDto:
        returns an instance of the transfer object
    """
    dto = DatesDto()
    dto.id_date = id_date
    dto.date_dto = date_dto
    return dto
