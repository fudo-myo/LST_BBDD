"""
This file contains the service logic
"""
from typing import List

from sqlalchemy.exc import InvalidRequestError, OperationalError
from sqlalchemy.orm import Session

from DTO.dl1a_dto import Dl1aDto, create_dl1a
from config.base import get_session
from utils.checkers import Checkers

try:
    from entities.lst_dl1a import LstDl1a
except ImportError as error:
    Checkers.print_exception_one_param(error)


class LstDl1aService:
    """`LstDl1aService` is a class that contains the service
    logic to manage the data in the `LST_DL1A` table.

    Attributes
    ----------
    self: type
        description
    session: Session
        the Session establishes all conversations with the database
        and represents a “holding zone” for all the objects which you've
        loaded or associated with it during its lifespan. It provides the
        entrypoint to acquire a Query object, which sends queries to the
        database using the Session object's current database connection,
        populating result rows into objects that are then stored in the
        Session, inside a structure called the Identity Map - a data structure
        that maintains unique copies of each object, where "unique" means
        "only one object with a particular primary key".
    all_dl1a: List[Dl1aDto]
        List of transfer objects
    dl1a_by_id: Dl1aDto
        Transfer object
    """
    def __init__(self):
        self.__session: Session = get_session()
        self.__all_dl1a = None
        self.__dl1a_by_id = None

    def insert_dl1a(self, dl1a_insert: Dl1aDto):
        """Method that inserts a record into the `LST_DL1A` table.

        Arguments
        ---------
        dl1a_insert: Dl1aDto
            transfer object
        """
        try:
            dl1a_aux = LstDl1a(subrun_number=dl1a_insert.subrun_number,
                               dl1a_path_file=dl1a_insert.dl1a_path_file)

            self.__session.add(dl1a_aux)
            self.__session.commit()
            if dl1a_aux.id_dl1a is not None:
                dl1a_insert.id_dl1a = dl1a_aux.id_dl1a
                print("RECORD INSERTED IN TABLE '{}' WITH ID '{}'".format(LstDl1a.__tablename__.name,
                                                                          dl1a_aux.id_dl1a))
            else:
                print(" THE RECORD OF TABLE '{}' HAS NOT BEEN INSERTED".format(LstDl1a.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def update_dl1a(self, id_dl1a, subrun_number=None, dl1a_path_file=None):
        """Method that updates a record into the `LST_DL1A` table.

        Arguments
        ---------
        id_dl1a: int
            primary identifier of the table
        subrun_number: int
            subrun number
        dl1a_path_file: str
            dl1a file path
        """
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
        """Method that deletes a record into the `LST_DL1A` table.

        Arguments
        ---------
        id_dl1a: int
            primary identifier of the table
        """
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
        """Method that gets all the records from the `LST_DL1A` table.

        Returns
        -------
        List[Dl1aDto]:
            returns a list of transfer objects
        """
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
        """Method that returns a record from the `LST_DL1A` table.

        Arguments
        -------
        id_dl1a: int
            table primary key

        Returns
        -------
        Dl1aDto:
            returns an instance of the transfer object
        """
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
