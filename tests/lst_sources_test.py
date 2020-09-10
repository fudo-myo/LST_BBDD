import unittest
from typing import List

from utils.test_config import *

from DTO.sources_dto import SourcesDto
from services.lst_sources_service import LstSourcesService
from utils.table_names import LstTableNames

from entities.lst_sources import LstSources
from utils.test_utils import TestUtils


class LstSourcesTest(unittest.TestCase):
    get_test_mode()

    def setUp(self):
        TestUtils.print_test_started(self._testMethodName)

    def tearDown(self):
        TestUtils.clear_table_after_test(LstSources)
        TestUtils.print_test_finished(self._testMethodName)

    def test_insert_source(self):
        source_service = LstSourcesService()
        source_dto = SourcesDto()
        source_dto.source_des = "Altair"
        source_dto.right_asc = 1.11
        source_dto.declination = 1.11
        source_dto.altitude = 1.11
        source_dto.azimuth = 1.11
        source_dto.right_asc_off_set = 1.11
        source_dto.declination_off_set = 1.11
        source_dto.altitude_off_set = 1.11
        source_dto.azimuth_off_set = 1.11

        source_service.insert_sources(source_dto)
        self.assertIsNotNone(source_dto.id_source, TestUtils.assert_insert_message(LstTableNames.LST_SOURCES))
        TestUtils.print_insert_trace(LstTableNames.LST_SOURCES, source_dto.id_source)
        return source_dto.id_source

    def test_update_source(self):
        id_source = self.test_insert_source()
        source_service = LstSourcesService()
        source_before: SourcesDto = source_service.get_source_by_id_and_desc(id_source)
        self.assertIsNotNone(source_before.id_source)
        self.assertIsNotNone(source_before.source_des)
        source_service.update_sources(source_before.source_des, source_before.id_source, source_des_update="Deneb",
                                      right_asc=2.22,
                                      declination=2.22, altitude=2.22,
                                      azimuth=2.22, right_asc_off_set=2.22, declination_off_set=2.22,
                                      altitude_off_set=2.22,
                                      azimuth_off_set=2.22)
        source_after: SourcesDto = source_service.get_source_by_id_and_desc(id_source)
        self.assertIsNotNone(source_after.id_source)
        self.assertIsNotNone(source_after.source_des)
        self.assertNotEqual(source_before.source_des, source_after.source_des,
                            TestUtils.assert_update_message(LstSources.source_des.name))
        self.assertNotEqual(source_before.right_asc, source_after.right_asc,
                            TestUtils.assert_update_message(LstSources.right_asc.name))
        self.assertNotEqual(source_before.declination, source_after.declination,
                            TestUtils.assert_update_message(LstSources.declination.name))
        self.assertNotEqual(source_before.altitude, source_after.altitude,
                            TestUtils.assert_update_message(LstSources.altitude.name))
        self.assertNotEqual(source_before.azimuth, source_after.azimuth,
                            TestUtils.assert_update_message(LstSources.azimuth.name))
        self.assertNotEqual(source_before.right_asc_off_set, source_after.right_asc_off_set,
                            TestUtils.assert_update_message(LstSources.right_asc_off_set.name))
        self.assertNotEqual(source_before.declination_off_set, source_after.declination_off_set,
                            TestUtils.assert_update_message(LstSources.declination_off_set.name))
        self.assertNotEqual(source_before.altitude_off_set, source_after.altitude_off_set,
                            TestUtils.assert_update_message(LstSources.altitude_off_set.name))
        self.assertNotEqual(source_before.azimuth_off_set, source_after.azimuth_off_set,
                            TestUtils.assert_update_message(LstSources.azimuth_off_set.name))

        TestUtils.print_update_trace(LstTableNames.LST_SOURCES, str(source_before.id_source))

    def test_delete_source(self):
        id_source = self.test_insert_source()
        source_service = LstSourcesService()
        source_before: SourcesDto = source_service.get_source_by_id_and_desc(id_source)
        self.assertIsNotNone(source_before.id_source)
        self.assertIsNotNone(source_before.source_des)
        source_service.delete_source(source_before.id_source)
        source_after: SourcesDto = source_service.get_source_by_id_and_desc(id_source)
        self.assertIsNone(source_after.id_source)
        self.assertIsNone(source_after.source_des)
        TestUtils.print_delete_trace(LstTableNames.LST_SOURCES, str(source_before.id_source))

    def test_get_all_sources(self):
        for _ in range(5):
            self.test_insert_source()
        source_service = LstSourcesService()
        source_list: List[SourcesDto] = source_service.get_all_sources()
        self.assertGreaterEqual(len(source_list), 5, TestUtils.assert_get_all_message(LstTableNames.LST_SOURCES))
        TestUtils.print_get_all_trace(LstTableNames.LST_SOURCES, len(source_list))

    def test_get_by_id_source(self):
        id_source = self.test_insert_source()
        source_service = LstSourcesService()
        source_dto: SourcesDto = source_service.get_source_by_id_and_desc(id_source)
        self.assertIsNotNone(source_dto.id_source)
        self.assertIsNotNone(source_dto.source_des)
        TestUtils.print_get_by_id_trace(LstTableNames.LST_SOURCES, str(source_dto.id_source))