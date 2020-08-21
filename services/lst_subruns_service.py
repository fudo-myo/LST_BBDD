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
                id_run=subruns_insert.id_run,
                date=subruns_insert.date,
                hour=subruns_insert.hour,
                stream=subruns_insert.stream,
                events=subruns_insert.events,
                length=subruns_insert.length,
                rate=subruns_insert.rate,
                size=subruns_insert.size,
                event_type=subruns_insert.event_type,
                process_state=subruns_insert.process_state
            )
            self.__session.add(subruns_aux)
            self.__session.commit()
            if subruns_aux.id_subrun is not None:
                subruns_insert.id_subrun = subruns_aux.id_subrun
                print("RECORD INSERTED IN TABLE '{}' WITH ID '{}'".format(LstSubruns.__tablename__.name,
                                                                          subruns_aux.id_subrun))
            else:
                print(" THE RECORD OF TABLE '{}' HAS NOT BEEN INSERTED".format(LstSubruns.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def update_subruns(self, id_subrun, subrun_number_to_search, subrun_number_to_update=None, id_run=None,
                       date=None, hour=None, stream=None, events=None, length=None, rate=None, size=None,
                       event_type=None, process_state=None, ):
        try:
            subruns_before: SubrunsDto = self.get_subrun_by_id(id_subrun, subrun_number_to_search)
            if Checkers.validate_int(id_subrun, LstSubruns.id_subrun.name) and \
                    Checkers.validate_int(subrun_number_to_search, LstSubruns.subrun_number.name) and \
                    subruns_before.subrun_number is not None and \
                    subruns_before.id_subrun is not None:
                self.__session.query(LstSubruns).filter(LstSubruns.id_subrun.like(id_subrun)) \
                    .filter(LstSubruns.subrun_number.like(subrun_number_to_search)) \
                    .update({
                    LstSubruns.subrun_number: Checkers.check_field_not_null(LstSubruns.subrun_number,
                                                                            subrun_number_to_update),
                    LstSubruns.id_run: Checkers.check_field_not_null(LstSubruns.id_run, id_run),
                    LstSubruns.date: Checkers.check_field_not_null(LstSubruns.date, date),
                    LstSubruns.hour: Checkers.check_field_not_null(LstSubruns.hour, hour),
                    LstSubruns.stream: Checkers.check_field_not_null(LstSubruns.stream, stream),
                    LstSubruns.events: Checkers.check_field_not_null(LstSubruns.events, events),
                    LstSubruns.length: Checkers.check_field_not_null(LstSubruns.length, length),
                    LstSubruns.rate: Checkers.check_field_not_null(LstSubruns.rate, rate),
                    LstSubruns.size: Checkers.check_field_not_null(LstSubruns.size, size),
                    LstSubruns.event_type: Checkers.check_field_not_null(LstSubruns.event_type, event_type),
                    LstSubruns.process_state: Checkers.check_field_not_null(LstSubruns.process_state, process_state)
                },
                    synchronize_session=False
                )
                self.__session.commit()
                subruns_after: SubrunsDto = self.get_subrun_by_id(id_subrun,
                                                                  Checkers.check_field_not_null(
                                                                      subruns_before.subrun_number,
                                                                      subrun_number_to_update))
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

    def delete_subruns(self, id_subrun, subrun_number):
        try:
            subruns_before: SubrunsDto = self.get_subrun_by_id(id_subrun, subrun_number)
            if Checkers.validate_int(id_subrun, LstSubruns.id_subrun.name) and subruns_before.id_subrun is not None:
                self.__session.query(LstSubruns).filter(LstSubruns.id_subrun.like(id_subrun)) \
                    .delete(synchronize_session=False)
                self.__session.commit()
                subruns_after: SubrunsDto = self.get_subrun_by_id(id_subrun, subrun_number)
                if subruns_before.id_subrun is not None and \
                        subruns_before.subrun_number is not None and \
                        subruns_after.subrun_number is None and \
                        subruns_after.id_subrun is None:
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
                        row.id_run,
                        row.date,
                        row.hour,
                        row.stream,
                        row.events,
                        row.length,
                        row.rate,
                        row.size,
                        row.event_type,
                        row.process_state
                    )
                    subruns_dto_list.append(subrun_aux)
            else:
                Checkers.empty_list(LstSubruns.__tablename__.name)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return subruns_dto_list

    def get_subrun_by_id(self, id_subrun=None, subrun_number=None):
        try:
            if id_subrun is not None:
                self.__subruns_by_id: SubrunsDto = self.__session.query(LstSubruns).filter(
                    LstSubruns.id_subrun.like(id_subrun),
                    LstSubruns.subrun_number.like(subrun_number)).first()
            else:
                self.__subruns_by_id: SubrunsDto = self.__session.query(LstSubruns).filter(
                    LstSubruns.subrun_number.like(subrun_number)).first()
            if self.__subruns_by_id is not None:
                return create_subrun(
                    self.__subruns_by_id.id_subrun,
                    self.__subruns_by_id.subrun_number,
                    self.__subruns_by_id.id_run,
                    self.__subruns_by_id.date,
                    self.__subruns_by_id.hour,
                    self.__subruns_by_id.stream,
                    self.__subruns_by_id.events,
                    self.__subruns_by_id.length,
                    self.__subruns_by_id.rate,
                    self.__subruns_by_id.size,
                    self.__subruns_by_id.event_type,
                    self.__subruns_by_id.process_state
                )
            else:
                Checkers.print_object_filter_null(LstSubruns.id_subrun.name, str(id_subrun))
                return create_subrun(None, None, None, None, None, None, None, None, None, None, None, None)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return create_subrun(None, None, None, None, None, None, None, None, None, None, None, None)

    def get_subrun_by_idrun_and_subrun(self, id_run, subrun_number):
        try:

            self.__subruns_by_id: SubrunsDto = self.__session.query(LstSubruns).filter(
                LstSubruns.id_run.like(id_run),
                LstSubruns.subrun_number.like(subrun_number)).first()
            if self.__subruns_by_id is not None:
                return create_subrun(
                    self.__subruns_by_id.id_subrun,
                    self.__subruns_by_id.subrun_number,
                    self.__subruns_by_id.id_run,
                    self.__subruns_by_id.date,
                    self.__subruns_by_id.hour,
                    self.__subruns_by_id.stream,
                    self.__subruns_by_id.events,
                    self.__subruns_by_id.length,
                    self.__subruns_by_id.rate,
                    self.__subruns_by_id.size,
                    self.__subruns_by_id.event_type,
                    self.__subruns_by_id.process_state
                )
            else:
                Checkers.print_object_filter_null(LstSubruns.id_subrun.name, str(id_run))
                return create_subrun(None, None, None, None, None, None, None, None, None, None, None, None)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return create_subrun(None, None, None, None, None, None, None, None, None, None, None, None)
