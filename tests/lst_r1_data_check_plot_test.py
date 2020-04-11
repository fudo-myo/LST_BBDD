from typing import List

from utils.test_config import *
from DTO.r1_data_check_plot_dto import R1DataCheckPlotDto
from services.lst_r1_data_check_plot_service import LstR1DataCheckPlotService
from utils.table_names import LstTableNames
import unittest

from entities.lst_r1_data_check_plot import LstR1DataCheckPlot
from utils.test_utils import TestUtils


class LstR1DataCheckPlotTests(unittest.TestCase):
    get_test_mode()

    def setUp(self):
        TestUtils.print_test_started(self._testMethodName)

    def tearDown(self):
        TestUtils.clear_table_after_test(LstR1DataCheckPlot)
        TestUtils.print_test_finished(self._testMethodName)

    def test_insert_r1_data_check_plot(self):
        r1_data_check_plot_service = LstR1DataCheckPlotService()
        r1_dto = R1DataCheckPlotDto()
        r1_dto.id_lst_r1_data_check_plot = 1
        r1_dto.id_r1_data_check = 1
        r1_dto.lst_r1_data_check_plot_path = "TI path insert"
        r1_dto.lst_r1_data_check_plot_description = "TI desc insert"
        r1_data_check_plot_service.insert_r1_data_check_plot(r1_dto)
        self.assertIsNotNone(r1_dto.id_record, TestUtils.assert_insert_message(LstTableNames.LST_R1_DATA_CHECK_PLOT))
        TestUtils.print_insert_trace(LstTableNames.LST_R1_DATA_CHECK_PLOT,
                                     str(r1_dto.id_record) + ", " + str(r1_dto.id_lst_r1_data_check_plot))
        return r1_dto.id_record, r1_dto.id_lst_r1_data_check_plot

    def test_update_r1_data_check_plot(self):
        id_record, id_lst_r1_data_check_plot = self.test_insert_r1_data_check_plot()
        r1_data_check_plot_service = LstR1DataCheckPlotService()
        r1_before: R1DataCheckPlotDto = r1_data_check_plot_service.get_r1_data_check_plot_by_id(id_record,
                                                                                                id_lst_r1_data_check_plot)
        self.assertIsNotNone(r1_before.id_record)
        self.assertIsNotNone(r1_before.id_lst_r1_data_check_plot)
        r1_data_check_plot_service.update_r1_data_check_plot(id_record, id_lst_r1_data_check_plot, 2, 2,
                                                             "TU path update", "TU desc update")
        r1_after: R1DataCheckPlotDto = r1_data_check_plot_service.get_r1_data_check_plot_by_id(id_record,
                                                                                               2)
        self.assertIsNotNone(r1_after.id_record)
        self.assertIsNotNone(r1_after.id_lst_r1_data_check_plot)
        self.assertNotEqual(r1_before.id_lst_r1_data_check_plot, r1_after.id_lst_r1_data_check_plot,
                            TestUtils.assert_update_message(LstR1DataCheckPlot.id_lst_r1_data_check_plot.name))
        self.assertNotEqual(r1_before.id_r1_data_check, r1_after.id_r1_data_check,
                            TestUtils.assert_update_message(LstR1DataCheckPlot.id_r1_data_check.name))
        self.assertNotEqual(r1_before.lst_r1_data_check_plot_path, r1_after.lst_r1_data_check_plot_path,
                            TestUtils.assert_update_message(LstR1DataCheckPlot.lst_r1_data_check_plot_path.name))
        self.assertNotEqual(r1_before.lst_r1_data_check_plot_description, r1_after.lst_r1_data_check_plot_description,
                            TestUtils.assert_update_message(LstR1DataCheckPlot.lst_r1_data_check_plot_description.name))
        TestUtils.print_update_trace(LstTableNames.LST_R1_DATA_CHECK_PLOT,
                                     str(r1_before.id_record) + ", " + str(r1_before.id_lst_r1_data_check_plot))

    def test_delete_r1_data_check_plot(self):
        id_record, id_lst_r1_data_check_plot = self.test_insert_r1_data_check_plot()
        r1_data_check_plot_service = LstR1DataCheckPlotService()
        r1_before: R1DataCheckPlotDto = r1_data_check_plot_service.get_r1_data_check_plot_by_id(id_record,
                                                                                                id_lst_r1_data_check_plot)
        self.assertIsNotNone(r1_before.id_record)
        self.assertIsNotNone(r1_before.id_lst_r1_data_check_plot)
        r1_data_check_plot_service.delete_r1_data_check_plot(id_record, id_lst_r1_data_check_plot)
        r1_after: R1DataCheckPlotDto = r1_data_check_plot_service.get_r1_data_check_plot_by_id(id_record,
                                                                                               id_lst_r1_data_check_plot)
        self.assertIsNone(r1_after.id_lst_r1_data_check_plot)
        self.assertIsNone(r1_after.id_record, TestUtils.assert_delete_message(
            str(r1_after.id_record) + ", " + str(r1_after.id_lst_r1_data_check_plot),
            LstTableNames.LST_R1_DATA_CHECK_PLOT))
        TestUtils.print_delete_trace(LstTableNames.LST_R1_DATA_CHECK_PLOT,
                                     str(r1_after.id_record) + ", " + str(r1_after.id_lst_r1_data_check_plot))

    def test_get_all_r1_data_check_plot(self):
        for _ in range(5):
            self.test_insert_r1_data_check_plot()
        r1_data_check_plot_service = LstR1DataCheckPlotService()
        r1_list: List[R1DataCheckPlotDto] = r1_data_check_plot_service.get_all_r1_data_check_plot()
        self.assertGreaterEqual(len(r1_list), 5, TestUtils.assert_get_all_message(LstTableNames.LST_R1_DATA_CHECK_PLOT))
        TestUtils.print_get_all_trace(LstTableNames.LST_R1_DATA_CHECK_PLOT, len(r1_list))

    def test_get_by_id_data_check_plot(self):
        id_record, id_lst_r1_data_check_plot = self.test_insert_r1_data_check_plot()
        r1_data_check_plot_service = LstR1DataCheckPlotService()
        r1_dto: R1DataCheckPlotDto = r1_data_check_plot_service.get_r1_data_check_plot_by_id(id_record,
                                                                                             id_lst_r1_data_check_plot)
        self.assertIsNotNone(r1_dto.id_record)
        self.assertIsNotNone(r1_dto.id_lst_r1_data_check_plot,
                             TestUtils.assert_get_by_id_message(LstTableNames.LST_R1_DATA_CHECK_PLOT,
                                                                str(id_record) + ", " + str(id_lst_r1_data_check_plot)))
        TestUtils.print_get_by_id_trace(LstTableNames.LST_R1_DATA_CHECK_PLOT,
                                        str(r1_dto.id_record) + ", " + str(r1_dto.id_lst_r1_data_check_plot))
