class SubrunsDto:

    def __init__(self, id_subrun=None, subrun_number=None, id_run=None, date=None, hour=None,
                 stream=None, events=None, length=None, rate=None, size=None, event_type=None, process_state=None,
                 waveform_data=None, waveform_filter=None, counter_data=None, counter_filter=None):
        self.__id_subrun = id_subrun
        self.__subrun_number = subrun_number
        self.__id_run = id_run
        self.__date = date
        self.__hour = hour
        self.__stream = stream
        self.__events = events
        self.__length = length
        self.__rate = rate
        self.__size = size
        self.__event_type = event_type
        self.__process_state = process_state
        self.__waveform_data = waveform_data
        self.__waveform_filter = waveform_filter
        self.__counter_data = counter_data
        self.__counter_filter = counter_filter

    @property
    def id_subrun(self):
        return self.__id_subrun

    @property
    def subrun_number(self):
        return self.__subrun_number

    @property
    def id_run(self):
        return self.__id_run

    @property
    def date(self):
        return self.__date

    @property
    def hour(self):
        return self.__hour

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

    @property
    def waveform_data(self):
        return self.__waveform_data

    @property
    def waveform_filter(self):
        return self.__waveform_filter

    @property
    def counter_data(self):
        return self.__counter_data

    @property
    def counter_filter(self):
        return self.__counter_filter

    @id_subrun.setter
    def id_subrun(self, value):
        self.__id_subrun = value

    @subrun_number.setter
    def subrun_number(self, value):
        self.__subrun_number = value

    @id_run.setter
    def id_run(self, value):
        self.__id_run = value

    @date.setter
    def date(self, value):
        self.__date = value

    @hour.setter
    def hour(self, value):
        self.__hour = value

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

    @waveform_data.setter
    def waveform_data(self, value):
        self.__waveform_data = value

    @waveform_filter.setter
    def waveform_filter(self, value):
        self.__waveform_filter = value

    @counter_data.setter
    def counter_data(self, value):
        self.__counter_data = value

    @counter_filter.setter
    def counter_filter(self, value):
        self.__counter_filter = value


def create_subrun(id_subrun, subrun_number, id_run, date, hour, stream, events,
                  length, rate, size, event_type, process_state, waveform_data, waveform_filter, counter_data, counter_filter ):
    dto = SubrunsDto()
    dto.id_subrun = id_subrun
    dto.subrun_number = subrun_number
    dto.id_run = id_run
    dto.date = date
    dto.hour = hour
    dto.stream = stream
    dto.events = events
    dto.length = length
    dto.rate = rate
    dto.size = size
    dto.event_type = event_type
    dto.process_state = process_state
    dto.waveform_data = waveform_data
    dto.waveform_filter = waveform_filter
    dto.counter_data = counter_data
    dto.counter_filter = counter_filter
    return dto
