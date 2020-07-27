class SubrunsDto:

    def __init__(self, id_subrun=None, subrun_number=None, run_number=None, id_run_type=None, date=None,
                 stream=None, events=None, length=None, rate=None, size=None, event_type=None, process_state=None):
        self.__id_subrun = id_subrun
        self.__subrun_number = subrun_number
        self.__run_number = run_number
        self.__id_run_type = id_run_type
        self.__date = date
        self.__stream = stream
        self.__events = events
        self.__length = length
        self.__rate = rate
        self.__size = size
        self.__event_type = event_type
        self.__process_state = process_state

    @property
    def id_subrun(self):
        return self.__id_subrun

    @property
    def subrun_number(self):
        return self.__subrun_number

    @property
    def run_number(self):
        return self.__run_number

    @property
    def id_run_type(self):
        return self.__id_run_type

    @property
    def date(self):
        return self.__date

    @property
    def stream(self):
        return self.__stream

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

    @property
    def process_state(self):
        return self.__process_state

    @id_subrun.setter
    def id_subrun(self, value):
        self.__id_subrun = value

    @subrun_number.setter
    def subrun_number(self, value):
        self.__subrun_number = value

    @run_number.setter
    def run_number(self, value):
        self.__run_number = value

    @id_run_type.setter
    def id_run_type(self, value):
        self.__id_run_type = value

    @date.setter
    def date(self, value):
        self.__date = value

    @stream.setter
    def stream(self, value):
        self.__stream = value

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

    @process_state.setter
    def process_state(self, value):
        self.__process_state = value


def create_subrun(id_subrun, subrun_number, run_number, id_run_type, date, stream, events,
                  length, rate, size, event_type, process_state):
    dto = SubrunsDto()
    dto.id_subrun = id_subrun
    dto.subrun_number = subrun_number
    dto.run_number = run_number
    dto.id_run_type = id_run_type
    dto.date = date
    dto.stream = stream
    dto.events = events
    dto.length = length
    dto.rate = rate
    dto.size = size
    dto.event_type = event_type
    dto.process_state = process_state
    return dto
