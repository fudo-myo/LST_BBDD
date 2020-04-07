from typing import List

from sqlalchemy.exc import InvalidRequestError, OperationalError
from sqlalchemy.orm import Session

from DTO.files_of_subrun_dto import FilesOfSubrunDto, create_files_of_subrun
from config.base import getSession
from utils.checkers import Checkers

try:
    from entities.lst_files_of_subrun import LstFilesOfSubrun
except ImportError as error:
    Checkers.print_exception_one_param(error)


class LstFilesOfSubrunService:

    def __init__(self):
        self.__session: Session = getSession()
        self.__all_files_of_subrun = None
        self.__files_by_id = None

    def insert_files_of_subrun(self, files_of_subrun_insert: FilesOfSubrunDto):
        try:
            files_of_subrun_aux = LstFilesOfSubrun(
                subrun_number=files_of_subrun_insert.subrun_number,
                path_file=files_of_subrun_insert.path_file,
                num_events=files_of_subrun_insert.num_events,
                array_num_files=files_of_subrun_insert.array_num_files
            )
            self.__session.add(files_of_subrun_aux)
            self.__session.commit()
            if files_of_subrun_aux.id_file_subrun is not None:
                print("RECORD INSERTED IN TABLE '{}' WITH ID '{}'".format(LstFilesOfSubrun.__tablename__.name,
                                                                          files_of_subrun_aux.id_file_subrun))
            else:
                print(" THE RECORD OF TABLE '{}' HAS NOT BEEN INSERTED".format(LstFilesOfSubrun.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def update_files_of_subrun(self, id_file_subrun, subrun_number=None, path_file=None, num_events=None,
                               array_num_files=None):
        try:
            files_before: FilesOfSubrunDto = self.__files_by_id(id_file_subrun)
            if Checkers.validate_int(id_file_subrun,
                                     LstFilesOfSubrun.id_file_subrun.name) and files_before.id_file_subrun is not None:
                self.__session.query(LstFilesOfSubrun).filter(LstFilesOfSubrun.id_file_subrun.like(id_file_subrun)) \
                    .update({
                    LstFilesOfSubrun.subrun_number: Checkers.check_field_not_null(LstFilesOfSubrun.subrun_number,
                                                                                  subrun_number),
                    LstFilesOfSubrun.path_file: Checkers.check_field_not_null(LstFilesOfSubrun.path_file, path_file),
                    LstFilesOfSubrun.num_events: Checkers.check_field_not_null(LstFilesOfSubrun.num_events, num_events),
                    LstFilesOfSubrun.array_num_files: Checkers.check_field_not_null(LstFilesOfSubrun.array_num_files,
                                                                                    array_num_files)
                },
                    synchronize_session=False
                )
                self.__session.commit()
                files_after: FilesOfSubrunDto = self.__files_by_id(id_file_subrun)
                if files_before.__dict__ != files_after.__dict__:
                    print("RECORD UPDATE IN TABLE '{}' WITH ID '{}'".format(LstFilesOfSubrun.__tablename__.name,
                                                                            id_file_subrun))
                else:
                    print(" THE RECORD OF TABLE '{}' HAS NOT BEEN UPDATED".format(LstFilesOfSubrun.__tablename__.name))
            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE UPDATED ".format(LstFilesOfSubrun.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def delete_files_of_subrun(self, id_file_subrun):
        try:
            files_before: FilesOfSubrunDto = self.__files_by_id(id_file_subrun)
            if Checkers.validate_int(id_file_subrun,
                                     LstFilesOfSubrun.id_file_subrun.name) and files_before.id_file_subrun is not None:
                self.__session.query(LstFilesOfSubrun).filter(LstFilesOfSubrun.id_file_subrun.like(id_file_subrun)) \
                    .delete(synchronize_session=False)
                self.__session.commit()
                files_after: FilesOfSubrunDto = self.__files_by_id(id_file_subrun)
                if files_before.id_file_subrun is not None and files_after.id_file_subrun is None:
                    print("RECORD DELETE IN TABLE '{}' WITH ID '{}'".format(LstFilesOfSubrun.__tablename__.name,
                                                                            id_file_subrun))
                else:
                    print(" THE RECORD OF TABLE '{}' WITH ID '{}' HAS NOT BEEN DELETED BECAUSE IT DID NOT EXIST".format(
                        LstFilesOfSubrun.__tablename__.name,
                        id_file_subrun))
            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE DELETED".format(LstFilesOfSubrun.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def get_all_files_of_subrun(self):
        files_dto_list = []
        try:
            self.__all_files_of_subrun: List[FilesOfSubrunDto] = self.__session.query(LstFilesOfSubrun).all()
            if len(self.__all_files_of_subrun) != 0:
                for row in self.__all_files_of_subrun:
                    files_aux = create_files_of_subrun(
                        row.id_file_subrun,
                        row.subrun_number,
                        row.path_file,
                        row.num_events,
                        row.array_num_files
                    )
                    files_dto_list.append(files_aux)
            else:
                Checkers.empty_list(LstFilesOfSubrun.__tablename__.name)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return files_dto_list

    def get_file_subrun_by_id(self, id_file_subrun):
        try:
            self.__files_by_id: FilesOfSubrunDto = self.__session.query(LstFilesOfSubrun).filter(
                LstFilesOfSubrun.id_file_subrun.like(id_file_subrun)).first()
            if self.__files_by_id is not None:
                return create_files_of_subrun(
                    self.__files_by_id.id_file_subrun,
                    self.__files_by_id.subrun_number,
                    self.__files_by_id.path_file,
                    self.__files_by_id.num_events,
                    self.__files_by_id.array_num_files
                )
            else:
                Checkers.print_object_filter_null(LstFilesOfSubrun.id_file_subrun, str(id_file_subrun))
                return create_files_of_subrun(None, None, None, None, None)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return create_files_of_subrun(None, None, None, None, None)
