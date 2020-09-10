import os
from datetime import datetime
from typing import List

from DTO.configuration_dto import ConfigurationDto
from DTO.dates_dto import DatesDto
from DTO.read_files_objects.run_basic_dto import RunBasicDto
from DTO.runs_dto import RunsDto
from services.lst_configuraction_service import LstConfigurationService
from services.lst_dates_service import LstDatesService
from services.lst_run_type_service import LstRunTypeService
from services.lst_runs_service import LstRunsService
from utils.cleaner_files import CleanerFiles

dir = 'C:\\Users\\fjromero\\Documents\\cta\\BBDD_ISIDRO\\basic_and_standard'
files_list = CleanerFiles.get_basic_and_standard_files_current_year(os.listdir(dir), "basic", year_to_compare=2020)

# WE CREATE AN INSTANCE OF EACH SERVICE ASSOCIATED WITH THE
# TABLES IN WHICH WE WILL INSERT RECORDS
dates_service = LstDatesService()
run_service = LstRunsService()
config_service = LstConfigurationService()
run_type_service = LstRunTypeService()

list_object_to_insert = []

# THE CONFIGURATIONS ARE INTRODUCED BY DEFAULT
configurations = ['LSTCam-002', 'LSTCam-003', 'NectarCam', 'NectarCam-003', 'MAGICCam']

# WE INSERT THE CONFIGURATIONS AND ONLY ENTER THE NON-EXISTING
# IN ITS ASSOCIATED TABLE
for i in configurations:
    config_aux = ConfigurationDto()
    config_aux.config_description = i
    config_list: List[ConfigurationDto] = config_service.get_all_config()
    flag_config = False
    for conf in config_list:
        if conf.config_description == i:
            flag_config = True
            break
    if not flag_config:
        config_service.insert_config(config_aux)

for i in files_list:
    file = open(dir + f"\\{i}", "r")
    print(dir + f"\\{i}")
    lines = CleanerFiles.clean_header_and_footer(file.readlines())
    for j in lines:
        # THIS REMOVE FINAL BREAK LINE
        j = j.rstrip()
        split_string = j.split(" ")
        clean_list = []
        for k in split_string:
            if k != "":
                clean_list.append(k)
        CleanerFiles.nan_to_none(clean_list)
        object_to_insert = RunBasicDto()

        # ONE MUST BE SUBTRACTED BECAUSE THE DATE IS COLLECTED FROM THE FILE NAME NOT FROM THE CLEAN LIST
        CleanerFiles.check_list_dimensions(clean_list, len(object_to_insert.__dict__.keys())-1)
        object_to_insert.date_fichero = CleanerFiles.get_date_from_basic_files(i)
        object_to_insert.registration_date = clean_list[0]
        object_to_insert.hour = clean_list[1]
        object_to_insert.run_name = CleanerFiles.check_run_number(clean_list[2])
        object_to_insert.subrun = clean_list[3]
        object_to_insert.events = clean_list[4]
        object_to_insert.length = clean_list[5]
        object_to_insert.rate = clean_list[6]
        object_to_insert.size = clean_list[7]

        # TWO MUST BE SUBTRACTED BECAUSE IT IS FROM THE ELEMENT OF THE CLEAN LIST THAT THE EVENT TYPE PART BEGINS
        object_to_insert.event_type = CleanerFiles.check_event_type(clean_list,
                                                                    len(object_to_insert.__dict__.keys()) - 2)
        list_object_to_insert.append(object_to_insert)
        print("prueba")

for object_aux in list_object_to_insert:
    dates: List[DatesDto] = dates_service.get_all_dates()
    date_dto = DatesDto()
    date_dto.date_dto = object_aux.date_fichero
    flag_date = False
    for date_aux in dates:
        if date_aux.date_dto == date_dto.date_dto:
            flag_date = True
            break
    if not flag_date:
        dates_service.insert_dates(date_dto)

    runs_list: List[RunsDto] = run_service.get_all_runs()
    flag_run = False
    run_aux = RunsDto()
    for run in runs_list:
        if run.run_number == object_aux.run_name:
            run_aux.id_run = run.id_run
            run_aux.run_number = object_aux.run_name
            run_aux.id_date = dates_service.get_date_by_id(date_dto.date_dto).id_date
            run_aux.date = object_aux.registration_date
            run_aux.hour = object_aux.hour
            run_aux.number_of_subrun = object_aux.subrun
            run_aux.events = object_aux.events
            run_aux.length = object_aux.length
            run_aux.rate = object_aux.rate
            run_aux.size = object_aux.size
            run_aux.event_type = object_aux.event_type
            flag_run = True
            break
    if flag_run:
        run_service.update_runs(run_aux.id_run, run_aux.run_number, None, run_aux.id_date, run_aux.date, run_aux.hour,
                                None, run_aux.number_of_subrun, run_aux.events, run_aux.length, run_aux.rate,
                                run_aux.size, run_aux.event_type, None, None, None, None, None, None, None, None,
                                None, None, None, None)
