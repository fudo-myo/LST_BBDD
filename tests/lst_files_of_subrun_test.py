from typing import List

from utils.test_config import *
import unittest

from DTO.files_of_subrun_dto import FilesOfSubrunDto
from entities.lst_files_of_subrun import LstFilesOfSubrun
from services.lst_files_of_subrun_service import LstFilesOfSubrunService
from utils.table_names import LstTableNames
from utils.test_utils import TestUtils


class LstFilesOfSubrunTests(unittest.TestCase):
    get_test_mode()

    def setUp(self):
        TestUtils.print_test_started(self._testMethodName)

    def tearDown(self):
        TestUtils.clear_table_after_test(LstFilesOfSubrun)
        TestUtils.print_test_finished(self._testMethodName)

    def test_insert_files_of_subrun(self):
        files_service = LstFilesOfSubrunService()
        files_dto = FilesOfSubrunDto()
        files_dto.subrun_number = 1
        files_dto.path_file = "TI path insert"
        files_dto.num_events = 50
        files_dto.array_num_files = "TI array numfiles"
        files_service.insert_files_of_subrun(files_dto)
        self.assertIsNotNone(files_dto.id_file_subrun,
                             TestUtils.assert_insert_message(LstTableNames.LST_FILES_OF_SUBRUN))
        TestUtils.print_insert_trace(LstTableNames.LST_FILES_OF_SUBRUN, files_dto.id_file_subrun)
        return files_dto.id_file_subrun

    def test_update_files_of_subrun(self):
        value = self.test_insert_files_of_subrun()
        files_service = LstFilesOfSubrunService()
        files_before: FilesOfSubrunDto = files_service.get_file_subrun_by_id(value)
        self.assertIsNotNone(files_before.id_file_subrun)
        files_service.update_files_of_subrun(files_before.id_file_subrun, 4, "TU path update", 80, "TU array numfiles")
        files_after: FilesOfSubrunDto = files_service.get_file_subrun_by_id(value)
        self.assertIsNotNone(files_after.id_file_subrun)
        self.assertNotEqual(files_before.subrun_number, files_after.subrun_number,
                            TestUtils.assert_update_message(LstFilesOfSubrun.subrun_number.name))
        self.assertNotEqual(files_before.path_file, files_after.path_file,
                            TestUtils.assert_update_message(LstFilesOfSubrun.path_file.name))
        self.assertNotEqual(files_before.num_events, files_after.num_events,
                            TestUtils.assert_update_message(LstFilesOfSubrun.num_events.name))
        self.assertNotEqual(files_before.array_num_files, files_after.array_num_files,
                            TestUtils.assert_update_message(LstFilesOfSubrun.array_num_files.name))
        TestUtils.print_update_trace(LstTableNames.LST_FILES_OF_SUBRUN, files_after.id_file_subrun)

    def test_delete_files_of_subrun(self):
        value = self.test_insert_files_of_subrun()
        files_service = LstFilesOfSubrunService()
        files_before: FilesOfSubrunDto = files_service.get_file_subrun_by_id(value)
        self.assertIsNotNone(files_before.id_file_subrun)
        files_service.delete_files_of_subrun(files_before.id_file_subrun)
        files_after: FilesOfSubrunDto = files_service.get_file_subrun_by_id(value)
        self.assertIsNone(files_after.id_file_subrun,
                          TestUtils.assert_delete_message(files_after.id_file_subrun,
                                                          LstTableNames.LST_FILES_OF_SUBRUN))
        TestUtils.print_delete_trace(LstTableNames.LST_FILES_OF_SUBRUN, files_before.id_file_subrun)

    def test_get_all_files_of_subrun(self):
        for _ in range(5):
            self.test_insert_files_of_subrun()
        files_service = LstFilesOfSubrunService()
        files_list: List[FilesOfSubrunDto] = files_service.get_all_files_of_subrun()
        self.assertGreaterEqual(len(files_list), 5, TestUtils.assert_get_all_message(LstTableNames.LST_FILES_OF_SUBRUN))
        TestUtils.print_get_all_trace(LstTableNames.LST_FILES_OF_SUBRUN, len(files_list))

    def test_get_by_id_files_of_subrun(self):
        value = self.test_insert_files_of_subrun()
        files_service = LstFilesOfSubrunService()
        files_dto: FilesOfSubrunDto = files_service.get_file_subrun_by_id(value)
        self.assertIsNotNone(files_dto.id_file_subrun,
                             TestUtils.assert_get_by_id_message(LstTableNames.LST_FILES_OF_SUBRUN, value))
        TestUtils.print_get_by_id_trace(LstTableNames.LST_FILES_OF_SUBRUN, files_dto.id_file_subrun)
