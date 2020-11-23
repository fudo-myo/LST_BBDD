class FilesOfSubrunDto:
    """
    This class is the transfer object of the `LST_FILES_OF_SUBRUN` table.

    Attributes
    ----------
    id_file_subrun: int
        primary identifier of the table
    subrun_number: int
        subrun number
    path_file: str
        file path
    num_events: int
        number of events
    array_num_files: str
        TODO include description
    """

    def __init__(self, id_file_subrun=None, subrun_number=None, path_file=None, num_events=None, array_num_files=None):
        self.__id_file_subrun = id_file_subrun
        self.__subrun_number = subrun_number
        self.__path_file = path_file
        self.__num_events = num_events
        self.__array_num_files = array_num_files

    @property
    def id_file_subrun(self):
        return self.__id_file_subrun

    @property
    def subrun_number(self):
        return self.__subrun_number

    @property
    def path_file(self):
        return self.__path_file

    @property
    def num_events(self):
        return self.__num_events

    @property
    def array_num_files(self):
        return self.__array_num_files

    @id_file_subrun.setter
    def id_file_subrun(self, value):
        self.__id_file_subrun = value

    @subrun_number.setter
    def subrun_number(self, value):
        self.__subrun_number = value

    @path_file.setter
    def path_file(self, value):
        self.__path_file = value

    @num_events.setter
    def num_events(self, value):
        self.__num_events = value

    @array_num_files.setter
    def array_num_files(self, value):
        self.__array_num_files = value


def create_files_of_subrun(id_file_subrun, subrun_number, path_file, num_events, array_num_files):
    """
    This method create a DTO for Files of Subrun and set every field with
    the paremeters given as arguments

    Arguments
    ---------
    id_file_subrun: int
        primary identifier of the table
    subrun_number: int
        subrun number
    path_file: str
        file path
    num_events: int
        number of events
    array_num_files: str
        TODO include description

    Returns
    -------
    FilesOfSubrunDto:
        returns an instance of the transfer object
    """
    dto = FilesOfSubrunDto()
    dto.id_file_subrun = id_file_subrun
    dto.subrun_number = subrun_number
    dto.path_file = path_file
    dto.num_events = num_events
    dto.array_num_files = array_num_files
    return dto
