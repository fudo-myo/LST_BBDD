from typing import List

from DTO.pixel_information_dto import PixelInformationDto
from services.lst_pixel_information_service import LstPixelInformationService
from utils.table_names import LstTableNames
from utils.test_config import *
import unittest

from entities.lst_pixel_information import LstPixelInformation
from utils.test_utils import TestUtils


class LstPixelInformationTests(unittest.TestCase):
    get_test_mode()

    def setUp(self):
        TestUtils.print_test_started(self._testMethodName)

    def tearDown(self):
        TestUtils.clear_table_after_test(LstPixelInformation)
        TestUtils.print_test_finished(self._testMethodName)

    def test_insert_pixel_information(self):
        pixel_info_service = LstPixelInformationService()
        pixel_info_dto = PixelInformationDto()
        pixel_info_dto.pixel_id = 1
        pixel_info_dto.pixel_group_number = 1
        pixel_info_dto.pixel_pos_x = 2.25
        pixel_info_dto.pixel_pos_y = 3.25
        pixel_info_dto.pixel_pos_z = 4.25
        pixel_info_service.insert_pixel_info(pixel_info_dto)
        self.assertIsNotNone(pixel_info_dto.id_record,
                             TestUtils.assert_insert_message(LstTableNames.LST_PIXEL_INFORMATION))
        TestUtils.print_insert_trace(LstTableNames.LST_PIXEL_INFORMATION, pixel_info_dto.id_record)
        return pixel_info_dto.id_record, pixel_info_dto.pixel_id, pixel_info_dto.pixel_group_number

    def test_update_pixel_information(self):
        id_record, pixel_id, pixel_group_number = self.test_insert_pixel_information()
        pixel_info_service = LstPixelInformationService()
        pixel_dto_before: PixelInformationDto = pixel_info_service.get_pixel_info_by_id(id_record, pixel_id,
                                                                                        pixel_group_number)
        self.assertIsNotNone(pixel_dto_before.id_record)
        self.assertIsNotNone(pixel_dto_before.pixel_id)
        self.assertIsNotNone(pixel_dto_before.pixel_group_number)
        pixel_info_service.update_pixel_info(pixel_dto_before.id_record, pixel_dto_before.pixel_id,
                                             pixel_dto_before.pixel_group_number, 5, 5, 9.99, 8.88, 7.77)
        pixel_dto_after: PixelInformationDto = pixel_info_service.get_pixel_info_by_id(id_record, 5,
                                                                                       5)
        self.assertIsNotNone(pixel_dto_after.id_record)
        self.assertIsNotNone(pixel_dto_after.pixel_id)
        self.assertIsNotNone(pixel_dto_after.pixel_group_number)
        self.assertNotEqual(pixel_dto_before.pixel_id, pixel_dto_after.pixel_id,
                            TestUtils.assert_update_message(LstPixelInformation.pixel_id.name))
        self.assertNotEqual(pixel_dto_before.pixel_group_number, pixel_dto_after.pixel_group_number,
                            TestUtils.assert_update_message(LstPixelInformation.pixel_group_number.name))
        self.assertNotEqual(pixel_dto_before.pixel_pos_x, pixel_dto_after.pixel_pos_x,
                            TestUtils.assert_update_message(LstPixelInformation.pixel_pos_x.name))
        self.assertNotEqual(pixel_dto_before.pixel_pos_y, pixel_dto_after.pixel_pos_y,
                            TestUtils.assert_update_message(LstPixelInformation.pixel_pos_y.name))
        self.assertNotEqual(pixel_dto_before.pixel_pos_z, pixel_dto_after.pixel_pos_z,
                            TestUtils.assert_update_message(LstPixelInformation.pixel_pos_z.name))
        TestUtils.print_update_trace(LstTableNames.LST_PIXEL_INFORMATION,
                                     str(id_record) + ", " + str(pixel_id) + ", " + str(pixel_group_number))

    def test_delete_pixel_information(self):
        id_record, pixel_id, pixel_group_number = self.test_insert_pixel_information()
        pixel_info_service = LstPixelInformationService()
        pixel_dto_before: PixelInformationDto = pixel_info_service.get_pixel_info_by_id(id_record, pixel_id,
                                                                                        pixel_group_number)
        self.assertIsNotNone(pixel_dto_before.id_record)
        self.assertIsNotNone(pixel_dto_before.pixel_id)
        self.assertIsNotNone(pixel_dto_before.pixel_group_number)
        pixel_info_service.delete_pixel_info(id_record, pixel_id, pixel_group_number)
        pixel_dto_after: PixelInformationDto = pixel_info_service.get_pixel_info_by_id(id_record, pixel_id,
                                                                                       pixel_group_number)
        self.assertIsNone(pixel_dto_after.pixel_id)
        self.assertIsNone(pixel_dto_after.pixel_group_number)
        self.assertIsNone(pixel_dto_after.id_record, TestUtils.assert_delete_message(
            str(pixel_dto_after.id_record) + ", " + str(pixel_dto_after.pixel_id) + ", " + str(
                pixel_dto_after.pixel_group_number),
            LstTableNames.LST_PIXEL_INFORMATION))
        TestUtils.print_delete_trace(LstTableNames.LST_PIXEL_INFORMATION,
                                     str(pixel_dto_before.id_record) + ", " + str(
                                         pixel_dto_before.pixel_id) + ", " + str(
                                         pixel_dto_before.pixel_group_number))

    def test_get_all_pixel_information(self):
        for _ in range(5):
            self.test_insert_pixel_information()
        pixel_info_service = LstPixelInformationService()
        pixel_info_list: List[PixelInformationDto] = pixel_info_service.get_all_pixel_info()
        self.assertGreaterEqual(len(pixel_info_list), 5,
                                TestUtils.assert_get_all_message(LstTableNames.LST_PIXEL_INFORMATION))
        TestUtils.print_get_all_trace(LstTableNames.LST_PIXEL_INFORMATION, len(pixel_info_list))

    def test_get_by_id_pixel_information(self):
        id_record, pixel_id, pixel_group_number = self.test_insert_pixel_information()
        pixel_info_service = LstPixelInformationService()
        pixel_dto: PixelInformationDto = pixel_info_service.get_pixel_info_by_id(id_record, pixel_id,
                                                                                 pixel_group_number)
        self.assertIsNotNone(pixel_dto.id_record,
                             TestUtils.assert_get_by_id_message(LstTableNames.LST_PIXEL_INFORMATION,
                                                                str(id_record) + ", " + str(pixel_id) + ", " + str(
                                                                    pixel_group_number)))
        TestUtils.print_get_by_id_trace(LstTableNames.LST_PIXEL_INFORMATION,
                                        str(pixel_dto.id_record) + ", " + str(pixel_dto.pixel_id) + ", " + str(
                                            pixel_dto.pixel_group_number))
