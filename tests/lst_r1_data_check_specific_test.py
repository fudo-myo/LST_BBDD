from typing import List

from utils.test_config import *
from DTO.r1_data_check_specific_dto import R1DataCheckSpecificDto
from services.lst_r1_data_check_specific_service import LstR1DataCheckSpecificService
from utils.table_names import LstTableNames
import unittest

from entities.lst_r1_data_check_specific import LstR1DataCheckSpecific
from utils.test_utils import TestUtils


class LstR1DataCheckSpecificTests(unittest.TestCase):
    get_test_mode()

    def setUp(self):
        TestUtils.print_test_started(self._testMethodName)

    def tearDown(self):
        TestUtils.clear_table_after_test(LstR1DataCheckSpecific)
        TestUtils.print_test_finished(self._testMethodName)

    def test_insert_r1_data_check_specific(self):
        r1_data_check_specific_service = LstR1DataCheckSpecificService()
        r1_dto = R1DataCheckSpecificDto()
        r1_dto.init_event = 1
        r1_dto.end_event = 1
        r1_dto.init_pixel = 1
        r1_dto.end_pixel = 1
        r1_dto.init_sample = 1
        r1_dto.end_sample = 1
        r1_dto.init_subrun = 1
        r1_dto.end_subrun = 1
        r1_dto.type_of_gap_calc = "TI gap insert"
        r1_dto.list_of_module_in_detail = "TI module insert"
        r1_data_check_specific_service.insert_r1_data_check_specific(r1_dto)
        self.assertIsNotNone(r1_dto.id_r1_data_check_specific,
                             TestUtils.assert_insert_message(LstTableNames.LST_R1_DATA_CHECK_SPECIFIC))
        TestUtils.print_insert_trace(LstTableNames.LST_R1_DATA_CHECK_SPECIFIC, r1_dto.id_r1_data_check_specific)
        return r1_dto.id_r1_data_check_specific

    def test_update_r1_data_check_specific(self):
        value = self.test_insert_r1_data_check_specific()
        r1_data_check_specific_service = LstR1DataCheckSpecificService()
        r1_before: R1DataCheckSpecificDto = r1_data_check_specific_service.get_r1_data_check_specific_by_id(value)
        self.assertIsNotNone(r1_before.id_r1_data_check_specific)
        r1_data_check_specific_service.update_r1_data_check_specific(r1_before.id_r1_data_check_specific, 2, 2, 2, 2, 2,
                                                                     2, 2, 2, "TU gap update", "TU module update")
        r1_after: R1DataCheckSpecificDto = r1_data_check_specific_service.get_r1_data_check_specific_by_id(value)
        self.assertIsNotNone(r1_after.id_r1_data_check_specific)
        self.assertNotEqual(r1_before.init_event, r1_after.init_event,
                            TestUtils.assert_update_message(LstR1DataCheckSpecific.init_event.name))
        self.assertNotEqual(r1_before.end_event, r1_after.end_event,
                            TestUtils.assert_update_message(LstR1DataCheckSpecific.end_event.name))
        self.assertNotEqual(r1_before.init_pixel, r1_after.init_pixel,
                            TestUtils.assert_update_message(LstR1DataCheckSpecific.init_pixel.name))
        self.assertNotEqual(r1_before.end_pixel, r1_after.end_pixel,
                            TestUtils.assert_update_message(LstR1DataCheckSpecific.end_pixel.name))
        self.assertNotEqual(r1_before.init_sample, r1_after.init_sample,
                            TestUtils.assert_update_message(LstR1DataCheckSpecific.init_sample.name))
        self.assertNotEqual(r1_before.end_sample, r1_after.end_sample,
                            TestUtils.assert_update_message(LstR1DataCheckSpecific.end_sample.name))
        self.assertNotEqual(r1_before.init_subrun, r1_after.init_subrun,
                            TestUtils.assert_update_message(LstR1DataCheckSpecific.init_subrun.name))
        self.assertNotEqual(r1_before.end_subrun, r1_after.end_subrun,
                            TestUtils.assert_update_message(LstR1DataCheckSpecific.end_subrun.name))
        self.assertNotEqual(r1_before.type_of_gap_calc, r1_after.type_of_gap_calc,
                            TestUtils.assert_update_message(LstR1DataCheckSpecific.type_of_gap_calc.name))
        self.assertNotEqual(r1_before.list_of_module_in_detail, r1_after.list_of_module_in_detail,
                            TestUtils.assert_update_message(LstR1DataCheckSpecific.list_of_module_in_detail.name))
        TestUtils.print_update_trace(LstTableNames.LST_R1_DATA_CHECK_SPECIFIC, r1_after.id_r1_data_check_specific)

    def test_delete_r1_data_check_specific(self):
        value = self.test_insert_r1_data_check_specific()
        r1_data_check_specific_service = LstR1DataCheckSpecificService()
        r1_before: R1DataCheckSpecificDto = r1_data_check_specific_service.get_r1_data_check_specific_by_id(value)
        self.assertIsNotNone(r1_before.id_r1_data_check_specific)
        r1_data_check_specific_service.delete_r1_data_check_specific(r1_before.id_r1_data_check_specific)
        r1_after: R1DataCheckSpecificDto = r1_data_check_specific_service.get_r1_data_check_specific_by_id(value)
        self.assertIsNone(r1_after.id_r1_data_check_specific,
                          TestUtils.assert_delete_message(r1_after.id_r1_data_check_specific,
                                                          LstTableNames.LST_R1_DATA_CHECK_SPECIFIC))
        TestUtils.print_delete_trace(LstTableNames.LST_R1_DATA_CHECK_SPECIFIC, r1_before.id_r1_data_check_specific)

    def test_get_all_r1_data_check_specific(self):
        for _ in range(5):
            self.test_insert_r1_data_check_specific()
        r1_data_check_specific_service = LstR1DataCheckSpecificService()
        r1_list: List[R1DataCheckSpecificDto] = r1_data_check_specific_service.get_all_r1_data_check_specific()
        self.assertGreaterEqual(len(r1_list), 5,
                                TestUtils.assert_get_all_message(LstTableNames.LST_R1_DATA_CHECK_SPECIFIC))
        TestUtils.print_get_all_trace(LstTableNames.LST_R1_DATA_CHECK_SPECIFIC, len(r1_list))

    def test_get_by_id_data_check_specific(self):
        value = self.test_insert_r1_data_check_specific()
        r1_data_check_specific_service = LstR1DataCheckSpecificService()
        r1_dto: R1DataCheckSpecificDto = r1_data_check_specific_service.get_r1_data_check_specific_by_id(value)
        self.assertIsNotNone(r1_dto.id_r1_data_check_specific,
                             TestUtils.assert_get_by_id_message(LstTableNames.LST_R1_DATA_CHECK_SPECIFIC, value))
        TestUtils.print_get_by_id_trace(LstTableNames.LST_R1_DATA_CHECK_SPECIFIC, r1_dto.id_r1_data_check_specific)
