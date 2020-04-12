from typing import List

from DTO.subruns_dto import SubrunsDto
from services.lst_subruns_service import LstSubrunsService
from utils.table_names import LstTableNames
from utils.test_config import *
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
        subruns_service = LstSubrunsService()
        subruns_dto = SubrunsDto()
        subruns_dto.subrun_number = 1
        subruns_dto.run_number = 1
        subruns_dto.id_run_type = 1
        subruns_service.insert_subruns(subruns_dto)
        self.assertIsNotNone(subruns_dto.id_subrun, TestUtils.assert_insert_message(LstTableNames.LST_SUBRUNS))
        TestUtils.print_insert_trace(LstTableNames.LST_SUBRUNS, subruns_dto.id_subrun)
        return subruns_dto.id_subrun, subruns_dto.subrun_number

    def test_update_subruns(self):
        id_subrun, subrun_number = self.test_insert_subruns()
        subruns_service = LstSubrunsService()
        subruns_before: SubrunsDto = subruns_service.get_subrun_by_id(id_subrun, subrun_number)
        self.assertIsNotNone(subruns_before.id_subrun)
        self.assertIsNotNone(subruns_before.subrun_number)
        subruns_service.update_subruns(subruns_before.id_subrun, subruns_before.subrun_number, 2, 2, 2)
        subruns_after: SubrunsDto = subruns_service.get_subrun_by_id(id_subrun, 2)
        self.assertIsNotNone(subruns_after.id_subrun)
        self.assertIsNotNone(subruns_after.subrun_number)
        self.assertNotEqual(subruns_before.subrun_number, subruns_after.subrun_number,
                            TestUtils.assert_update_message(LstSubruns.subrun_number.name))
        self.assertNotEqual(subruns_before.run_number, subruns_after.run_number,
                            TestUtils.assert_update_message(LstSubruns.run_number.name))
        self.assertNotEqual(subruns_before.id_run_type, subruns_after.id_run_type,
                            TestUtils.assert_update_message(LstSubruns.id_run_type.name))
        TestUtils.print_update_trace(LstTableNames.LST_SUBRUNS,
                                     str(subruns_before.id_subrun) + ", " + str(subruns_before.subrun_number))

    def test_delete_subruns(self):
        id_subrun, subrun_number = self.test_insert_subruns()
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
        id_subrun, subrun_number = self.test_insert_subruns()
        subruns_service = LstSubrunsService()
        subruns_dto: SubrunsDto = subruns_service.get_subrun_by_id(id_subrun, subrun_number)
        self.assertIsNotNone(subruns_dto.id_subrun)
        self.assertIsNotNone(subruns_dto.subrun_number, TestUtils.assert_get_by_id_message(LstTableNames.LST_SUBRUNS,
                                                                                           str(id_subrun) + ", " + str(
                                                                                               subrun_number)))
        TestUtils.print_get_by_id_trace(LstTableNames.LST_SUBRUNS,
                                        str(subruns_dto.id_subrun) + ", " + str(subruns_dto.subrun_number))
