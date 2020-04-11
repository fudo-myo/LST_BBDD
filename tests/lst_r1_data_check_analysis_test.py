from utils.test_config import *
from typing import List

from DTO.r1_data_check_analysis_dto import R1DataCheckAnalysisDto
from entities.lst_r1_data_check_analysis import LstR1DataCheckAnalysis
from services.lst_r1_data_check_analysis_service import LstR1DataCheckAnalysisService
from utils.table_names import LstTableNames
import unittest

from utils.test_utils import TestUtils


class LstR1DataCheckAnalysisTests(unittest.TestCase):
    get_test_mode()

    def setUp(self):
        TestUtils.print_test_started(self._testMethodName)

    def tearDown(self):
        TestUtils.clear_table_after_test(LstR1DataCheckAnalysis)
        TestUtils.print_test_finished(self._testMethodName)

    def test_insert_r1_data_check_analysis(self):
        r1_data_check_analysis_service = LstR1DataCheckAnalysisService()
        r1_dto = R1DataCheckAnalysisDto()
        r1_dto.id_r1_data_check = 1
        r1_dto.run_number = 1
        r1_dto.id_r1_data_check_specific = 1
        r1_data_check_analysis_service.insert_r1_data_check_analysis(r1_dto)
        self.assertIsNotNone(r1_dto.id_record,
                             TestUtils.assert_insert_message(LstTableNames.LST_R1_DATA_CHECK_ANALYSIS))
        TestUtils.print_insert_trace(LstTableNames.LST_R1_DATA_CHECK_ANALYSIS, r1_dto.id_record)
        return r1_dto.id_record, r1_dto.id_r1_data_check

    def test_update_r1_data_check_analysis(self):
        id_record, id_r1_data_check = self.test_insert_r1_data_check_analysis()
        r1_data_check_analysis_service = LstR1DataCheckAnalysisService()
        r1_before: R1DataCheckAnalysisDto = r1_data_check_analysis_service.get_r1_data_check_analysis_by_id(id_record,
                                                                                                            id_r1_data_check)
        self.assertIsNotNone(r1_before.id_record)
        self.assertIsNotNone(r1_before.id_r1_data_check)
        r1_data_check_analysis_service.update_r1_data_check_analysis(r1_before.id_record, r1_before.id_r1_data_check, 2,
                                                                     2, 2)
        r1_after: R1DataCheckAnalysisDto = r1_data_check_analysis_service.get_r1_data_check_analysis_by_id(id_record,
                                                                                                           2)
        self.assertIsNotNone(r1_after.id_record)
        self.assertIsNotNone(r1_after.id_r1_data_check)
        self.assertNotEqual(r1_before.id_r1_data_check, r1_after.id_r1_data_check,
                            TestUtils.assert_update_message(LstR1DataCheckAnalysis.id_r1_data_check.name))
        self.assertNotEqual(r1_before.run_number, r1_after.run_number,
                            TestUtils.assert_update_message(LstR1DataCheckAnalysis.run_number.name))
        self.assertNotEqual(r1_before.id_r1_data_check_specific, r1_after.id_r1_data_check_specific,
                            TestUtils.assert_update_message(LstR1DataCheckAnalysis.id_r1_data_check_specific.name))
        TestUtils.print_update_trace(LstTableNames.LST_R1_DATA_CHECK_ANALYSIS,
                                     str(r1_after.id_record) + ", " + str(r1_after.id_r1_data_check))

    def test_delete_r1_data_check_analysis(self):
        id_record, id_r1_data_check = self.test_insert_r1_data_check_analysis()
        r1_data_check_analysis_service = LstR1DataCheckAnalysisService()
        r1_before: R1DataCheckAnalysisDto = r1_data_check_analysis_service.get_r1_data_check_analysis_by_id(id_record,
                                                                                                            id_r1_data_check)
        self.assertIsNotNone(r1_before.id_record)
        self.assertIsNotNone(r1_before.id_r1_data_check)
        r1_data_check_analysis_service.delete_r1_data_check_analysis(r1_before.id_record, r1_before.id_r1_data_check)
        r1_after: R1DataCheckAnalysisDto = r1_data_check_analysis_service.get_r1_data_check_analysis_by_id(id_record,
                                                                                                           id_r1_data_check)
        self.assertIsNone(r1_after.id_record)
        self.assertIsNone(r1_after.id_r1_data_check, TestUtils.assert_delete_message(
            str(r1_after.id_record) + ", " + str(r1_after.id_r1_data_check), LstTableNames.LST_R1_DATA_CHECK_ANALYSIS))
        TestUtils.print_delete_trace(LstTableNames.LST_R1_DATA_CHECK_ANALYSIS,
                                     str(r1_before.id_record) + ", " + str(r1_before.id_r1_data_check))

    def test_get_all_r1_data_check_analaysis(self):
        for _ in range(5):
            self.test_insert_r1_data_check_analysis()
        r1_data_check_analysis_service = LstR1DataCheckAnalysisService()
        r1_list: List[R1DataCheckAnalysisDto] = r1_data_check_analysis_service.get_all_r1_data_check_analysis()
        self.assertGreaterEqual(len(r1_list), 5,
                                TestUtils.assert_get_all_message(LstTableNames.LST_R1_DATA_CHECK_ANALYSIS))
        TestUtils.print_get_all_trace(LstTableNames.LST_R1_DATA_CHECK_ANALYSIS, len(r1_list))

    def test_get_by_id_r1_data_check_analysis(self):
        id_record, id_r1_data_check = self.test_insert_r1_data_check_analysis()
        r1_data_check_analysis_service = LstR1DataCheckAnalysisService()
        r1_dto: R1DataCheckAnalysisDto = r1_data_check_analysis_service.get_r1_data_check_analysis_by_id(id_record,
                                                                                                         id_r1_data_check)
        self.assertIsNotNone(r1_dto.id_record)
        self.assertIsNotNone(r1_dto.id_r1_data_check,
                             TestUtils.assert_get_by_id_message(LstTableNames.LST_R1_DATA_CHECK_ANALYSIS,
                                                                str(id_record) + ", " + str(
                                                                    id_r1_data_check)))
        TestUtils.print_get_by_id_trace(LstTableNames.LST_R1_DATA_CHECK_ANALYSIS, str(r1_dto.id_record) + ", " + str(
            r1_dto.id_r1_data_check))
