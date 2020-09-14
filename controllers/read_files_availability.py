import os

from DTO.sources_dto import SourcesDto
from DTO.subruns_dto import SubrunsDto
from services.lst_runs_service import LstRunsService
from services.lst_subruns_service import LstSubrunsService
from utils.cleaner_files import CleanerFiles

dir = 'C:\\Users\\fjromero\\Documents\\cta\\BBDD_ISIDRO\\data_availability'
files_list = CleanerFiles.get_data_availability_files_current_year(os.listdir(dir), year_to_compare=2020)

run_service = LstRunsService()
subrun_service = LstSubrunsService()
list_runs_not_found = []

for i in files_list:
    file = open(dir + f"\\{i}", "r")
    print(dir + f"\\{i}")
    lines = file.readlines()
    for j in lines:
        # THIS REMOVE FINAL BREAK LINE
        j = j.rstrip()
        # REMOVE \t FROM THE LINE
        j = CleanerFiles.remove_tab(j)
        split_string = j.split(" ")
        clean_list = []
        for k in split_string:
            if k != "":
                clean_list.append(k)
        CleanerFiles.nan_to_none(clean_list)
        subrun_dto = SubrunsDto()
        run_name = CleanerFiles.check_run_number(clean_list[0])
        subrun_dto.id_run = run_service.get_run_by_runnumber(run_name).id_run
        subrun_dto.subrun_number = CleanerFiles.convert_string_to_number(clean_list[1], "int")
        subrun_dto.waveform_filter = clean_list[2]
        subrun_dto.waveform_data = clean_list[3]
        subrun_dto.counter_filter = clean_list[4]
        subrun_dto.counter_data = clean_list[5]
        if subrun_dto.id_run is None:
            list_runs_not_found.append({run_name: f"\\{i}"})
            continue
        subrun_exist = subrun_service.get_subrun_by_idrun_and_subrun(subrun_dto.id_run,
                                                                     subrun_dto.subrun_number)
        if subrun_exist is not None and subrun_exist.id_subrun is not None:
            subrun_service.update_subruns(id_subrun=subrun_exist.id_subrun, subrun_number_to_search=subrun_exist.subrun_number, subrun_number_to_update=subrun_exist.subrun_number,
                                          id_run=subrun_exist.id_run, waveform_filter=subrun_exist.waveform_filter, waveform_data=subrun_exist.waveform_data,
                                          counter_filter=subrun_exist.counter_filter, counter_data=subrun_exist.counter_data)
        else:
            subrun_service.insert_subruns(subrun_dto)

with open('list_runs_not_found_by_data_availability.txt', 'w') as f:
    for i in list_runs_not_found:
        for key, value in i.items():
            f.write("%s\n" % "Run"+str(key)+" "+value)
            print(f"Run {key} of file {value} not found in database")