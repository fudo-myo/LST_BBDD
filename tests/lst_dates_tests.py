from datetime import datetime

from sqlalchemy import DateTime

from DTO.dates_dto import DatesDto
from entities.lst_dates import LstDates
from services.lst_dates_service import LstDatesService
from utils.table_names import LstTableNames
from utils.test_config import *
import unittest

from utils.test_utils import TestUtils


class LstDatesTests(unittest.TestCase):
    get_test_mode()

    def setUp(self):
        TestUtils.print_test_started(self._testMethodName)

    def tearDown(self):
        # TestUtils.clear_table_after_test(LstDates)
        TestUtils.print_test_finished(self._testMethodName)

    def test_insert_dates(self):
        dates_service = LstDatesService()
        dates_dto = DatesDto()
        now = datetime.now()
        formatted_date_string = now.strftime('%Y-%m-%d %H:%M:%S')
        formatted_date = datetime.strptime(formatted_date_string,'%Y-%m-%d %H:%M:%S')
        dates_dto.date = formatted_date
        dates_service.insert_dates(dates_dto)
        self.assertIsNotNone(dates_dto.id_date, TestUtils.assert_insert_message(LstTableNames.LST_DATES))
        TestUtils.print_insert_trace(LstTableNames.LST_DATES, dates_dto.id_date)