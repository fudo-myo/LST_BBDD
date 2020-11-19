from typing import List

from sqlalchemy.exc import InvalidRequestError, OperationalError
from sqlalchemy.orm import Session

from DTO.r1_data_check_generic_dto import R1DataCheckGenericDto, create_r1_data_check_generic
from config.base import get_session
from utils.checkers import Checkers

try:
    from entities.lst_r1_data_check_generic import LstR1DataCheckGeneric
except ImportError as error:
    Checkers.print_exception_one_param(error)


class LstR1DataCheckGenericService:

    def __init__(self):
        self.__session: Session = get_session()
        self.__all_r1_data_check_generic = None
        self.__r1_data_check_generic_by_id = None

    def insert_r1_data_check_generic(self, r1_data_check_generic_insert: R1DataCheckGenericDto):
        try:
            r1_data_check_generic_aux = LstR1DataCheckGeneric(
                init_event=r1_data_check_generic_insert.init_event,
                end_event=r1_data_check_generic_insert.end_event,
                init_pixel=r1_data_check_generic_insert.init_pixel,
                end_pixel=r1_data_check_generic_insert.end_pixel,
                init_sample=r1_data_check_generic_insert.init_sample,
                end_sample=r1_data_check_generic_insert.end_sample,
                init_subrun=r1_data_check_generic_insert.init_subrun,
                end_subrun=r1_data_check_generic_insert.end_subrun,
                type_of_gap_calc=r1_data_check_generic_insert.type_of_gap_calc,
                list_of_module_in_detail=r1_data_check_generic_insert.list_of_module_in_detail
            )
            self.__session.add(r1_data_check_generic_aux)
            self.__session.commit()
            if r1_data_check_generic_aux.id_r1_data_check_generic is not None:
                r1_data_check_generic_insert.id_r1_data_check_generic = r1_data_check_generic_aux.id_r1_data_check_generic
                print("RECORD INSERTED IN TABLE '{}' WITH ID '{}'".format(LstR1DataCheckGeneric.__tablename__.name,
                                                                          r1_data_check_generic_aux.id_r1_data_check_generic))
            else:
                print(
                    " THE RECORD OF TABLE '{}' HAS NOT BEEN INSERTED".format(LstR1DataCheckGeneric.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def update_r1_data_check_generic(self, id_r1_data_check_generic, init_event=None, end_event=None, init_pixel=None,
                                     end_pixel=None,
                                     init_sample=None, end_sample=None, init_subrun=None, end_subrun=None,
                                     type_of_gap_calc=None,
                                     list_of_module_in_detail=None):
        try:
            r1_before: R1DataCheckGenericDto = self.get_r1_data_check_generic_by_id(id_r1_data_check_generic)
            if Checkers.validate_int(id_r1_data_check_generic,
                                     LstR1DataCheckGeneric.id_r1_data_check_generic.name) and r1_before.id_r1_data_check_generic is not None:
                self.__session.query(LstR1DataCheckGeneric).filter(
                    LstR1DataCheckGeneric.id_r1_data_check_generic.like(id_r1_data_check_generic)) \
                    .update({
                    LstR1DataCheckGeneric.init_event: Checkers.check_field_not_null(LstR1DataCheckGeneric.init_event,
                                                                                    init_event),
                    LstR1DataCheckGeneric.end_event: Checkers.check_field_not_null(LstR1DataCheckGeneric.end_event,
                                                                                   end_event),
                    LstR1DataCheckGeneric.init_pixel: Checkers.check_field_not_null(LstR1DataCheckGeneric.init_pixel,
                                                                                    init_pixel),
                    LstR1DataCheckGeneric.end_pixel: Checkers.check_field_not_null(LstR1DataCheckGeneric.end_pixel,
                                                                                   end_pixel),
                    LstR1DataCheckGeneric.init_sample: Checkers.check_field_not_null(LstR1DataCheckGeneric.init_sample,
                                                                                     init_sample),
                    LstR1DataCheckGeneric.end_sample: Checkers.check_field_not_null(LstR1DataCheckGeneric.end_sample,
                                                                                    end_sample),
                    LstR1DataCheckGeneric.init_subrun: Checkers.check_field_not_null(LstR1DataCheckGeneric.init_subrun,
                                                                                     init_subrun),
                    LstR1DataCheckGeneric.end_subrun: Checkers.check_field_not_null(LstR1DataCheckGeneric.end_subrun,
                                                                                    end_subrun),
                    LstR1DataCheckGeneric.type_of_gap_calc: Checkers.check_field_not_null(
                        LstR1DataCheckGeneric.type_of_gap_calc, type_of_gap_calc),
                    LstR1DataCheckGeneric.list_of_module_in_detail: Checkers.check_field_not_null(
                        LstR1DataCheckGeneric.list_of_module_in_detail, list_of_module_in_detail)
                },
                    synchronize_session=False
                )
                self.__session.commit()
                r1_after: R1DataCheckGenericDto = self.get_r1_data_check_generic_by_id(id_r1_data_check_generic)
                if r1_before.__dict__ != r1_after.__dict__:
                    print("RECORD UPDATE IN TABLE '{}' WITH ID '{}'".format(LstR1DataCheckGeneric.__tablename__.name,
                                                                            id_r1_data_check_generic))
                else:
                    print(" THE RECORD OF TABLE '{}' HAS NOT BEEN UPDATED".format(
                        LstR1DataCheckGeneric.__tablename__.name))

            else:
                print(
                    " THE RECORD OF TABLE '{}' COULD NOT BE UPDATED ".format(LstR1DataCheckGeneric.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def delete_r1_data_check_generic(self, id_r1_data_check_generic):
        try:
            r1_before: R1DataCheckGenericDto = self.get_r1_data_check_generic_by_id(id_r1_data_check_generic)
            if Checkers.validate_int(id_r1_data_check_generic,
                                     LstR1DataCheckGeneric.id_r1_data_check_generic.name) and r1_before.id_r1_data_check_generic is not None:
                self.__session.query(LstR1DataCheckGeneric).filter(
                    LstR1DataCheckGeneric.id_r1_data_check_generic.like(id_r1_data_check_generic)) \
                    .delete(synchronize_session=False)
                self.__session.commit()
                r1_after: R1DataCheckGenericDto = self.get_r1_data_check_generic_by_id(id_r1_data_check_generic)
                if r1_before.id_r1_data_check_generic is not None and r1_after.id_r1_data_check_generic is None:
                    print("RECORD DELETE IN TABLE '{}' WITH ID '{}'".format(LstR1DataCheckGeneric.__tablename__.name,
                                                                            id_r1_data_check_generic))
                else:
                    print(" THE RECORD OF TABLE '{}' WITH ID '{}' HAS NOT BEEN DELETED BECAUSE IT DID NOT EXIST".format(
                        LstR1DataCheckGeneric.__tablename__.name,
                        id_r1_data_check_generic))
            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE DELETED".format(LstR1DataCheckGeneric.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def get_all_r1_data_check_generic(self):
        r1_data_check_generic_dto_list = []
        try:
            self.__all_r1_data_check_generic: List[R1DataCheckGenericDto] = self.__session.query(
                LstR1DataCheckGeneric).all()
            if len(self.__all_r1_data_check_generic) != 0:
                for row in self.__all_r1_data_check_generic:
                    r1_aux = create_r1_data_check_generic(
                        row.id_r1_data_check_generic,
                        row.init_event,
                        row.end_event,
                        row.init_pixel,
                        row.end_pixel,
                        row.init_sample,
                        row.end_sample,
                        row.init_subrun,
                        row.end_subrun,
                        row.type_of_gap_calc,
                        row.list_of_module_in_detail
                    )
                    r1_data_check_generic_dto_list.append(r1_aux)
            else:
                Checkers.empty_list(LstR1DataCheckGeneric.__tablename__.name)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return r1_data_check_generic_dto_list

    def get_r1_data_check_generic_by_id(self, id_r1_data_check_generic):
        try:
            self.__r1_data_check_generic_by_id: R1DataCheckGenericDto = self.__session.query(
                LstR1DataCheckGeneric).filter(
                LstR1DataCheckGeneric.id_r1_data_check_generic.like(id_r1_data_check_generic)).first()
            if self.__r1_data_check_generic_by_id is not None:
                return create_r1_data_check_generic(
                    self.__r1_data_check_generic_by_id.id_r1_data_check_generic,
                    self.__r1_data_check_generic_by_id.init_event,
                    self.__r1_data_check_generic_by_id.end_event,
                    self.__r1_data_check_generic_by_id.init_pixel,
                    self.__r1_data_check_generic_by_id.end_pixel,
                    self.__r1_data_check_generic_by_id.init_sample,
                    self.__r1_data_check_generic_by_id.end_sample,
                    self.__r1_data_check_generic_by_id.init_subrun,
                    self.__r1_data_check_generic_by_id.end_subrun,
                    self.__r1_data_check_generic_by_id.type_of_gap_calc,
                    self.__r1_data_check_generic_by_id.list_of_module_in_detail
                )
            else:
                Checkers.print_object_filter_null(LstR1DataCheckGeneric.id_r1_data_check_generic.name,
                                                  str(id_r1_data_check_generic))
                return create_r1_data_check_generic(None, None, None, None, None, None, None, None, None, None, None)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return create_r1_data_check_generic(None, None, None, None, None, None, None, None, None, None, None)
