from utils.test_config import *
import unittest
from typing import List

from DTO.configuration_dto import ConfigurationDto
from entities.lst_configuration import LstConfiguration
from services.lst_configuraction_service import LstConfigurationService
from utils.table_names import LstTableNames
from utils.test_utils import TestUtils


class LstConfigurationTests(unittest.TestCase):
    get_test_mode()

    def setUp(self):
        TestUtils.print_test_started(self._testMethodName)

    def tearDown(self):
        TestUtils.clear_table_after_test(LstConfiguration)
        TestUtils.print_test_finished(self._testMethodName)

    def test_insert_configuration(self):
        configuration_service = LstConfigurationService()
        config_dto = ConfigurationDto()
        config_dto.config_description = "TI config desc"
        config_dto.param_1 = "TI config P1"
        config_dto.param_2 = "TI config P2"
        config_dto.param_3 = "TI config P3"
        configuration_service.insert_config(config_dto)
        self.assertIsNotNone(config_dto.id_config, TestUtils.assert_insert_message(LstTableNames.LST_CONFIGURATION))
        TestUtils.print_insert_trace(LstTableNames.LST_CONFIGURATION, config_dto.id_config)
        return config_dto.id_config

    def test_update_configuration(self):
        value = self.test_insert_configuration()
        configuration_service = LstConfigurationService()
        config_dto_before: ConfigurationDto = configuration_service.get_config_by_id(value)
        configuration_service.update_config(config_dto_before.id_config, "TU config desc", "TU config P1",
                                            "TU config P2", "TU config P3")
        config_dto_after: ConfigurationDto = configuration_service.get_config_by_id(value)
        self.assertIsNotNone(config_dto_after.id_config)
        self.assertNotEqual(config_dto_before.config_description, config_dto_after.config_description,
                            TestUtils.assert_update_message(LstConfiguration.config_description.name))
        self.assertNotEqual(config_dto_before.param_1, config_dto_after.param_1,
                            TestUtils.assert_update_message(LstConfiguration.param_1.name))
        self.assertNotEqual(config_dto_before.param_2, config_dto_after.param_2,
                            TestUtils.assert_update_message(LstConfiguration.param_2.name))
        self.assertNotEqual(config_dto_before.param_3, config_dto_after.param_3,
                            TestUtils.assert_update_message(LstConfiguration.param_3.name))
        TestUtils.print_update_trace(LstTableNames.LST_CONFIGURATION, config_dto_after.id_config)

    def test_delete_configuration(self):
        value = self.test_insert_configuration()
        configuration_service = LstConfigurationService()
        config_dto_before: ConfigurationDto = configuration_service.get_config_by_id(value)
        configuration_service.delete_by_id(config_dto_before.id_config)
        config_dto_after: ConfigurationDto = configuration_service.get_config_by_id(value)
        self.assertIsNone(config_dto_after.id_config,
                          TestUtils.assert_delete_message(config_dto_after.id_config, LstTableNames.LST_CONFIGURATION))

    def test_get_all_configuration(self):
        for _ in range(5):
            self.test_insert_configuration()
        configuration_service = LstConfigurationService()
        config_list: List[ConfigurationDto] = configuration_service.get_all_config()
        self.assertGreaterEqual(len(config_list), 5, TestUtils.assert_get_all_message(LstTableNames.LST_CONFIGURATION))
        TestUtils.print_get_all_trace(LstTableNames.LST_CONFIGURATION, len(config_list))

    def test_get_by_id_configuration(self):
        value = self.test_insert_configuration()
        configuration_service = LstConfigurationService()
        config_dto: ConfigurationDto = configuration_service.get_config_by_id(value)
        self.assertIsNotNone(config_dto.id_config,
                             TestUtils.assert_get_by_id_message(LstTableNames.LST_CONFIGURATION, value))
        TestUtils.print_get_by_id_trace(LstTableNames.LST_CONFIGURATION, config_dto.id_config)
