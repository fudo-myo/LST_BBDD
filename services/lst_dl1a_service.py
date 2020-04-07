from typing import List

from sqlalchemy.exc import InvalidRequestError, OperationalError
from sqlalchemy.orm import Session

from DTO.dl1a_dto import Dl1aDto, create_dl1a
from config.base import getSession
from utils.checkers import Checkers

try:
    from entities.lst_dl1a import LstDl1a
except ImportError as error:
    Checkers.print_exception_one_param(error)


class LstDl1aService:

    def __init__(self):
        self.__session: Session = getSession()
        self.__all_dl1a = None
        self.__dl1a_by_id = None

    def insert_dl1a(self, dl1a_insert: Dl1aDto):
        try:
            dl1a_aux = LstDl1a(subrun_number=dl1a_insert.subrun_number,
                               dl1a_path_file=dl1a_insert.dl1a_path_file)

            self.__session.add(dl1a_aux)
            self.__session.commit()
            if dl1a_aux.id_dl1a is not None:
                print("RECORD INSERTED IN TABLE '{}' WITH ID '{}'".format(LstDl1a.__tablename__.name,
                                                                          dl1a_aux.id_dl1a))
            else:
                print(" THE RECORD OF TABLE '{}' HAS NOT BEEN INSERTED".format(LstDl1a.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def update_dl1a(self, id_dl1a, subrun_number=None, dl1a_path_file=None):
        try:
            dl1a_before: Dl1aDto = self.get_dl1a_by_id(id_dl1a)
            if Checkers.validate_int(id_dl1a, LstDl1a.id_dl1a) and dl1a_before.id_dl1a is not None:
                self.__session.query(LstDl1a).filter(LstDl1a.id_dl1a.like(id_dl1a)) \
                    .update({
                    LstDl1a.subrun_number: Checkers.check_field_not_null(LstDl1a.subrun_number, subrun_number),
                    LstDl1a.dl1a_path_file: Checkers.check_field_not_null(LstDl1a.dl1a_path_file, dl1a_path_file)
                },
                    synchronize_session=False
                )
                self.__session.commit()
                dl1a_after: Dl1aDto = self.get_dl1a_by_id(id_dl1a)
                if dl1a_before.__dict__ != dl1a_after.__dict__:
                    print("RECORD UPDATE IN TABLE '{}' WITH ID '{}'".format(LstDl1a.__tablename__.name,
                                                                            id_dl1a))
                else:
                    print(" THE RECORD OF TABLE '{}' HAS NOT BEEN UPDATED".format(LstDl1a.__tablename__.name))

            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE UPDATED ".format(LstDl1a.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def delete_dl1a(self, id_dl1a):
        try:
            dl1a_before: Dl1aDto = self.get_dl1a_by_id(id_dl1a)
            if Checkers.validate_int(id_dl1a, LstDl1a.id_dl1a) and dl1a_before.id_dl1a is not None:
                self.__session.query(LstDl1a).filter(LstDl1a.id_dl1a.like(id_dl1a)) \
                    .delete(synchronize_session=False)
                self.__session.commit()
                dl1a_after: Dl1aDto = self.get_dl1a_by_id(id_dl1a)
                if dl1a_before.id_dl1a is not None and dl1a_after.id_dl1a is None:
                    print("RECORD DELETE IN TABLE '{}' WITH ID '{}'".format(LstDl1a.__tablename__.name,
                                                                            id_dl1a))
                else:
                    print(" THE RECORD OF TABLE '{}' WITH ID '{}' HAS NOT BEEN DELETED BECAUSE IT DID NOT EXIST".format(
                        LstDl1a.__tablename__.name,
                        id_dl1a))
            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE DELETED".format(LstDl1a.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def get_all_dl1a(self):
        dl1a_dto_list = []
        try:
            self.__all_dl1a: List[Dl1aDto] = self.__session.query(LstDl1a).all()
            if len(self.__all_dl1a) != 0:
                for row in self.__all_dl1a:
                    dl1a_aux = create_dl1a(
                        row.id_dl1a,
                        row.subrun_number,
                        row.dl1a_path_file
                    )
                    dl1a_dto_list.append(dl1a_aux)
            else:
                Checkers.empty_list(LstDl1a.__tablename__.name)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return dl1a_dto_list

    def get_dl1a_by_id(self, id_dl1a):
        try:
            self.__dl1a_by_id: Dl1aDto = self.__session.query(LstDl1a).filter(LstDl1a.id_dl1a.like(id_dl1a)).first()
            if self.__dl1a_by_id is not None:
                return create_dl1a(
                    self.__dl1a_by_id.id_dl1a,
                    self.__dl1a_by_id.subrun_number,
                    self.__dl1a_by_id.dl1a_path_file
                )
            else:
                Checkers.print_object_filter_null(LstDl1a.id_dl1a.name, str(id_dl1a))
                return create_dl1a(None, None, None)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return create_dl1a(None, None, None)
