from typing import List

from utils.test_config import *
from DTO.r1_data_check_generic_dto import R1DataCheckGenericDto
from services.lst_r1_data_check_generic_service import LstR1DataCheckGenericService
from utils.table_names import LstTableNames
import unittest

from entities.lst_r1_data_check_generic import LstR1DataCheckGeneric
from utils.test_utils import TestUtils


class LstR1DataCheckGenericTests(unittest.TestCase):
    get_test_mode()

    def setUp(self):
        TestUtils.print_test_started(self._testMethodName)

    def tearDown(self):
        TestUtils.clear_table_after_test(LstR1DataCheckGeneric)
        TestUtils.print_test_finished(self._testMethodName)

    def test_insert_r1_data_check_generic(self):
        r1_data_check_generic_service = LstR1DataCheckGenericService()
        r1_dto = R1DataCheckGenericDto()
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
        r1_data_check_generic_service.insert_r1_data_check_generic(r1_dto)
        self.assertIsNotNone(r1_dto.id_r1_data_check_generic,
                             TestUtils.assert_insert_message(LstTableNames.LST_R1_DATA_CHECK_GENERIC))
        TestUtils.print_insert_trace(LstTableNames.LST_R1_DATA_CHECK_GENERIC, r1_dto.id_r1_data_check_generic)
        return r1_dto.id_r1_data_check_generic

    def test_update_r1_data_check_generic(self):
        value = self.test_insert_r1_data_check_generic()
        r1_data_check_generic_service = LstR1DataCheckGenericService()
        r1_before: R1DataCheckGenericDto = r1_data_check_generic_service.get_r1_data_check_generic_by_id(value)
        self.assertIsNotNone(r1_before.id_r1_data_check_generic)
        r1_data_check_generic_service.update_r1_data_check_generic(r1_before.id_r1_data_check_generic, 2, 2, 2, 2, 2, 2,
                                                                   2, 2, "TU gap update", "TU module update")
        r1_after: R1DataCheckGenericDto = r1_data_check_generic_service.get_r1_data_check_generic_by_id(value)
        self.assertIsNotNone(r1_after.id_r1_data_check_generic)
        self.assertNotEqual(r1_before.init_event, r1_after.init_event,
                            TestUtils.assert_update_message(LstR1DataCheckGeneric.init_event.name))
        self.assertNotEqual(r1_before.end_event, r1_after.end_event,
                            TestUtils.assert_update_message(LstR1DataCheckGeneric.end_event.name))
        self.assertNotEqual(r1_before.init_pixel, r1_after.init_pixel,
                            TestUtils.assert_update_message(LstR1DataCheckGeneric.init_pixel.name))
        self.assertNotEqual(r1_before.end_pixel, r1_after.end_pixel,
                            TestUtils.assert_update_message(LstR1DataCheckGeneric.end_pixel.name))
        self.assertNotEqual(r1_before.init_sample, r1_after.init_sample,
                            TestUtils.assert_update_message(LstR1DataCheckGeneric.init_sample.name))
        self.assertNotEqual(r1_before.end_sample, r1_after.end_sample,
                            TestUtils.assert_update_message(LstR1DataCheckGeneric.end_sample.name))
        self.assertNotEqual(r1_before.init_subrun, r1_after.init_subrun,
                            TestUtils.assert_update_message(LstR1DataCheckGeneric.init_subrun.name))
        self.assertNotEqual(r1_before.end_subrun, r1_after.end_subrun,
                            TestUtils.assert_update_message(LstR1DataCheckGeneric.end_subrun.name))
        self.assertNotEqual(r1_before.type_of_gap_calc, r1_after.type_of_gap_calc,
                            TestUtils.assert_update_message(LstR1DataCheckGeneric.type_of_gap_calc.name))
        self.assertNotEqual(r1_before.list_of_module_in_detail, r1_after.list_of_module_in_detail,
                            TestUtils.assert_update_message(LstR1DataCheckGeneric.list_of_module_in_detail.name))
        TestUtils.print_update_trace(LstTableNames.LST_R1_DATA_CHECK_GENERIC, r1_after.id_r1_data_check_generic)

    def test_delete_r1_data_check_generic(self):
        value = self.test_insert_r1_data_check_generic()
        r1_data_check_generic_service = LstR1DataCheckGenericService()
        r1_before: R1DataCheckGenericDto = r1_data_check_generic_service.get_r1_data_check_generic_by_id(value)
        self.assertIsNotNone(r1_before.id_r1_data_check_generic)
        r1_data_check_generic_service.delete_r1_data_check_generic(r1_before.id_r1_data_check_generic)
        r1_after: R1DataCheckGenericDto = r1_data_check_generic_service.get_r1_data_check_generic_by_id(value)
        self.assertIsNone(r1_after.id_r1_data_check_generic,
                          TestUtils.assert_delete_message(r1_after.id_r1_data_check_generic,
                                                          LstTableNames.LST_R1_DATA_CHECK_GENERIC))
        TestUtils.print_delete_trace(LstTableNames.LST_R1_DATA_CHECK_GENERIC, r1_before.id_r1_data_check_generic)

    def test_get_all_r1_data_check_generic(self):
        for _ in range(5):
            self.test_insert_r1_data_check_generic()
        r1_data_check_generic_service = LstR1DataCheckGenericService()
        r1_list: List[R1DataCheckGenericDto] = r1_data_check_generic_service.get_all_r1_data_check_generic()
        self.assertGreaterEqual(len(r1_list), 5,
                                TestUtils.assert_get_all_message(LstTableNames.LST_R1_DATA_CHECK_GENERIC))
        TestUtils.print_get_all_trace(LstTableNames.LST_R1_DATA_CHECK_GENERIC, len(r1_list))

    def test_get_by_id_r1_data_check_generic(self):
        value = self.test_insert_r1_data_check_generic()
        r1_data_check_generic_service = LstR1DataCheckGenericService()
        r1_dto: R1DataCheckGenericDto = r1_data_check_generic_service.get_r1_data_check_generic_by_id(value)
        self.assertIsNotNone(r1_dto.id_r1_data_check_generic,
                             TestUtils.assert_get_by_id_message(LstTableNames.LST_R1_DATA_CHECK_GENERIC, value))
        TestUtils.print_get_by_id_trace(LstTableNames.LST_R1_DATA_CHECK_GENERIC, r1_dto.id_r1_data_check_generic)
