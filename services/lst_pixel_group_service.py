from typing import List

from sqlalchemy.exc import InvalidRequestError, OperationalError
from sqlalchemy.orm import Session

from DTO.pixel_group_dto import PixelGroupDto, create_pixel_group
from config.base import getSession
from utils.checkers import Checkers

try:
    from entities.lst_pixel_group import LstPixelGroup
except ImportError as error:
    Checkers.print_exception_one_param(error)


class LstPixelGroupService:

    def __init__(self):
        self.__session: Session = getSession()
        self.__all_pixel_group = None
        self.__pixel_group_by_id = None

    def insert_pixel_group(self, pixel_group_insert: PixelGroupDto):
        try:
            pixel_group_aux = LstPixelGroup(
                pixel_group_number=pixel_group_insert.pixel_group_number,
                id_config=pixel_group_insert.id_config,
                other_data=pixel_group_insert.other_data
            )
            self.__session.add(pixel_group_aux)
            self.__session.commit()
            if pixel_group_aux.id_config is not None:
                print("RECORD INSERTED IN TABLE '{}' WITH ID '{}'".format(LstPixelGroup.__tablename__.name,
                                                                          pixel_group_aux.pixel_group_number))
            else:
                print(" THE RECORD OF TABLE '{}' HAS NOT BEEN INSERTED".format(LstPixelGroup.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def update_pixel_group(self, id_config, pixel_group_number_to_search, pixel_group_number_to_update=None,
                           id_pixel_group=None, other_data=None):
        try:
            pixel_group_before: PixelGroupDto = self.__pixel_group_by_id(pixel_group_number_to_search, id_config)
            if Checkers.validate_int(id_config, LstPixelGroup.id_config.name) and Checkers.validate_int(
                    pixel_group_number_to_search,
                    LstPixelGroup.pixel_group_number.name) and pixel_group_before.id_config is not None and pixel_group_before.pixel_group_number is not None:
                self.__session.query(LstPixelGroup).filter(LstPixelGroup.id_config.like(id_config),
                                                           LstPixelGroup.pixel_group_number.like(
                                                               pixel_group_number_to_search)) \
                    .update({
                    LstPixelGroup.pixel_group_number_to_update: Checkers.check_field_not_null(
                        LstPixelGroup.pixel_group_number_to_update, pixel_group_number_to_update),
                    LstPixelGroup.id_config: Checkers.check_field_not_null(LstPixelGroup.id_config, id_config),
                    LstPixelGroup.other_data: Checkers.check_field_not_null(LstPixelGroup.other_data, other_data)
                },
                    synchronize_session=False
                )
                self.__session.commit()
                pixel_group_after: PixelGroupDto = self.get_pixel_group_by_id(pixel_group_number_to_search, id_config)
                if pixel_group_before.__dict__ != pixel_group_after.__dict__:
                    print("RECORD UPDATE IN TABLE '{}' WITH ID '{}'".format(LstPixelGroup.__tablename__.name,
                                                                            id_pixel_group))
                else:
                    print(" THE RECORD OF TABLE '{}' HAS NOT BEEN UPDATED".format(LstPixelGroup.__tablename__.name))

            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE UPDATED ".format(LstPixelGroup.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def delete_pixel_group(self, id_config, pixel_group_number):
        try:
            pixel_group_before: PixelGroupDto = self.get_pixel_group_by_id(pixel_group_number, id_config)
            if Checkers.validate_int(id_config, LstPixelGroup.id_config.name) and Checkers.validate_int(
                    pixel_group_number,
                    LstPixelGroup.pixel_group_number.name) and pixel_group_before.id_config is not None and pixel_group_before.pixel_group_number is not None:
                self.__session.query(LstPixelGroup).filter(LstPixelGroup.id_pixel_group.like(id_config),
                                                           LstPixelGroup.pixel_group_number.like(pixel_group_number)) \
                    .delete(synchronize_session=False)
                self.__session.commit()
                pixel_group_after: PixelGroupDto = self.get_pixel_group_by_id(pixel_group_number, id_config)
                if pixel_group_before.id_pixel_group is not None and pixel_group_after.id_pixel_group is None:
                    print("RECORD DELETE IN TABLE '{}' WITH ID '{}'".format(LstPixelGroup.__tablename__.name,
                                                                            pixel_group_before.id_pixel_group))
                else:
                    print(" THE RECORD OF TABLE '{}' WITH ID '{}' HAS NOT BEEN DELETED BECAUSE IT DID NOT EXIST".format(
                        LstPixelGroup.__tablename__.name,
                        id_config))
            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE DELETED".format(LstPixelGroup.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def get_all_pixel_group(self):
        pixel_group_dto_list = []
        try:
            self.__all_pixel_group: List[PixelGroupDto] = self.__session.query(LstPixelGroup).all()
            if len(self.__all_pixel_group) != 0:
                for row in self.__all_pixel_group:
                    pixel_group_aux = create_pixel_group(
                        row.id_pixel_group,
                        row.pixel_group_number,
                        row.id_config,
                        row.other_data
                    )
                    pixel_group_dto_list.append(pixel_group_aux)
            else:
                Checkers.empty_list(LstPixelGroup.__tablename__.name)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return pixel_group_dto_list

    def get_pixel_group_by_id(self, pixel_group_number, id_config):
        try:
            self.__pixel_group_by_id: PixelGroupDto = self.__session.query(LstPixelGroup).filter(
                LstPixelGroup.id_config.like(id_config),
                LstPixelGroup.pixel_group_number.like(pixel_group_number)).first()
            if self.__pixel_group_by_id is not None:
                return create_pixel_group(
                    self.__pixel_group_by_id.id_pixel_group,
                    self.__pixel_group_by_id.pixel_group_number,
                    self.__pixel_group_by_id.id_config,
                    self.__pixel_group_by_id.other_data
                )
            else:
                Checkers.print_object_filter_null(
                    LstPixelGroup.pixel_group_number.name + ", " + LstPixelGroup.id_config.name,
                    str(pixel_group_number) + ", " + str(id_config))
                return create_pixel_group(None, None, None, None)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return create_pixel_group(None, None, None, None)
