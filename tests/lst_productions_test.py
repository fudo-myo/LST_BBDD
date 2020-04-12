from typing import List

from utils.test_config import *
from DTO.productions_dto import ProductionsDto
from services.lst_productions_service import LstProductionsService
from utils.table_names import LstTableNames
import unittest

from entities.lst_productions import LstProductions
from utils.test_utils import TestUtils


class LstProductionsTests(unittest.TestCase):
    get_test_mode()

    def setUp(self):
        TestUtils.print_test_started(self._testMethodName)

    def tearDown(self):
        TestUtils.clear_table_after_test(LstProductions)
        TestUtils.print_test_finished(self._testMethodName)

    def test_insert_productions(self):
        productions_service = LstProductionsService()
        prod_dto = ProductionsDto()
        prod_dto.run_number = 1
        prod_dto.id_run_type = 1
        prod_dto.r1_check_build = 1
        prod_dto.dl1a_check_build = 1
        prod_dto.dl1b_check_build = 1
        prod_dto.dl2_check_build = 1
        prod_dto.number_production = 1
        productions_service.insert_productions(prod_dto)
        self.assertIsNotNone(prod_dto.id_production, TestUtils.assert_insert_message(LstTableNames.LST_PRODUCTIONS))
        TestUtils.print_insert_trace(LstTableNames.LST_PRODUCTIONS, prod_dto.id_production)
        return prod_dto.id_production

    def test_update_productions(self):
        value = self.test_insert_productions()
        productions_service = LstProductionsService()
        prod_before: ProductionsDto = productions_service.get_productions_by_id(value)
        self.assertIsNotNone(prod_before.id_production)
        productions_service.update_productions(prod_before.id_production, 2, 2, 2, 2, 2, 2, 2)
        prod_after: ProductionsDto = productions_service.get_productions_by_id(value)
        self.assertNotEqual(prod_before.run_number, prod_after.run_number,
                            TestUtils.assert_update_message(LstProductions.run_number.name))
        self.assertNotEqual(prod_before.id_run_type, prod_after.id_run_type,
                            TestUtils.assert_update_message(LstProductions.id_run_type.name))
        self.assertNotEqual(prod_before.r1_check_build, prod_after.r1_check_build,
                            TestUtils.assert_update_message(LstProductions.r1_check_build.name))
        self.assertNotEqual(prod_before.dl1a_check_build, prod_after.dl1a_check_build,
                            TestUtils.assert_update_message(LstProductions.dl1a_check_build.name))
        self.assertNotEqual(prod_before.dl1b_check_build, prod_after.dl1b_check_build,
                            TestUtils.assert_update_message(LstProductions.dl1b_check_build.name))
        self.assertNotEqual(prod_before.dl2_check_build, prod_after.dl2_check_build,
                            TestUtils.assert_update_message(LstProductions.dl2_check_build.name))
        self.assertNotEqual(prod_before.number_production, prod_after.number_production,
                            TestUtils.assert_update_message(LstProductions.number_production.name))
        TestUtils.print_update_trace(LstTableNames.LST_PRODUCTIONS, prod_after.id_production)

    def test_delete_productions(self):
        value = self.test_insert_productions()
        productions_service = LstProductionsService()
        prod_before: ProductionsDto = productions_service.get_productions_by_id(value)
        self.assertIsNotNone(prod_before.id_production)
        productions_service.delete_productions(prod_before.id_production)
        prod_after: ProductionsDto = productions_service.get_productions_by_id(value)
        self.assertIsNone(prod_after.id_production,
                          TestUtils.assert_delete_message(prod_after.id_production, LstTableNames.LST_PRODUCTIONS))
        TestUtils.print_delete_trace(LstTableNames.LST_PRODUCTIONS, prod_before.id_production)

    def test_get_all_productions(self):
        for _ in range(5):
            self.test_insert_productions()
        productions_service = LstProductionsService()
        prod_list: List[ProductionsDto] = productions_service.get_all_productions()
        self.assertGreaterEqual(len(prod_list), 5, TestUtils.assert_get_all_message(LstTableNames.LST_PRODUCTIONS))
        TestUtils.print_get_all_trace(LstTableNames.LST_PRODUCTIONS, len(prod_list))

    def test_get_by_id_productions(self):
        value = self.test_insert_productions()
        productions_service = LstProductionsService()
        prod_dto: ProductionsDto = productions_service.get_productions_by_id(value)
        self.assertIsNotNone(prod_dto.id_production,
                             TestUtils.assert_get_by_id_message(LstTableNames.LST_PRODUCTIONS, value))
        TestUtils.print_get_by_id_trace(LstTableNames.LST_PRODUCTIONS, prod_dto.id_production)
