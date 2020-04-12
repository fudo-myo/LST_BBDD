from typing import List

from utils.test_config import *
from DTO.qp_data_dto import QpDataDto
from entities.lst_qp_data import LstQpData
from services.lst_qp_data_service import LstQpDataService
from utils.table_names import LstTableNames
import unittest

from utils.test_utils import TestUtils


class LstQpDataTests(unittest.TestCase):
    get_test_mode()

    def setUp(self):
        TestUtils.print_test_started(self._testMethodName)

    def tearDown(self):
        TestUtils.clear_table_after_test(LstQpData)
        TestUtils.print_test_finished(self._testMethodName)

    def test_insert_qp_data(self):
        qp_data_service = LstQpDataService()
        qp_data_dto = QpDataDto()
        qp_data_dto.pixel_id = 1
        qp_data_dto.id_dl1a = 1
        qp_data_dto.q_average = 2.25
        qp_data_dto.q_rms = 3.25
        qp_data_dto.time_average = 4.25
        qp_data_dto.time_rms = 5.25
        qp_data_dto.dl1a_check_build = 1
        qp_data_service.insert_qp_data(qp_data_dto)
        self.assertIsNotNone(qp_data_dto.id_qp_data, TestUtils.assert_insert_message(LstTableNames.LST_QP_DATA))
        TestUtils.print_insert_trace(LstTableNames.LST_QP_DATA, qp_data_dto.id_qp_data)
        return qp_data_dto.id_qp_data

    def test_update_qp_data(self):
        value = self.test_insert_qp_data()
        qp_data_service = LstQpDataService()
        qp_data_before: QpDataDto = qp_data_service.get_qp_data_by_id(value)
        self.assertIsNotNone(qp_data_before.id_qp_data)
        qp_data_service.update_qp_data(qp_data_before.id_qp_data, 2, 2, 2.22, 3.33, 4.44, 5.55, 2)
        qp_data_after: QpDataDto = qp_data_service.get_qp_data_by_id(value)
        self.assertIsNotNone(qp_data_after.id_qp_data)
        self.assertNotEqual(qp_data_before.pixel_id, qp_data_after.pixel_id,
                            TestUtils.assert_update_message(LstQpData.pixel_id.name))
        self.assertNotEqual(qp_data_before.id_dl1a, qp_data_after.id_dl1a,
                            TestUtils.assert_update_message(LstQpData.id_dl1a.name))
        self.assertNotEqual(qp_data_before.q_average, qp_data_after.q_average,
                            TestUtils.assert_update_message(LstQpData.q_average.name))
        self.assertNotEqual(qp_data_before.q_rms, qp_data_after.q_rms,
                            TestUtils.assert_update_message(LstQpData.q_rms.name))
        self.assertNotEqual(qp_data_before.time_average, qp_data_after.time_average,
                            TestUtils.assert_update_message(LstQpData.time_average.name))
        self.assertNotEqual(qp_data_before.time_rms, qp_data_after.time_rms,
                            TestUtils.assert_update_message(LstQpData.time_rms.name))
        self.assertNotEqual(qp_data_before.dl1a_check_build, qp_data_after.dl1a_check_build,
                            TestUtils.assert_update_message(LstQpData.dl1a_check_build.name))
        TestUtils.print_update_trace(LstTableNames.LST_QP_DATA, qp_data_after.id_qp_data)

    def test_delete_qp_data(self):
        value = self.test_insert_qp_data()
        qp_data_service = LstQpDataService()
        qp_data_before: QpDataDto = qp_data_service.get_qp_data_by_id(value)
        self.assertIsNotNone(qp_data_before.id_qp_data)
        qp_data_service.delete_qp_data(qp_data_before.id_qp_data)
        qp_data_after: QpDataDto = qp_data_service.get_qp_data_by_id(value)
        self.assertIsNone(qp_data_after.id_qp_data,
                          TestUtils.assert_delete_message(qp_data_after.id_qp_data, LstTableNames.LST_QP_DATA))
        TestUtils.print_delete_trace(LstTableNames.LST_QP_DATA, qp_data_before.id_qp_data)

    def test_get_all_qp_data(self):
        for _ in range(5):
            self.test_insert_qp_data()
        qp_data_service = LstQpDataService()
        qp_data_list: List[QpDataDto] = qp_data_service.get_all_qp_data()
        self.assertGreaterEqual(len(qp_data_list), 5, TestUtils.assert_get_all_message(LstTableNames.LST_QP_DATA))
        TestUtils.print_get_all_trace(LstTableNames.LST_QP_DATA, len(qp_data_list))

    def test_get_by_id_qp_data(self):
        value = self.test_insert_qp_data()
        qp_data_service = LstQpDataService()
        qp_data_dto: QpDataDto = qp_data_service.get_qp_data_by_id(value)
        self.assertIsNotNone(qp_data_dto.id_qp_data,
                             TestUtils.assert_get_by_id_message(LstTableNames.LST_QP_DATA, value))
        TestUtils.print_get_by_id_trace(LstTableNames.LST_QP_DATA, qp_data_dto.id_qp_data)
