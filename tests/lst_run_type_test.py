from typing import List

from utils.test_config import *
from DTO.run_type_dto import RunTypeDto
from services.lst_run_type_service import LstRunTypeService
from utils.table_names import LstTableNames
import unittest

from entities.lst_run_type import LstRunType
from utils.test_utils import TestUtils


class LstRunTypeTests(unittest.TestCase):
    get_test_mode()

    def setUp(self):
        TestUtils.print_test_started(self._testMethodName)

    def tearDown(self):
        TestUtils.clear_table_after_test(LstRunType)
        TestUtils.print_test_finished(self._testMethodName)

    def test_insert_run_type(self):
        run_type_service = LstRunTypeService()
        run_type_dto = RunTypeDto()
        run_type_dto.description_run_type = "TI desc insert"
        run_type_service.insert_run_type(run_type_dto)
        self.assertIsNotNone(run_type_dto.id_run_type, TestUtils.assert_insert_message(LstTableNames.LST_RUN_TYPE))
        TestUtils.print_insert_trace(LstTableNames.LST_RUN_TYPE, run_type_dto.id_run_type)
        return run_type_dto.id_run_type

    def test_update_run_type(self):
        value = self.test_insert_run_type()
        run_type_service = LstRunTypeService()
        run_type_before: RunTypeDto = run_type_service.get_run_type_by_id(value)
        self.assertIsNotNone(run_type_before.id_run_type)
        run_type_service.update_run_type(run_type_before.id_run_type, "TU desc update")
        run_type_after: RunTypeDto = run_type_service.get_run_type_by_id(value)
        self.assertIsNotNone(run_type_after.id_run_type)
        self.assertNotEqual(run_type_before.description_run_type, run_type_after.description_run_type,
                            TestUtils.assert_update_message(LstRunType.description_run_type.name))
        TestUtils.print_update_trace(LstTableNames.LST_RUN_TYPE, run_type_after.id_run_type)

    def test_delete_run_type(self):
        value = self.test_insert_run_type()
        run_type_service = LstRunTypeService()
        run_type_before: RunTypeDto = run_type_service.get_run_type_by_id(value)
        self.assertIsNotNone(run_type_before.id_run_type)
        run_type_service.delete_run_type(run_type_before.id_run_type)
        run_type_after: RunTypeDto = run_type_service.get_run_type_by_id(value)
        self.assertIsNone(run_type_after.id_run_type,
                          TestUtils.assert_delete_message(run_type_after.id_run_type, LstTableNames.LST_RUN_TYPE))
        TestUtils.print_delete_trace(LstTableNames.LST_RUN_TYPE, run_type_before.id_run_type)

    def test_get_all_run_type(self):
        for _ in range(5):
            self.test_insert_run_type()
        run_type_service = LstRunTypeService()
        run_type_list: List[RunTypeDto] = run_type_service.get_all_run_type()
        self.assertGreaterEqual(len(run_type_list), 5, TestUtils.assert_get_all_message(LstTableNames.LST_RUN_TYPE))
        TestUtils.print_get_all_trace(LstTableNames.LST_RUN_TYPE, len(run_type_list))

    def test_get_by_id_run_type(self):
        value = self.test_insert_run_type()
        run_type_service = LstRunTypeService()
        run_type_dto: RunTypeDto = run_type_service.get_run_type_by_id(value)
        self.assertIsNotNone(run_type_dto.id_run_type,
                             TestUtils.assert_get_by_id_message(LstTableNames.LST_RUN_TYPE, value))
        TestUtils.print_get_by_id_trace(LstTableNames.LST_RUN_TYPE, run_type_dto.id_run_type)
