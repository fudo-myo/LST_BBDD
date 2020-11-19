from typing import List

from sqlalchemy.exc import InvalidRequestError, OperationalError
from sqlalchemy.orm import Session

from DTO.dates_dto import DatesDto, create_date
from config.base import get_session
from utils.checkers import Checkers

try:
    from entities.lst_dates import LstDates
except ImportError as error:
    Checkers.print_exception_one_param(error)


class LstDatesService:

    def __init__(self):
        self.__session: Session = get_session()
        self.__all_dates = None
        self.__date_by_id = None
        self.__date_between = None

    def insert_dates(self, dates_insert: DatesDto):
        try:
            dates_aux = LstDates(date_entity=dates_insert.date_dto)
            self.__session.add(dates_aux)
            self.__session.commit()
            if dates_aux.id_date is not None:
                dates_insert.id_date = dates_aux.id_date
                print("RECORD INSERTED IN TABLE '{}' WITH ID '{}'".format(LstDates.__tablename__.name,
                                                                          dates_aux.id_date))
            else:
                print(" THE RECORD OF TABLE '{}' HAS NOT BEEN INSERTED".format(LstDates.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def update_dates(self, id_date, date_to_search, date_to_update=None):
        try:
            date_before: DatesDto = self.get_date_by_id(date_to_search, id_date)
            if Checkers.validate_int(id_date, LstDates.id_date.name) and \
                    Checkers.validate_date(date_to_search, LstDates.date_entity.name) and \
                    date_before.id_date is not None and \
                    date_before.date_dto is not None:
                self.__session.query(LstDates).filter(LstDates.date_entity.like(date_to_search),
                                                      LstDates.id_date.like(id_date)) \
                    .update({
                    LstDates.date_entity: Checkers.check_field_not_null(LstDates.date_entity, date_to_update)},
                    synchronize_session=False
                )
                self.__session.commit()
                date_after: DatesDto = self.get_date_by_id(Checkers.check_field_not_null(date_before.date_dto,
                                                                                         date_to_update), id_date)
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

    def delete_date(self, id_date, date_to_delete):
        try:
            date_before: DatesDto = self.get_date_by_id(date_to_delete, id_date)
            if Checkers.validate_int(id_date, LstDates.id_date.name) and \
                    Checkers.validate_date(date_to_delete, LstDates.date_entity.name) and \
                    date_before.id_date is not None and \
                    date_before.date_dto is not None:
                self.__session.query(LstDates).filter(LstDates.date_entity.like(date_to_delete),
                                                      LstDates.id_date.like(id_date)) \
                    .delete(synchronize_session=False)
                self.__session.commit()
                date_after: DatesDto = self.get_date_by_id(date_to_delete, id_date)
                if date_before.id_date is not None and \
                        date_before.date_dto is not None and \
                        date_after.date_dto is None and \
                        date_after.id_date is None:
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
            self.__all_dates = self.__session.query(LstDates).all()
            if len(self.__all_dates) != 0:
                for row in self.__all_dates:
                    date_aux = create_date(
                        row.id_date,
                        row.date_entity
                    )
                    dates_dto_list.append(date_aux)
            else:
                Checkers.empty_list(LstDates.__tablename__.name)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return dates_dto_list

    def get_date_by_id(self, date=None, id_date=None):
        try:
            if id_date is not None:
                self.__date_by_id = self.__session.query(LstDates).filter(
                    LstDates.id_date.like(id_date),
                    LstDates.date_entity.like(date)).first()
            else:
                self.__date_by_id = self.__session.query(LstDates).filter(
                    LstDates.date_entity.like(date)).first()
            if self.__date_by_id is not None:
                return create_date(
                    self.__date_by_id.id_date,
                    self.__date_by_id.date_entity,
                )
            else:
                Checkers.print_object_filter_null(LstDates.id_date, str(id_date))
                return create_date(None, None)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return create_date(None, None)

    def get_date_between_dates(self, date_from, date_to):
        dates_dto_list = []
        try:
            self.__date_between = self.__session.query(LstDates.id_date).filter(
                LstDates.date_entity >= date_from,
                LstDates.date_entity <= date_to
            ).all()
            if len(self.__date_between) != 0:
                for row in self.__date_between:
                    date_aux = create_date(
                        row.id_date,
                        row.date_entity
                    )
                    dates_dto_list.append(date_aux)
        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return dates_dto_list
