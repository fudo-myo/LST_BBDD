import os

from DTO.subruns_dto import SubrunsDto
from services.lst_runs_service import LstRunsService
from services.lst_subruns_service import LstSubrunsService
from utils.cleaner_files import CleanerFiles

dir = 'C:\\Users\\fjromero\\Documents\\cta\\BBDD_ISIDRO\\basic_and_standard'
files_list = CleanerFiles.get_basic_and_standard_files_current_year(os.listdir(dir), "standard", year_to_compare=2020)

run_service = LstRunsService()
subrun_service = LstSubrunsService()

list_object_to_insert = []
list_runs_not_found = []

for i in files_list:
    file = open(dir + f"\\{i}", "r")
    print(dir + f"\\{i}")
    lines = CleanerFiles.clean_header_and_footer(file.readlines())
    for j in lines:
        # THIS REMOVE FINAL BREAK LINE
        j = j.rstrip()
        # REMOVE \t FROM THE LINE
        j = CleanerFiles.remove_tab(j)
        j, stream = CleanerFiles.get_stream_attr(j)
        split_string = j.split(" ")
        clean_list = []
        for k in split_string:
            if k != "":
                clean_list.append(k)
        CleanerFiles.nan_to_none(clean_list)
        subrun_dto = SubrunsDto()
        CleanerFiles.check_list_dimensions(clean_list, 12)
        subrun_dto.date = clean_list[0]
        subrun_dto.hour = clean_list[1]
        run_name = CleanerFiles.check_run_number(clean_list[2])
        subrun_dto.subrun_number = CleanerFiles.convert_string_to_number(clean_list[3], "int")
        subrun_dto.stream = stream
        subrun_dto.events = CleanerFiles.convert_string_to_number(clean_list[4], "int")
        subrun_dto.length = CleanerFiles.convert_string_to_number(clean_list[5], "float")
        subrun_dto.rate = CleanerFiles.convert_string_to_number(clean_list[6], "float")
        subrun_dto.size = clean_list[7]
        subrun_dto.event_type = CleanerFiles.check_event_type_standard_file(clean_list, 8)
        subrun_dto.process_state = CleanerFiles.check_proccess_state_standard_file(clean_list)
        subrun_dto.id_run = run_service.get_run_by_runnumber(run_name).id_run
        if subrun_dto.id_run is None:
            list_runs_not_found.append({run_name: subrun_dto.date + " " + subrun_dto.hour})
            continue
        subrun_exist = subrun_service.get_subrun_by_idrun_and_subrun(subrun_dto.id_run,
                                                                     subrun_dto.subrun_number)
        if subrun_exist is not None and subrun_exist.id_subrun is not None:
            subrun_service.update_subruns(id_subrun=subrun_exist.id_subrun,
                                          subrun_number_to_search=subrun_exist.subrun_number,
                                          subrun_number_to_update=subrun_dto.subrun_number, id_run=subrun_dto.id_run,
                                          date=subrun_dto.date, hour=subrun_dto.hour, stream=subrun_dto.stream,
                                          events=subrun_dto.events, length=subrun_dto.length, rate=subrun_dto.rate,
                                          size=subrun_dto.size, event_type=subrun_dto.event_type,
                                          process_state=subrun_dto.process_state)
        else:
            subrun_service.insert_subruns(subrun_dto)

with open('list_runs_not_found_by_standard.txt', 'w') as f:
    for i in list_runs_not_found:
        for key, value in i.items():
            f.write("%s\n" % "Run" + str(key) + " " + value)
            print(f"Run {key} dated {value} not found")
