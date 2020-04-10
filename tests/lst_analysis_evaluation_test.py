from utils.test_config import *
from entities.lst_analysis_evaluation import LstAnalysisEvaluation
from utils.test_utils import TestUtils

import unittest
from typing import List

from DTO.analysis_evaluation_dto import AnalysisEvaluationDto
from services.lst_analysis_evaluation_service import LstAnalysisEvaluationService
from utils.table_names import LstTableNames


class LstAnalysisEvaluationTests(unittest.TestCase):
    get_test_mode()

    def setUp(self):
        TestUtils.print_test_started(self._testMethodName)

    def tearDown(self):
        TestUtils.clear_table_after_test(LstAnalysisEvaluation)
        TestUtils.print_test_finished(self._testMethodName)

    def test_insert_analysis_evaluation(self):
        analysis_service = LstAnalysisEvaluationService()
        analysis_dto = AnalysisEvaluationDto()
        analysis_dto.id_lst_r1_data_check_plot = 1
        analysis_dto.parameter_description = "test desc"
        analysis_dto.parameter_value = 3.25
        analysis_service.insert_analysis_eval(analysis_dto)
        self.assertIsNotNone(analysis_dto.id_analysis_evaluation,
                             TestUtils.assert_insert_message(LstTableNames.LST_ANALYSIS_EVALUATION))
        TestUtils.print_insert_trace(LstTableNames.LST_ANALYSIS_EVALUATION, analysis_dto.id_analysis_evaluation)
        return analysis_dto.id_analysis_evaluation

    def test_update_analysis_evaluation(self):
        value = self.test_insert_analysis_evaluation()
        analysis_service = LstAnalysisEvaluationService()
        analysis_dto_before: AnalysisEvaluationDto = analysis_service.get_analysis_by_id(value)
        analysis_service.update_analysis_eval(analysis_dto_before.id_analysis_evaluation, 33, "update", 8.90)
        analysis_dto_after: AnalysisEvaluationDto = analysis_service.get_analysis_by_id(value)
        self.assertIsNotNone(analysis_dto_after.id_analysis_evaluation)
        self.assertNotEqual(analysis_dto_before.id_lst_r1_data_check_plot, analysis_dto_after.id_lst_r1_data_check_plot,
                            TestUtils.assert_update_message(LstAnalysisEvaluation.id_lst_r1_data_check_plot.name))
        self.assertNotEqual(analysis_dto_before.parameter_description, analysis_dto_after.parameter_description,
                            TestUtils.assert_update_message(LstAnalysisEvaluation.parameter_description.name))
        self.assertNotEqual(analysis_dto_before.parameter_value, analysis_dto_after.parameter_value,
                            TestUtils.assert_update_message(LstAnalysisEvaluation.parameter_value.name))
        TestUtils.print_update_trace(LstTableNames.LST_ANALYSIS_EVALUATION, analysis_dto_after.id_analysis_evaluation)

    def test_delete_analysis_evaluation(self):
        value = self.test_insert_analysis_evaluation()
        analysis_service = LstAnalysisEvaluationService()
        analysis_dto_before: AnalysisEvaluationDto = analysis_service.get_analysis_by_id(value)
        analysis_service.delete_analysis_eval(analysis_dto_before.id_analysis_evaluation)
        analysis_dto_after: AnalysisEvaluationDto = analysis_service.get_analysis_by_id(value)
        self.assertIsNone(analysis_dto_after.id_analysis_evaluation,
                          TestUtils.assert_delete_message(analysis_dto_before.id_analysis_evaluation,
                                                          LstTableNames.LST_ANALYSIS_EVALUATION))
        TestUtils.print_delete_trace(LstTableNames.LST_ANALYSIS_EVALUATION, analysis_dto_before.id_analysis_evaluation)

    def test_get_all_analysis(self):
        for _ in range(5):
            self.test_insert_analysis_evaluation()
        analysis_service = LstAnalysisEvaluationService()
        analysis_list: List[AnalysisEvaluationDto] = analysis_service.get_all_analysis_eval()
        self.assertGreaterEqual(len(analysis_list), 5,
                                TestUtils.assert_get_all_message(LstTableNames.LST_ANALYSIS_EVALUATION))
        TestUtils.print_get_all_trace(LstTableNames.LST_ANALYSIS_EVALUATION, len(analysis_list))

    def test_get_by_id_analysis(self):
        value = self.test_insert_analysis_evaluation()
        analysis_service = LstAnalysisEvaluationService()
        analysis_dto: AnalysisEvaluationDto = analysis_service.get_analysis_by_id(value)
        self.assertIsNotNone(analysis_dto.id_analysis_evaluation,
                             TestUtils.assert_get_by_id_message(LstTableNames.LST_ANALYSIS_EVALUATION,
                                                                value))
        TestUtils.print_get_by_id_trace(LstTableNames.LST_ANALYSIS_EVALUATION, analysis_dto.id_analysis_evaluation)


if __name__ == '__main__':
    unittest.main(verbosity=2)
