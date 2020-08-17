from datetime import datetime, timedelta, date
from typing import List
from utils.test_config import *

from DTO.dates_dto import DatesDto
from DTO.runs_dto import RunsDto
from DTO.subruns_dto import SubrunsDto
from services.lst_dates_service import LstDatesService
from services.lst_runs_service import LstRunsService
from services.lst_subruns_service import LstSubrunsService
from utils.table_names import LstTableNames

from entities.lst_subruns import LstSubruns
import unittest

from utils.test_utils import TestUtils


class LstSubrunsTests(unittest.TestCase):
    get_test_mode()

    def setUp(self):
        TestUtils.print_test_started(self._testMethodName)

    def tearDown(self):
        TestUtils.clear_table_after_test(LstSubruns)
        TestUtils.print_test_finished(self._testMethodName)

    def test_insert_subruns(self):
        dates_service = LstDatesService()
        dates_dto = DatesDto()
        dates_dto.date_dto = date.today()
        dates_service.insert_dates(dates_dto)
        self.assertIsNotNone(dates_dto.id_date, TestUtils.assert_insert_message(LstTableNames.LST_DATES))
        TestUtils.print_insert_trace(LstTableNames.LST_DATES, dates_dto.id_date)

        runs_service = LstRunsService()
        runs_dto = RunsDto()
        runs_dto.run_number = 1
        runs_dto.id_run_type = 1
        runs_dto.id_date = dates_dto.id_date
        runs_dto.id_config = 1
        runs_service.insert_runs(runs_dto)
        self.assertIsNotNone(runs_dto.id_run, TestUtils.assert_insert_message(LstTableNames.LST_RUNS))
        TestUtils.print_insert_trace(LstTableNames.LST_RUNS, runs_dto.id_run)

        subruns_service = LstSubrunsService()
        subruns_dto = SubrunsDto()
        subruns_dto.subrun_number = 1
        subruns_dto.id_run = runs_dto.id_run
        subruns_dto.date = date.today()
        subruns_dto.hour = datetime.now().time()
        subruns_dto.stream = "[0,1,2,3]"
        subruns_dto.events = 1
        subruns_dto.length = 1.5
        subruns_dto.rate = 1.5
        subruns_dto.size = "15MB"
        subruns_dto.event_type = "M= 82% P= 18%"
        subruns_dto.process_state = "R1 Ready"
        subruns_service.insert_subruns(subruns_dto)
        self.assertIsNotNone(subruns_dto.id_subrun, TestUtils.assert_insert_message(LstTableNames.LST_SUBRUNS))
        TestUtils.print_insert_trace(LstTableNames.LST_SUBRUNS, subruns_dto.id_subrun)
        return subruns_dto.id_subrun, subruns_dto.subrun_number, subruns_dto.id_run

    def test_update_subruns(self):
        id_subrun, subrun_number, id_run = self.test_insert_subruns()
        subruns_service = LstSubrunsService()
        subruns_before: SubrunsDto = subruns_service.get_subrun_by_id(id_subrun, subrun_number)
        self.assertIsNotNone(subruns_before.id_subrun)
        self.assertIsNotNone(subruns_before.subrun_number)
        self.assertIsNotNone(subruns_before.id_run)
        id_subrun_after, subrun_number_after, id_run_after = self.test_insert_subruns()
        subruns_service.update_subruns(subruns_before.id_subrun, subruns_before.subrun_number, 2, id_run_after,
                                       date.today() + timedelta(days=10), (datetime.now() + timedelta(hours=5)).time(),
                                       "[3,2,1,0]", 2, 2.5, 2.5, "3GB", "P=100%", "R1 KO")
        subruns_after: SubrunsDto = subruns_service.get_subrun_by_id(id_subrun, 2)
        self.assertIsNotNone(subruns_after.id_subrun)
        self.assertIsNotNone(subruns_after.subrun_number)
        self.assertNotEqual(subruns_before.subrun_number, subruns_after.subrun_number,
                            TestUtils.assert_update_message(LstSubruns.subrun_number.name))
        self.assertNotEqual(subruns_before.id_run, subruns_after.id_run,
                            TestUtils.assert_update_message(LstSubruns.id_run.name))
        self.assertNotEqual(subruns_before.date, subruns_after.date,
                            TestUtils.assert_update_message(LstSubruns.date.name))
        self.assertNotEqual(subruns_before.hour, subruns_after.hour,
                            TestUtils.assert_update_message(LstSubruns.hour.name))
        self.assertNotEqual(subruns_before.stream, subruns_after.stream,
                            TestUtils.assert_update_message(LstSubruns.stream.name))
        self.assertNotEqual(subruns_before.events, subruns_after.events,
                            TestUtils.assert_update_message(LstSubruns.events.name))
        self.assertNotEqual(subruns_before.length, subruns_after.length,
                            TestUtils.assert_update_message(LstSubruns.length.name))
        self.assertNotEqual(subruns_before.rate, subruns_after.rate,
                            TestUtils.assert_update_message(LstSubruns.rate.name))
        self.assertNotEqual(subruns_before.size, subruns_after.size,
                            TestUtils.assert_update_message(LstSubruns.size.name))
        self.assertNotEqual(subruns_before.event_type, subruns_after.event_type,
                            TestUtils.assert_update_message(LstSubruns.event_type.name))
        self.assertNotEqual(subruns_before.process_state, subruns_after.process_state,
                            TestUtils.assert_update_message(LstSubruns.process_state.name))
        TestUtils.print_update_trace(LstTableNames.LST_SUBRUNS,
                                     str(subruns_before.id_subrun) + ", " + str(subruns_before.subrun_number))

    def test_delete_subruns(self):
        id_subrun, subrun_number, id_run = self.test_insert_subruns()
        subruns_service = LstSubrunsService()
        subruns_before: SubrunsDto = subruns_service.get_subrun_by_id(id_subrun, subrun_number)
        self.assertIsNotNone(subruns_before.id_subrun)
        self.assertIsNotNone(subruns_before.subrun_number)
        subruns_service.delete_subruns(subruns_before.id_subrun, subruns_before.subrun_number)
        subruns_after: SubrunsDto = subruns_service.get_subrun_by_id(id_subrun, subrun_number)
        self.assertIsNone(subruns_after.id_subrun)
        self.assertIsNone(subruns_after.subrun_number, TestUtils.assert_delete_message(
            str(subruns_after.id_subrun) + ", " + str(subruns_after.subrun_number), LstTableNames.LST_SUBRUNS))
        TestUtils.print_delete_trace(LstTableNames.LST_SUBRUNS,
                                     str(subruns_before.id_subrun) + ", " + str(subruns_before.subrun_number))

    def test_get_all_subruns(self):
        for _ in range(5):
            self.test_insert_subruns()
        subruns_service = LstSubrunsService()
        subruns_list: List[SubrunsDto] = subruns_service.get_all_subruns()
        self.assertGreaterEqual(len(subruns_list), 5, TestUtils.assert_get_all_message(LstTableNames.LST_SUBRUNS))
        TestUtils.print_get_all_trace(LstTableNames.LST_SUBRUNS, len(subruns_list))

    def test_get_by_id_subruns(self):
        id_subrun, subrun_number, id_run = self.test_insert_subruns()
        subruns_service = LstSubrunsService()
        subruns_dto: SubrunsDto = subruns_service.get_subrun_by_id(id_subrun, subrun_number)
        self.assertIsNotNone(subruns_dto.id_subrun)
        self.assertIsNotNone(subruns_dto.subrun_number, TestUtils.assert_get_by_id_message(LstTableNames.LST_SUBRUNS,
                                                                                           str(id_subrun)))
        TestUtils.print_get_by_id_trace(LstTableNames.LST_SUBRUNS,
                                        str(subruns_dto.id_subrun) + ", " + str(subruns_dto.subrun_number))

    def test_get_by_id_run(self):
        id_subrun, subrun_number, id_run = self.test_insert_subruns()
        subruns_service = LstSubrunsService()
        subruns_dto: SubrunsDto = subruns_service.get_subrun_by_idrun(id_run)
        self.assertIsNotNone(subruns_dto.id_subrun)
        self.assertIsNotNone(subruns_dto.subrun_number, TestUtils.assert_get_by_id_message(LstTableNames.LST_SUBRUNS,
                                                                                           str(id_subrun)))
        TestUtils.print_get_by_id_trace(LstTableNames.LST_SUBRUNS,
                                        str(subruns_dto.id_subrun) + ", " + str(subruns_dto.subrun_number))
