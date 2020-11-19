from typing import List

from sqlalchemy.exc import InvalidRequestError, OperationalError
from sqlalchemy.orm import Session

from DTO.productions_dto import ProductionsDto, create_productions
from config.base import get_session
from utils.checkers import Checkers

try:
    from entities.lst_productions import LstProductions
except ImportError as error:
    Checkers.print_exception_one_param(error)


class LstProductionsService:

    def __init__(self):
        self.__session: Session = get_session()
        self.__all_productions = None
        self.__prod_by_id = None

    def insert_productions(self, productions_insert: ProductionsDto):
        try:
            productions_aux = LstProductions(
                run_number=productions_insert.run_number,
                id_run_type=productions_insert.id_run_type,
                r1_check_build=productions_insert.r1_check_build,
                dl1a_check_build=productions_insert.dl1a_check_build,
                dl1b_check_build=productions_insert.dl1b_check_build,
                dl2_check_build=productions_insert.dl2_check_build,
                number_production=productions_insert.number_production
            )
            self.__session.add(productions_aux)
            self.__session.commit()
            if productions_aux.id_production is not None:
                productions_insert.id_production = productions_aux.id_production
                print("RECORD INSERTED IN TABLE '{}' WITH ID '{}'".format(LstProductions.__tablename__.name,
                                                                          productions_aux.id_production))
            else:
                print(" THE RECORD OF TABLE '{}' HAS NOT BEEN INSERTED".format(LstProductions.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def update_productions(self, id_production, run_number=None, id_run_type=None, r1_check_build=None,
                           dl1a_check_build=None,
                           dl1b_check_build=None, dl2_check_build=None, number_production=None):
        try:
            prod_before: ProductionsDto = self.get_productions_by_id(id_production)
            if Checkers.validate_int(id_production,
                                     LstProductions.id_production.name) and prod_before.id_production is not None:
                self.__session.query(LstProductions).filter(LstProductions.id_production.like(id_production)) \
                    .update({
                    LstProductions.run_number: Checkers.check_field_not_null(LstProductions.run_number, run_number),
                    LstProductions.id_run_type: Checkers.check_field_not_null(LstProductions.id_run_type, id_run_type),
                    LstProductions.r1_check_build: Checkers.check_field_not_null(LstProductions.r1_check_build,
                                                                                 r1_check_build),
                    LstProductions.dl1a_check_build: Checkers.check_field_not_null(LstProductions.dl1a_check_build,
                                                                                   dl1a_check_build),
                    LstProductions.dl1b_check_build: Checkers.check_field_not_null(LstProductions.dl1b_check_build,
                                                                                   dl1b_check_build),
                    LstProductions.dl2_check_build: Checkers.check_field_not_null(LstProductions.dl2_check_build,
                                                                                  dl2_check_build),
                    LstProductions.number_production: Checkers.check_field_not_null(LstProductions.number_production,
                                                                                    number_production)
                },
                    synchronize_session=False
                )
                self.__session.commit()
                prod_after: ProductionsDto = self.get_productions_by_id(id_production)
                if prod_before.__dict__ != prod_after.__dict__:
                    print("RECORD UPDATE IN TABLE '{}' WITH ID '{}'".format(LstProductions.__tablename__.name,
                                                                            id_production))
                else:
                    print(" THE RECORD OF TABLE '{}' HAS NOT BEEN UPDATED".format(LstProductions.__tablename__.name))

            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE UPDATED ".format(LstProductions.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def delete_productions(self, id_production):
        try:
            prod_before: ProductionsDto = self.get_productions_by_id(id_production)
            if Checkers.validate_int(id_production,
                                     LstProductions.id_production.name) and prod_before.id_production is not None:
                self.__session.query(LstProductions).filter(LstProductions.id_production.like(id_production)) \
                    .delete(synchronize_session=False)
                self.__session.commit()
                prod_after: ProductionsDto = self.get_productions_by_id(id_production)
                if prod_before.id_production is not None and prod_after.id_production is None:
                    print("RECORD DELETE IN TABLE '{}' WITH ID '{}'".format(LstProductions.__tablename__.name,
                                                                            id_production))
                else:
                    print(" THE RECORD OF TABLE '{}' WITH ID '{}' HAS NOT BEEN DELETED BECAUSE IT DID NOT EXIST".format(
                        LstProductions.__tablename__.name,
                        id_production))

            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE DELETED".format(LstProductions.__tablename__.name))


        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def get_all_productions(self):
        productions_dto_list = []
        try:
            self.__all_productions: List[ProductionsDto] = self.__session.query(LstProductions).all()
            if len(self.__all_productions) != 0:
                for row in self.__all_productions:
                    prod_aux = create_productions(
                        row.id_production,
                        row.run_number,
                        row.id_run_type,
                        row.r1_check_build,
                        row.dl1a_check_build,
                        row.dl1b_check_build,
                        row.dl2_check_build,
                        row.number_production
                    )
                    productions_dto_list.append(prod_aux)
            else:
                Checkers.empty_list(LstProductions.__tablename__.name)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return productions_dto_list

    def get_productions_by_id(self, id_production):
        try:
            self.__prod_by_id: ProductionsDto = self.__session.query(LstProductions).filter(
                LstProductions.id_production.like(id_production)).first()
            if self.__prod_by_id is not None:
                return create_productions(
                    self.__prod_by_id.id_production,
                    self.__prod_by_id.run_number,
                    self.__prod_by_id.id_run_type,
                    self.__prod_by_id.r1_check_build,
                    self.__prod_by_id.dl1a_check_build,
                    self.__prod_by_id.dl1b_check_build,
                    self.__prod_by_id.dl2_check_build,
                    self.__prod_by_id.number_production
                )
            else:
                Checkers.print_object_filter_null(LstProductions.id_production.name, str(id_production))
                return create_productions(None, None, None, None, None, None, None, None)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return create_productions(None, None, None, None, None, None, None, None)
