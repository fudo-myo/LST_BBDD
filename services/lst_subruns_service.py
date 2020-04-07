from typing import List

from sqlalchemy.exc import InvalidRequestError, OperationalError
from sqlalchemy.orm import Session

from DTO.subruns_dto import SubrunsDto, create_subrun
from config.base import getSession
from utils.checkers import Checkers

try:
    from entities.lst_subruns import LstSubruns
except ImportError as error:
    Checkers.print_exception_one_param(error)


class LstSubrunsService:

    def __init__(self):
        self.__session: Session = getSession()
        self.__all_subruns = None
        self.__subruns_by_id = None

    def insert_subruns(self, subruns_insert: SubrunsDto):
        try:
            subruns_aux = LstSubruns(
                subrun_number=subruns_insert.subrun_number,
                run_number=subruns_insert.run_number,
                id_run_type=subruns_insert.id_run_type
            )
            self.__session.add(subruns_aux)
            self.__session.commit()
            if subruns_aux.id_subrun is not None:
                print("RECORD INSERTED IN TABLE '{}' WITH ID '{}'".format(LstSubruns.__tablename__.name,
                                                                          subruns_aux.id_subrun))
            else:
                print(" THE RECORD OF TABLE '{}' HAS NOT BEEN INSERTED".format(LstSubruns.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def update_subruns(self, id_subrun, subrun_number_to_search, subrun_number_to_update=None, run_number=None,
                       id_run_type=None):
        try:
            subruns_before: SubrunsDto = self.get_subrun_by_id(id_subrun)
            if Checkers.validate_int(id_subrun, LstSubruns.id_subrun.name) and subruns_before.id_subrun is not None:
                self.__session.query(LstSubruns).filter(LstSubruns.id_subrun.like(id_subrun)) \
                    .filter(LstSubruns.subrun_number.like(subrun_number_to_search)) \
                    .update({
                    LstSubruns.subrun_number: Checkers.check_field_not_null(LstSubruns.subrun_number,
                                                                            subrun_number_to_update),
                    LstSubruns.run_number: Checkers.check_field_not_null(LstSubruns.run_number, run_number),
                    LstSubruns.id_run_type: Checkers.check_field_not_null(LstSubruns.id_run_type, id_run_type)
                },
                    synchronize_session=False
                )
                self.__session.commit()
                subruns_after: SubrunsDto = self.get_subrun_by_id(id_subrun)
                if subruns_before.__dict__ != subruns_after.__dict__:
                    print("RECORD UPDATE IN TABLE '{}' WITH ID '{}'".format(LstSubruns.__tablename__.name,
                                                                            id_subrun))
                else:
                    print(" THE RECORD OF TABLE '{}' HAS NOT BEEN UPDATED".format(LstSubruns.__tablename__.name))
            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE UPDATED ".format(LstSubruns.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def delete_subruns(self, id_subrun):
        try:
            subruns_before: SubrunsDto = self.get_subrun_by_id(id_subrun)
            if Checkers.validate_int(id_subrun, LstSubruns.id_subrun.name) and subruns_before.id_subrun is not None:
                self.__session.query(LstSubruns).filter(LstSubruns.id_subrun.like(id_subrun)) \
                    .delete(synchronize_session=False)
                self.__session.commit()
                subruns_after: SubrunsDto = self.get_subrun_by_id(id_subrun)
                if subruns_before.id_subrun is not None and subruns_after.id_subrun is None:
                    print("RECORD DELETE IN TABLE '{}' WITH ID '{}'".format(LstSubruns.__tablename__.name,
                                                                            id_subrun))
                else:
                    print(" THE RECORD OF TABLE '{}' WITH ID '{}' HAS NOT BEEN DELETED BECAUSE IT DID NOT EXIST".format(
                        LstSubruns.__tablename__.name,
                        id_subrun))
            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE DELETED".format(LstSubruns.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def get_all_subruns(self):
        subruns_dto_list = []
        try:
            self.__all_subruns: List[SubrunsDto] = self.__session.query(LstSubruns).all()
            if len(self.__all_subruns) != 0:
                for row in self.__all_subruns:
                    subrun_aux = create_subrun(
                        row.id_subrun,
                        row.subrun_number,
                        row.run_number,
                        row.id_run_type
                    )
                    subruns_dto_list.append(subrun_aux)
            else:
                Checkers.empty_list(LstSubruns.__tablename__.name)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return subruns_dto_list

    def get_subrun_by_id(self, id_subrun):
        try:
            self.__subruns_by_id: SubrunsDto = self.__session.query(LstSubruns).filter(
                LstSubruns.id_subrun.like(id_subrun)).first()
            if self.__subruns_by_id is not None:
                return create_subrun(
                    self.__subruns_by_id.id_subrun,
                    self.__subruns_by_id.subrun_number,
                    self.__subruns_by_id.run_number,
                    self.__subruns_by_id.id_run_type
                )
            else:
                Checkers.print_object_filter_null(LstSubruns.id_subrun.name, str(id_subrun))
                return create_subrun(None, None, None, None)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return create_subrun(None, None, None, None)
