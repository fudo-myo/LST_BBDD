from typing import List

from utils.test_config import *
import unittest

from DTO.pixel_group_dto import PixelGroupDto
from entities.lst_pixel_group import LstPixelGroup
from services.lst_pixel_group_service import LstPixelGroupService
from utils.table_names import LstTableNames
from utils.test_utils import TestUtils


class LstPixelGroupTests(unittest.TestCase):
    get_test_mode()

    def setUp(self):
        TestUtils.print_test_started(self._testMethodName)

    def tearDown(self):
        TestUtils.clear_table_after_test(LstPixelGroup)
        TestUtils.print_test_finished(self._testMethodName)

    def test_insert_pixel_group(self):
        pixel_group_service = LstPixelGroupService()
        pixel_group_dto = PixelGroupDto()
        pixel_group_dto.pixel_group_number = 1
        pixel_group_dto.id_config = 1
        pixel_group_dto.other_data = "TI other data"
        pixel_group_service.insert_pixel_group(pixel_group_dto)
        self.assertIsNotNone(pixel_group_dto.id_pixel_group,
                             TestUtils.assert_insert_message(LstTableNames.LST_PIXEL_GROUP))
        TestUtils.print_insert_trace(LstTableNames.LST_PIXEL_GROUP, pixel_group_dto.id_pixel_group)
        return pixel_group_dto.id_pixel_group

    def test_update_pixel_group(self):
        value = self.test_insert_pixel_group()
        pixel_group_service = LstPixelGroupService()
        group_before: PixelGroupDto = pixel_group_service.get_pixel_group_by_id(value, 1)
        pixel_group_service.update_pixel_group(group_before.id_pixel_group, group_before.pixel_group_number, 24, 42,
                                               "TU other data")
        group_after: PixelGroupDto = pixel_group_service.get_pixel_group_by_id(group_before.id_pixel_group, 24)
        self.assertIsNotNone(group_after.id_pixel_group)
        self.assertIsNotNone(group_after.pixel_group_number)
        self.assertNotEqual(group_before.pixel_group_number, group_after.pixel_group_number,
                            TestUtils.assert_update_message(LstPixelGroup.pixel_group_number.name))
        self.assertNotEqual(group_before.id_config, group_after.id_config,
                            TestUtils.assert_update_message(LstPixelGroup.id_config.name))
        self.assertNotEqual(group_before.other_data, group_after.other_data,
                            TestUtils.assert_update_message(LstPixelGroup.other_data.name))
        TestUtils.print_update_trace(LstTableNames.LST_PIXEL_GROUP,
                                     str(group_before.id_pixel_group) + ", " + str(group_before.pixel_group_number))

    def test_delete_pixel_group(self):
        value = self.test_insert_pixel_group()
        pixel_group_service = LstPixelGroupService()
        group_before: PixelGroupDto = pixel_group_service.get_pixel_group_by_id(value, 1)
        pixel_group_service.delete_pixel_group(group_before.id_pixel_group, group_before.pixel_group_number)
        group_after: PixelGroupDto = pixel_group_service.get_pixel_group_by_id(value, 1)
        self.assertIsNone(group_after.id_pixel_group, TestUtils.assert_delete_message(
            str(group_after.id_pixel_group) + ", " + str(group_after.pixel_group_number),
            LstTableNames.LST_PIXEL_GROUP))
        TestUtils.print_delete_trace(LstTableNames.LST_PIXEL_GROUP,
                                     str(group_before.id_pixel_group) + ", " + str(group_before.pixel_group_number))

    def test_get_all_pixel_group(self):
        for _ in range(5):
            self.test_insert_pixel_group()
        pixel_group_service = LstPixelGroupService()
        pixel_group_list: List[PixelGroupDto] = pixel_group_service.get_all_pixel_group()
        self.assertGreaterEqual(len(pixel_group_list), 5,
                                TestUtils.assert_get_all_message(LstTableNames.LST_PIXEL_GROUP))
        TestUtils.print_get_all_trace(LstTableNames.LST_PIXEL_GROUP, len(pixel_group_list))

    def test_get_by_id_pixel_group(self):
        value = self.test_insert_pixel_group()
        pixel_group_service = LstPixelGroupService()
        pixel_group_dto: PixelGroupDto = pixel_group_service.get_pixel_group_by_id(value, 1)
        self.assertIsNotNone(pixel_group_dto.id_pixel_group,
                             TestUtils.assert_get_by_id_message(LstTableNames.LST_PIXEL_GROUP,
                                                                str(pixel_group_dto.id_pixel_group) + ", " + str(
                                                                    pixel_group_dto.pixel_group_number)))
        TestUtils.print_get_by_id_trace(LstTableNames.LST_PIXEL_GROUP, str(pixel_group_dto.id_pixel_group) + ", " + str(
            pixel_group_dto.pixel_group_number))
