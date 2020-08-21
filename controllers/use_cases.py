from typing import List

from DTO.runs_dto import RunsDto
from services.lst_dates_service import LstDatesService

# dates_service = LstDatesService()
# dates_list = dates_service.get_date_between_dates('2020-01-13','2020-01-15')
from services.lst_runs_service import LstRunsService

runs_service = LstRunsService()
runs_dto_list: List[RunsDto] = runs_service.get_runs_by_date_and_runtype('DATA', '2020-01-13', '2020-01-15')
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




print("prueba")

