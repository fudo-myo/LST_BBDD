from typing import List

from sqlalchemy.exc import InvalidRequestError, OperationalError
from sqlalchemy.orm import sessionmaker, Session

from DTO.run_type_dto import RunTypeDto, create_run_type
from config.base import get_session
from utils.checkers import Checkers

try:
    from entities.lst_run_type import LstRunType
except ImportError as error:
    Checkers.print_exception_one_param(error)


class LstRunTypeService:

    def __init__(self):
        self.__session: Session = get_session()
        self.__all_run_type = None
        self.__run_type_by_id = None

    def insert_run_type(self, run_type_insert: RunTypeDto):
        try:
            run_type_aux = LstRunType(
                description_run_type=run_type_insert.description_run_type
            )
            self.__session.add(run_type_aux)
            self.__session.commit()
            if run_type_aux.id_run_type is not None:
                run_type_insert.id_run_type = run_type_aux.id_run_type
                print("RECORD INSERTED IN TABLE '{}' WITH ID '{}'".format(LstRunType.__tablename__.name,
                                                                          run_type_aux.id_run_type))
            else:
                print(" THE RECORD OF TABLE '{}' HAS NOT BEEN INSERTED".format(LstRunType.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def update_run_type(self, id_run_type, description_run_type=None):
        try:
            run_type_before: RunTypeDto = self.get_run_type_by_id(id_run_type)
            if Checkers.validate_int(id_run_type,
                                     LstRunType.id_run_type.name) and run_type_before.id_run_type is not None:
                self.__session.query(LstRunType).filter(LstRunType.id_run_type.like(id_run_type)) \
                    .update({
                    LstRunType.description_run_type: Checkers.check_field_not_null(LstRunType.description_run_type,
                                                                                   description_run_type)
                },
                    synchronize_session=False
                )
                self.__session.commit()
                run_type_after: RunTypeDto = self.get_run_type_by_id(id_run_type)
                if run_type_before.__dict__ != run_type_after.__dict__:
                    print(" RECORD UPDATED IN TABLE '{}' WITH ID '{}' ".format(LstRunType.__tablename__.name,
                                                                               id_run_type))
                else:
                    print(" THE RECORD OF TABLE '{}' HAS NOT BEEN UPDATED".format(LstRunType.__tablename__.name))

            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE UPDATED ".format(LstRunType.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def delete_run_type(self, id_run_type):
        try:
            run_type_before: RunTypeDto = self.get_run_type_by_id(id_run_type)
            if Checkers.validate_int(id_run_type,
                                     LstRunType.id_run_type.name) and run_type_before.id_run_type is not None:

                self.__session.query(LstRunType).filter(LstRunType.id_run_type.like(id_run_type)) \
                    .delete(synchronize_session=False)
                self.__session.commit()
                run_type_after: RunTypeDto = self.get_run_type_by_id(id_run_type)
                if run_type_before.id_run_type is not None and run_type_after.id_run_type is None:
                    print("RECORD DELETE IN TABLE '{}' WITH ID '{}'".format(LstRunType.__tablename__.name,
                                                                            id_run_type))
                else:
                    print(" THE RECORD OF TABLE '{}' WITH ID '{}' HAS NOT BEEN DELETED BECAUSE IT DID NOT EXIST".format(
                        LstRunType.__tablename__.name,
                        id_run_type))
            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE DELETED".format(LstRunType.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def get_all_run_type(self):
        run_type_dto_list = []
        try:
            self.__all_run_type: List[RunTypeDto] = self.__session.query(LstRunType).all()
            if len(self.__all_run_type) != 0:
                for row in self.__all_run_type:
                    run_type_aux = create_run_type(
                        row.id_run_type,
                        row.description_run_type
                    )
                    run_type_dto_list.append(run_type_aux)
            else:
                Checkers.empty_list(LstRunType.__tablename__.name)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return run_type_dto_list

    def get_run_type_by_id(self, id_run_type):
        try:
            self.__run_type_by_id: RunTypeDto = self.__session.query(LstRunType).filter(
                LstRunType.id_run_type.like(id_run_type)).first()
            if self.__run_type_by_id is not None:
                return create_run_type(
                    self.__run_type_by_id.id_run_type,
                    self.__run_type_by_id.description_run_type
                )
            else:
                Checkers.print_object_filter_null(LstRunType.id_run_type.name, str(id_run_type))
                return create_run_type(None, None)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return create_run_type(None, None)
