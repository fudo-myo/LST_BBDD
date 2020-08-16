class RunBasicDto():

    def __init__(self, date=None, hour=None, run_name=None, subrun=None, events=None, length=None,
                 rate=None, size=None, event_type=None):
        self.__date = date
        self.__hour = hour
        self.__run_name = run_name
        self.__subrun = subrun
        self.__events = events
        self.__length = length
        self.__rate = rate
        self.__size = size
        self.__event_type = event_type

    @property
    def date(self):
        return self.__date

    @property
    def hour(self):
        return self.__hour

    @property
    def run_name(self):
        return self.__run_name

    @property
    def subrun(self):
        return self.__subrun

    @property
    def events(self):
        return self.__events

    @property
    def length(self):
        return self.__length

    @property
    def rate(self):
        return self.__rate

    @property
    def size(self):
        return self.__size

    @property
    def event_type(self):
        return self.__event_type

    @date.setter
    def date(self, value):
        self.__date = value

    @hour.setter
    def hour(self, value):
        self.__hour = value

    @run_name.setter
    def run_name(self, value):
        self.__run_name = value

    @subrun.setter
    def subrun(self, value):
        self.__subrun = value

    @events.setter
    def events(self, value):
        self.__events = value

    @length.setter
    def length(self, value):
        self.__length = value

    @rate.setter
    def rate(self, value):
        self.__rate = value

    @size.setter
    def size(self, value):
        self.__size = value

    @event_type.setter
    def event_type(self, value):
        self.__event_type = value

    