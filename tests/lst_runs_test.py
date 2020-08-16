import time
from typing import List
from utils.test_config import *

from DTO.dates_dto import DatesDto
from services.lst_dates_service import LstDatesService

from datetime import datetime, timedelta, date

from DTO.runs_dto import RunsDto
from services.lst_runs_service import LstRunsService
from utils.table_names import LstTableNames
import unittest

from entities.lst_runs import LstRuns
from utils.test_utils import TestUtils


class LstRunsTests(unittest.TestCase):
    get_test_mode()

    def setUp(self):
        TestUtils.print_test_started(self._testMethodName)

    def tearDown(self):
        TestUtils.clear_table_after_test(LstRuns)
        TestUtils.print_test_finished(self._testMethodName)

    def test_insert_runs(self):
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
        runs_dto.date = date.today()
        runs_dto.hour = datetime.now().time()
        runs_dto.id_config = 1
        runs_dto.number_of_subrun = 1
        runs_dto.events = 1
        runs_dto.length = 1.5
        runs_dto.rate = 1.5
        runs_dto.size = "15MB"
        runs_dto.event_type = "M= 82% P= 18%"
        runs_dto.id_production = 1
        runs_dto.path_file = "TI path insert"
        runs_dto.init_ra = 2.25
        runs_dto.end_ra = 3.25
        runs_dto.init_dec = 4.25
        runs_dto.end_dec = 5.25
        runs_dto.init_altitude = 6.25
        runs_dto.end_altitude = 7.25
        runs_dto.init_azimuth = 8.25
        runs_dto.end_azimuth = 9.25
        runs_dto.init_time_collect_data = datetime.now()
        runs_dto.end_time_collect_data = datetime.now()
        runs_service.insert_runs(runs_dto)
        self.assertIsNotNone(runs_dto.id_run, TestUtils.assert_insert_message(LstTableNames.LST_RUNS))
        TestUtils.print_insert_trace(LstTableNames.LST_RUNS, runs_dto.id_run)
        return runs_dto.id_run, dates_dto.id_date

    def test_update_runs(self):
        value, id_date = self.test_insert_runs()
        runs_service = LstRunsService()
        runs_before: RunsDto = runs_service.get_runs_by_id(value)
        self.assertIsNotNone(runs_before.id_run)
        runs_service.update_runs(runs_before.id_run, 2, 2, id_date, date.today() + timedelta(days=10),
                                 (datetime.now() + timedelta(hours=5)).time(), 2, 2, 2, 2.5, 2.5,
                                 "3GB", "P=100%", 2, "TU path update", 2.22, 3.33, 4.44, 5.55, 6.66, 7.77, 8.88, 9.99,
                                 datetime.now() + timedelta(days=30), datetime.now() + timedelta(days=40))
        runs_after: RunsDto = runs_service.get_runs_by_id(value)
        self.assertIsNotNone(runs_after.id_run)
        self.assertNotEqual(runs_before.run_number, runs_after.run_number,
                            TestUtils.assert_update_message(LstRuns.run_number.name))
        self.assertNotEqual(runs_before.id_run_type, runs_after.id_run_type,
                            TestUtils.assert_update_message(LstRuns.id_run_type.name))
        self.assertNotEqual(runs_before.date, runs_after.date, TestUtils.assert_update_message(LstRuns.date.name))
        self.assertNotEqual(runs_before.id_config, runs_after.id_config,
                            TestUtils.assert_update_message(LstRuns.id_config.name))
        self.assertNotEqual(runs_before.number_of_subrun, runs_after.number_of_subrun,
                            TestUtils.assert_update_message(LstRuns.number_of_subrun.name))
        self.assertNotEqual(runs_before.events, runs_after.events,
                            TestUtils.assert_update_message(LstRuns.events.name))
        self.assertNotEqual(runs_before.length, runs_after.length,
                            TestUtils.assert_update_message(LstRuns.length.name))
        self.assertNotEqual(runs_before.rate, runs_after.rate,
                            TestUtils.assert_update_message(LstRuns.rate.name))
        self.assertNotEqual(runs_before.size, runs_after.size,
                            TestUtils.assert_update_message(LstRuns.size.name))
        self.assertNotEqual(runs_before.event_type, runs_after.event_type,
                            TestUtils.assert_update_message(LstRuns.event_type.name))
        self.assertNotEqual(runs_before.id_production, runs_after.id_production,
                            TestUtils.assert_update_message(LstRuns.id_production.name))
        self.assertNotEqual(runs_before.path_file, runs_after.path_file,
                            TestUtils.assert_update_message(LstRuns.path_file.name))
        self.assertNotEqual(runs_before.init_ra, runs_after.init_ra,
                            TestUtils.assert_update_message(LstRuns.init_ra.name))
        self.assertNotEqual(runs_before.end_ra, runs_after.end_ra, TestUtils.assert_update_message(LstRuns.end_ra.name))
        self.assertNotEqual(runs_before.init_dec, runs_after.init_dec,
                            TestUtils.assert_update_message(LstRuns.init_dec.name))
        self.assertNotEqual(runs_before.end_dec, runs_after.end_dec,
                            TestUtils.assert_update_message(LstRuns.end_dec.name))
        self.assertNotEqual(runs_before.init_altitude, runs_after.init_altitude,
                            TestUtils.assert_update_message(LstRuns.init_altitude.name))
        self.assertNotEqual(runs_before.end_altitude, runs_after.end_altitude,
                            TestUtils.assert_update_message(LstRuns.end_altitude.name))
        self.assertNotEqual(runs_before.init_azimuth, runs_after.init_azimuth,
                            TestUtils.assert_update_message(LstRuns.init_azimuth.name))
        self.assertNotEqual(runs_before.end_azimuth, runs_after.end_azimuth,
                            TestUtils.assert_update_message(LstRuns.end_azimuth.name))
        self.assertNotEqual(runs_before.init_time_collect_data, runs_after.init_time_collect_data,
                            TestUtils.assert_update_message(LstRuns.init_time_collect_data.name))
        self.assertNotEqual(runs_before.end_time_collect_data, runs_after.end_time_collect_data,
                            TestUtils.assert_update_message(LstRuns.end_time_collect_data.name))
        TestUtils.print_update_trace(LstTableNames.LST_RUNS, runs_after.id_run)

    def test_delete_runs(self):
        value, id_date = self.test_insert_runs()
        runs_service = LstRunsService()
        runs_before: RunsDto = runs_service.get_runs_by_id(value)
        self.assertIsNotNone(runs_before.id_run)
        runs_service.delete_runs(runs_before.id_run)
        runs_after: RunsDto = runs_service.get_runs_by_id(value)
        self.assertIsNone(runs_after.id_run, TestUtils.assert_delete_message(runs_after.id_run, LstTableNames.LST_RUNS))
        TestUtils.print_delete_trace(LstTableNames.LST_RUNS, runs_before.id_run)

    def test_get_all_runs(self):
        for _ in range(5):
            self.test_insert_runs()
        runs_service = LstRunsService()
        runs_list: List[RunsDto] = runs_service.get_all_runs()
        self.assertGreaterEqual(len(runs_list), 5, TestUtils.assert_get_all_message(LstTableNames.LST_RUNS))
        TestUtils.print_get_all_trace(LstTableNames.LST_RUNS, len(runs_list))

    def test_get_by_id_runs(self):
        value, id_date = self.test_insert_runs()
        runs_service = LstRunsService()
        runs_dto: RunsDto = runs_service.get_runs_by_id(value)
        self.assertIsNotNone(runs_dto.id_run, TestUtils.assert_get_by_id_message(LstTableNames.LST_RUNS, value))
        TestUtils.print_get_by_id_trace(LstTableNames.LST_RUNS, runs_dto.id_run)
