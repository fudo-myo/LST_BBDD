from typing import List

from sqlalchemy.exc import InvalidRequestError, OperationalError
from sqlalchemy.orm import Session

from DTO.dates_dto import DatesDto, create_date
from config.base import getSession
from utils.checkers import Checkers

try:
    from entities.lst_dates import LstDates
except ImportError as error:
    Checkers.print_exception_one_param(error)


class LstDatesService:

    def __init__(self):
        self.__session: Session = getSession()
        self.__all_dates = None
        self.__date_by_id = None

    def insert_dates(self, dates_insert: DatesDto):
        try:
            dates_aux = LstDates(date=dates_insert.date)
            self.__session.add(dates_aux)
            self.__session.commit()
            if dates_aux.id_date is not None:
                print("RECORD INSERTED IN TABLE '{}' WITH ID '{}'".format(LstDates.__tablename__.name,
                                                                          dates_aux.id_date))
            else:
                print(" THE RECORD OF TABLE '{}' HAS NOT BEEN INSERTED".format(LstDates.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def update_dates(self, date_to_serach, id_date, date_to_update=None):
        try:
            date_before: DatesDto = self.get_date_by_id(id_date)
            if Checkers.validate_int(id_date, LstDates.id_date.name) and Checkers.validate_datetime(
                    date_to_serach, LstDates.date) and date_before.id_date is not None and date_before.date is not None:
                self.__session.query(LstDates).filter(LstDates.date.like(date_to_serach),
                                                      LstDates.id_date.like(id_date)) \
                    .update({
                    LstDates.date: Checkers.check_field_not_null(LstDates.date, date_to_update)},
                    synchronize_session=False
                )
                self.__session.commit()
                date_after: DatesDto = self.get_date_by_id(id_date)
                if date_before.__dict__ != date_after.__dict__:
                    print("RECORD UPDATE IN TABLE '{}' WITH ID '{}'".format(LstDates.__tablename__.name,
                                                                            id_date))
                else:
                    print(" THE RECORD OF TABLE '{}' HAS NOT BEEN UPDATED".format(LstDates.__tablename__.name))
            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE UPDATED ".format(LstDates.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def delete_date(self, date_to_delete, id_date):
        try:
            date_before: DatesDto = self.get_date_by_id(id_date)
            if Checkers.validate_int(id_date, LstDates.id_date.name) and Checkers.validate_datetime(
                    date_to_delete, LstDates.date) and date_before.id_date is not None and date_before.date is not None:
                self.__session.query(LstDates).filter(LstDates.date.like(date_to_delete),
                                                      LstDates.id_date.like(id_date)) \
                    .delete(synchronize_session=False)
                self.__session.commit()
                date_after: DatesDto = self.get_date_by_id(id_date)
                if date_before.id_date is not None and date_after.id_date is None:
                    print("RECORD DELETE IN TABLE '{}' WITH ID '{}'".format(LstDates.__tablename__.name,
                                                                            id_date))
                else:
                    print(" THE RECORD OF TABLE '{}' WITH ID '{}' HAS NOT BEEN DELETED BECAUSE IT DID NOT EXIST".format(
                        LstDates.__tablename__.name,
                        id_date))
            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE DELETED".format(LstDates.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def get_all_dates(self):
        dates_dto_list = []
        try:
            self.__all_dates: List[DatesDto] = self.__session.query(LstDates).all()
            if len(self.__all_dates) != 0:
                for row in self.__all_dates:
                    date_aux = create_date(
                        row.id_date,
                        row.date
                    )
                    dates_dto_list.append(date_aux)
            else:
                Checkers.empty_list(LstDates.__tablename__.name)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return dates_dto_list

    def get_date_by_id(self, id_date):
        try:
            self.__date_by_id: DatesDto = self.__session.query(LstDates).filter(LstDates.id_date.like(id_date)).first()
            if self.__date_by_id is not None:
                return create_date(
                    self.__date_by_id.id_date,
                    self.__date_by_id.date,
                )
            else:
                Checkers.print_object_filter_null(LstDates.id_date, str(id_date))
                return create_date(None, None)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return create_date(None, None)
