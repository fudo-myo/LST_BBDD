from typing import List

from utils.test_config import *
from DTO.dl1a_dto import Dl1aDto
from entities.lst_dl1a import LstDl1a
from services.lst_dl1a_service import LstDl1aService
from utils.table_names import LstTableNames
import unittest

from utils.test_utils import TestUtils


class LstDl1aTests(unittest.TestCase):
    get_test_mode()

    def setUp(self):
        TestUtils.print_test_started(self._testMethodName)

    def tearDown(self):
        TestUtils.clear_table_after_test(LstDl1a)
        TestUtils.print_test_finished(self._testMethodName)

    def test_insert_dl1a(self):
        dl1a_service = LstDl1aService()
        dl1a_dto = Dl1aDto()
        dl1a_dto.subrun_number = 1
        dl1a_dto.dl1a_path_file = "TI path insert"
        dl1a_service.insert_dl1a(dl1a_dto)
        self.assertIsNotNone(dl1a_dto.id_dl1a, TestUtils.assert_insert_message(LstTableNames.LST_DL1A))
        TestUtils.print_insert_trace(LstTableNames.LST_DL1A, dl1a_dto.id_dl1a)
        return dl1a_dto.id_dl1a

    def test_update_dl1a(self):
        value = self.test_insert_dl1a()
        dl1a_service = LstDl1aService()
        dl1a_before: Dl1aDto = dl1a_service.get_dl1a_by_id(value)
        dl1a_service.update_dl1a(dl1a_before.id_dl1a, 3, "TU path update")
        dl1a_after: Dl1aDto = dl1a_service.get_dl1a_by_id(value)
        self.assertIsNotNone(dl1a_after.id_dl1a)
        self.assertNotEqual(dl1a_before.subrun_number, dl1a_after.subrun_number,
                            TestUtils.assert_update_message(LstDl1a.subrun_number.name))
        self.assertNotEqual(dl1a_before.dl1a_path_file, dl1a_after.dl1a_path_file,
                            TestUtils.assert_update_message(LstDl1a.dl1a_path_file.name))
        TestUtils.print_update_trace(LstTableNames.LST_DL1A, dl1a_after.id_dl1a)

    def test_delete_dl1a(self):
        value = self.test_insert_dl1a()
        dl1a_service = LstDl1aService()
        dl1a_before: Dl1aDto = dl1a_service.get_dl1a_by_id(value)
        dl1a_service.delete_dl1a(dl1a_before.id_dl1a)
        dl1a_after: Dl1aDto = dl1a_service.get_dl1a_by_id(value)
        self.assertIsNone(dl1a_after.id_dl1a, TestUtils.assert_delete_message(value, LstTableNames.LST_DL1A))
        TestUtils.print_delete_trace(LstTableNames.LST_DL1A, dl1a_before.id_dl1a)

    def test_get_all_dl1a(self):
        for _ in range(5):
            self.test_insert_dl1a()
        dl1a_service = LstDl1aService()
        dl1a_list: List[Dl1aDto] = dl1a_service.get_all_dl1a()
        self.assertGreaterEqual(len(dl1a_list), 5, TestUtils.assert_get_all_message(LstTableNames.LST_DL1A))
        TestUtils.print_get_all_trace(LstTableNames.LST_DL1A, len(dl1a_list))

    def test_get_by_id_dl1a(self):
        value = self.test_insert_dl1a()
        dl1a_service = LstDl1aService()
        dl1a_dto: Dl1aDto = dl1a_service.get_dl1a_by_id(value)
        self.assertIsNotNone(dl1a_dto.id_dl1a, TestUtils.assert_get_by_id_message(LstTableNames.LST_DL1A, value))
        TestUtils.print_get_by_id_trace(LstTableNames.LST_DL1A, dl1a_dto.id_dl1a)
