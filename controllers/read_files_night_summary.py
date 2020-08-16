
import os
from datetime import datetime
from typing import List

from DTO.configuration_dto import ConfigurationDto
from DTO.dates_dto import DatesDto
from DTO.read_files_objects.night_summary_dto import NightSummaryDto
from DTO.run_type_dto import RunTypeDto
from DTO.runs_dto import RunsDto
from services.lst_configuraction_service import LstConfigurationService
from services.lst_dates_service import LstDatesService
from services.lst_run_type_service import LstRunTypeService
from services.lst_runs_service import LstRunsService
from utils.cleaner_files import CleanerFiles

dir = 'C:\\Users\\fjromero\\Documents\\cta\\BBDD_ISIDRO\\night_summary'
# WE COLLECT THE NIGHT SUMMARY FILES FROM THE YEAR TO COMPARE UNTIL THE PRESENT YEAR
files_list = CleanerFiles.get_night_summary_files_current_year(os.listdir(dir), year_to_compare=2020)

list_object_to_insert = []

# WE CREATE AN INSTANCE OF EACH SERVICE ASSOCIATED WITH THE
# TABLES IN WHICH WE WILL INSERT RECORDS
dates_service = LstDatesService()
run_service = LstRunsService()
config_service = LstConfigurationService()
run_type_service = LstRunTypeService()

# THE CONFIGURATIONS ARE INTRODUCED BY DEFAULT
configurations = ['LSTCam-002','LSTCam-003','NectarCam','NectarCam-003','MAGICCam']

# WE INSERT THE CONFIGURATIONS AND ONLY ENTER THE NON-EXISTING
# IN ITS ASSOCIATED TABLE
for i in configurations:
    config_aux = ConfigurationDto()
    config_aux.config_description = i
    config_list: List[ConfigurationDto] = config_service.get_all_config()
    flag_config = False
    for conf in config_list:
        if conf.config_description == i:
            flag_config=True
            break
    if not flag_config:
        config_service.insert_config(config_aux)

# WE INSERT THE NIGHT SUMMARY FILES, AND ADD INFORMATION TO THE
# OBJECT THAT HAS A COLUMN ASSOCIATED IN THE CORRESPONDING TABLE,
# THE REST OF PARAMETERS OF MOMENT ARE NOT USED
for i in files_list:
    file = open(dir+f"\\{i}","r")
    print(dir+f"\\{i}")
    lines = file.readlines()
    for j in lines:
        j = j.rstrip()
        split_string = j.split(" ")
        clean_list =[]
        for k in split_string:
            if k != "":
                clean_list.append(k)
        CleanerFiles.nan_to_none(clean_list)
        object_to_insert = NightSummaryDto()
        CleanerFiles.check_list_dimensions(clean_list,len(object_to_insert.__dict__.keys()))
        object_to_insert.run_num = clean_list[0]
        object_to_insert.n_subruns = clean_list[1]
        object_to_insert.run_type = clean_list[2]
        object_to_insert.fecha = clean_list[3]
        object_to_insert.hora = clean_list[4]
        object_to_insert.event_id_one = clean_list[5]
        object_to_insert.ts_from_ucts_one = clean_list[6]
        object_to_insert.tib_ts = clean_list[7]
        object_to_insert.event_id_two = clean_list[8]
        object_to_insert.ts_from_ucts_two = clean_list[9]
        object_to_insert.dragon_ts = clean_list[10]
        list_object_to_insert.append(object_to_insert)
for object_aux in list_object_to_insert:
    date_time_string = object_aux.fecha+" "+object_aux.hora
    date_time = datetime.strptime(date_time_string, '%Y-%m-%d %H:%M:%S')
    dates: List[DatesDto] = dates_service.get_all_dates()
    run_type_list: List[RunTypeDto] = run_type_service.get_all_run_type()
    date_dto = DatesDto()
    date_dto.date_time = date_time
    flag_date =False
    for date_aux in dates:
        if date_aux.date_time == date_dto.date_time:
            flag_date =True
            break
    if not flag_date:
        dates_service.insert_dates(date_dto)

    flag_run_type = False
    run_type_to_insert = RunTypeDto()
    run_type_to_insert.description_run_type =object_aux.run_type
    for run_type_aux in run_type_list:
        if run_type_aux.description_run_type == run_type_to_insert.description_run_type:
            flag_run_type = True
            break
    if not flag_run_type:
        run_type_service.insert_run_type(run_type_to_insert)

    run_aux = RunsDto()
    run_aux.date = [datetime_aux.date_time for datetime_aux in dates_service.get_all_dates() if datetime_aux.date_time==date_time]
    run_aux.init_time_collect_data = [datetime_aux.date_time for datetime_aux in dates_service.get_all_dates() if datetime_aux.date_time==date_time]
    if len(run_aux.date) != 0:
        run_aux.date = run_aux.date[0]
        run_aux.init_time_collect_data = run_aux.init_time_collect_data[0]
    run_aux.id_run_type = [runtype.id_run_type for runtype in run_type_service.get_all_run_type() if runtype.description_run_type==object_aux.run_type]
    if len(run_aux.id_run_type) != 0:
        run_aux.id_run_type = run_aux.id_run_type[0]
    run_aux.id_config = [run_config.id_config for run_config in config_service.get_all_config() if run_config.config_description=='LSTCam-003']
    if len(run_aux.id_config) != 0:
        run_aux.id_config = run_aux.id_config[0]
    run_aux.run_number= object_aux.run_num

    runs_list: List[RunsDto] = run_service.get_all_runs()
    flag_run = False
    for run in runs_list:
        if run.date == run_aux.date and run.id_config == run_aux.id_config and run.id_run_type == run_aux.id_run_type:
            flag_run= True
            break
    if not flag_run:
        run_service.insert_runs(run_aux)

print("prueba")
