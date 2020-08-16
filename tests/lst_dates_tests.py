from typing import List

from utils.test_config import *
from entities.lst_dates import LstDates
import unittest
from datetime import datetime, timedelta, date

from DTO.dates_dto import DatesDto
from services.lst_dates_service import LstDatesService
from utils.table_names import LstTableNames
from utils.test_utils import TestUtils


class LstDatesTests(unittest.TestCase):
    get_test_mode()

    def setUp(self):
        TestUtils.print_test_started(self._testMethodName)

    def tearDown(self):
        TestUtils.clear_table_after_test(LstDates)
        TestUtils.print_test_finished(self._testMethodName)

    def test_insert_dates(self):
        dates_service = LstDatesService()
        dates_dto = DatesDto()
        dates_dto.date_dto = date.today()
        dates_service.insert_dates(dates_dto)
        self.assertIsNotNone(dates_dto.id_date, TestUtils.assert_insert_message(LstTableNames.LST_DATES))
        TestUtils.print_insert_trace(LstTableNames.LST_DATES, dates_dto.id_date)
        return dates_dto.id_date, dates_dto.date_dto

    def test_update_dates(self):
        id_date, date_aux = self.test_insert_dates()
        dates_service = LstDatesService()
        dates_before: DatesDto = dates_service.get_date_by_id(date_aux, id_date)
        self.assertIsNotNone(dates_before.id_date)
        self.assertIsNotNone(dates_before.date_dto)
        date_update = date.today() + timedelta(days=45)
        dates_service.update_dates(dates_before.id_date, dates_before.date_dto, date_update)
        dates_after: DatesDto = dates_service.get_date_by_id(date_update, id_date)
        self.assertIsNotNone(dates_after.id_date)
        self.assertIsNotNone(dates_after.date_dto)
        self.assertNotEqual(dates_before.date_dto, dates_after.date_dto,
                            TestUtils.assert_update_message(LstDates.date_entity.name))
        TestUtils.print_update_trace(LstTableNames.LST_SUBRUNS,
                                     str(id_date) + ", " + dates_before.date_dto.strftime("%m/%d/%Y"))

    def test_delete_dates(self):
        id_date, date_aux = self.test_insert_dates()
        dates_service = LstDatesService()
        dates_before: DatesDto = dates_service.get_date_by_id(date_aux, id_date)
        self.assertIsNotNone(dates_before.id_date)
        self.assertIsNotNone(dates_before.date_dto)
        dates_service.delete_date(id_date, date_aux)
        dates_after: DatesDto = dates_service.get_date_by_id(date_aux, id_date)
        self.assertIsNone(dates_after.id_date)
        self.assertIsNone(dates_after.date_dto, TestUtils.assert_delete_message(
            str(id_date) + ", " + str(date_aux), LstTableNames.LST_DATES))
        TestUtils.print_delete_trace(LstTableNames.LST_DATES,
                                     str(id_date) + ", " + dates_before.date_dto.strftime("%m/%d/%Y"))

    def test_get_all_dates(self):
        for _ in range(5):
            self.test_insert_dates()
        dates_service = LstDatesService()
        dates_list: List[DatesDto] = dates_service.get_all_dates()
        self.assertGreaterEqual(len(dates_list), 5, TestUtils.assert_get_all_message(LstTableNames.LST_DATES))
        TestUtils.print_get_all_trace(LstTableNames.LST_DATES, len(dates_list))

    def test_get_by_id_dates(self):
        id_date, date_aux = self.test_insert_dates()
        dates_service = LstDatesService()
        dates_dto: DatesDto = dates_service.get_date_by_id(date_aux, id_date)
        self.assertIsNotNone(dates_dto.id_date)
        self.assertIsNotNone(dates_dto.date_dto, TestUtils.assert_get_by_id_message(LstTableNames.LST_DATES, str(
            id_date) + ", " + date_aux.strftime("%m/%d/%Y")))
        TestUtils.print_get_by_id_trace(LstTableNames.LST_DATES, str(
            dates_dto.id_date) + ", " + dates_dto.date_dto.strftime("%m/%d/%Y"))
