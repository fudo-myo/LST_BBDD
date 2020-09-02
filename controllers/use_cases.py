from typing import List

from DTO.runs_dto import RunsDto
from services.lst_dates_service import LstDatesService

# dates_service = LstDatesService()
# dates_list = dates_service.get_date_between_dates('2020-01-13','2020-01-15')
from services.lst_runs_service import LstRunsService
from utils.cleaner_files import CleanerFiles
import statistics
import matplotlib.pyplot as plt

dates_list = ["20200115", "20200117", "20200118", "20200127", "20200128", "20200201", "20200202", "20200131",
              "20200215", "20200217", "20200218", "20200227", "20200228", "20200610", "20200618", "20200622",
              "20200624", "20200710", "20200711", "20200713", "20200715", "20200719"]
runs_service = LstRunsService()

for i in range(len(dates_list)):
    dates_list[i] = CleanerFiles.add_hyphen_to_date(dates_list[i])
# runs_dto_list: List[RunsDto] = runs_service.get_runs_by_date_and_runtype('DATA', '2020-01-13', '2020-01-15')
runs_dto_list: List[RunsDto] = runs_service.get_runs_by_date_and_runtype('DATA', dates_list)
list_of_dict = []
if len(runs_dto_list) != 0:
    list_id_dates = set([run.id_date for run in runs_dto_list])
    for id_date in list_id_dates:
        run_dict = {}
        list_runs_aux = []
        for run in runs_dto_list:
            if run.id_date == id_date:
                list_runs_aux.append(run)
        run_dict[id_date] = list_runs_aux
        list_of_dict.append(run_dict)

list_mean_value = []
list_std_value = []
list_y = []
list_error_bar = []
for i in list_of_dict:
    for key, value in i.items():
        mean_value_aux = 0
        std_value_aux = 0
        rate_mean_dict = {}
        rate_std_dict = {}
        list_rates = []
        for run_dto_aux in value:
            #mean_value_aux = (mean_value_aux) + (run_dto_aux.rate/len(value))
            list_rates.append(run_dto_aux.rate)
        std_value_aux = statistics.stdev(list_rates)
        mean_value_aux = statistics.mean(list_rates)
        rate_mean_dict[key] = mean_value_aux
        rate_std_dict[key] =  std_value_aux
        list_mean_value.append(rate_mean_dict)
        list_std_value.append(rate_std_dict)
        list_y.append(mean_value_aux)
        list_error_bar.append(std_value_aux)

list_x = list(range(0, len(dates_list)-1))
plt.figure(figsize=(15,8))
plt.scatter(list_x, list_y)
plt.title("Event Rate Evolution 2020", fontsize=18)
plt.xlabel("Date", fontsize=15)
plt.ylabel("Rate (kHz)",fontsize=15)
plt.xticks(list_x, dates_list, rotation=45)
# for i in range(len(list_error_bar)):
#     plt.axvline(x=list_x[i], ymax=list_error_bar[i], color='b')
plt.show()


print("prueba")
