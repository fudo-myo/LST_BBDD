class NightSummaryDto():

    def __init__(self, run_num=None, n_subruns=None, run_type=None, date_fichero=None, registration_date=None,
                 hora=None, event_id_one=None, ts_from_ucts_one=None, tib_ts=None, event_id_two=None,
                 ts_from_ucts_two=None, dragon_ts=None):
        self.__run_num = run_num
        self.__n_subruns = n_subruns
        self.__run_type = run_type
        self.__date_fichero = date_fichero
        self.__registration_date = registration_date
        self.__hora = hora
        self.__event_id_one = event_id_one
        self.__ts_from_ucts_one = ts_from_ucts_one
        self.__tib_ts = tib_ts
        self.__event_id_two = event_id_two
        self.__ts_from_ucts_two = ts_from_ucts_two
        self.__dragon_ts = dragon_ts

    @property
    def run_num(self):
        return self.__run_num

    @property
    def n_subruns(self):
        return self.__n_subruns

    @property
    def run_type(self):
        return self.__run_type

    @property
    def date_fichero(self):
        return self.__date_fichero

    @property
    def registration_date(self):
        return self.__registration_date

    @property
    def hora(self):
        return self.__hora

    @property
    def event_id_one(self):
        return self.__event_id_one

    @property
    def ts_from_ucts_one(self):
        return self.__ts_from_ucts_one

    @property
    def tib_ts(self):
        return self.__tib_ts

    @property
    def event_id_two(self):
        return self.__event_id_two

    @property
    def ts_from_ucts_two(self):
        return self.__ts_from_ucts_two

    @property
    def dragon_ts(self):
        return self.__dragon_ts

    @run_num.setter
    def run_num(self, value):
        self.__run_num = value

    @n_subruns.setter
    def n_subruns(self, value):
        self.__n_subruns = value

    @run_type.setter
    def run_type(self, value):
        self.__run_type = value

    @date_fichero.setter
    def date_fichero(self, value):
        self.__date_fichero = value

    @registration_date.setter
    def registration_date(self, value):
        self.__registration_date = value

    @hora.setter
    def hora(self, value):
        self.__hora = value

    @event_id_one.setter
    def event_id_one(self, value):
        self.__event_id_one = value

    @ts_from_ucts_one.setter
    def ts_from_ucts_one(self, value):
        self.__ts_from_ucts_one = value

    @ts_from_ucts_one.setter
    def ts_from_ucts_one(self, value):
        self.__ts_from_ucts_one = value

    @tib_ts.setter
    def tib_ts(self, value):
        self.__tib_ts = value

    @event_id_two.setter
    def event_id_two(self, value):
        self.__event_id_two = value

    @ts_from_ucts_two.setter
    def ts_from_ucts_two(self, value):
        self.__ts_from_ucts_two = value

    @dragon_ts.setter
    def dragon_ts(self, value):
        self.__dragon_ts = value
