from typing import List

from sqlalchemy.exc import InvalidRequestError, OperationalError
from sqlalchemy.orm import Session

from DTO.pixel_information_dto import PixelInformationDto, create_pixel_information
from config.base import getSession
from utils.checkers import Checkers

try:
    from entities.lst_pixel_information import LstPixelInformation
except ImportError as error:
    Checkers.print_exception_one_param(error)


class LstPixelInformationService:

    def __init__(self):
        self.__session: Session = getSession()
        self.__all_pixel_info = None
        self.__pixel_info_by_id = None

    def insert_pixel_info(self, pixel_info_insert: PixelInformationDto):
        try:
            pixel_info_aux = LstPixelInformation(
                pixel_id=pixel_info_insert.pixel_id,
                pixel_group_number=pixel_info_insert.pixel_group_number,
                pixel_pos_x=pixel_info_insert.pixel_pos_x,
                pixel_pos_y=pixel_info_insert.pixel_pos_y,
                pixel_pos_z=pixel_info_insert.pixel_pos_z
            )
            self.__session.add(pixel_info_aux)
            self.__session.commit()
            if pixel_info_aux.id_record is not None:
                pixel_info_insert.id_record = pixel_info_aux.id_record
                print("RECORD INSERTED IN TABLE '{}' WITH ID '{}'".format(LstPixelInformation.__tablename__.name,
                                                                          pixel_info_aux.pixel_id))
            else:
                print(" THE RECORD OF TABLE '{}' HAS NOT BEEN INSERTED".format(LstPixelInformation.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def update_pixel_info(self, id_record, pixel_id_to_search, pixel_group_number_to_search, pixel_id_to_update=None,
                          pixel_group_number_to_update=None, pixel_pos_x=None, pixel_pos_y=None,
                          pixel_pos_z=None):
        try:
            pixel_info_before: PixelInformationDto = self.get_pixel_info_by_id(id_record, pixel_id_to_search,
                                                                               pixel_group_number_to_search)
            if Checkers.validate_int(pixel_id_to_search, LstPixelInformation.pixel_id.name) and \
                    Checkers.validate_int(pixel_group_number_to_search, LstPixelInformation.pixel_group_number.name) and \
                    Checkers.validate_int(id_record, LstPixelInformation.id_record.name) and \
                    pixel_info_before.id_record is not None and \
                    pixel_info_before.pixel_id is not None and \
                    pixel_info_before.pixel_group_number is not None:

                self.__session.query(LstPixelInformation).filter(LstPixelInformation.pixel_id.like(pixel_id_to_search),
                                                                 LstPixelInformation.pixel_group_number.like(
                                                                     pixel_group_number_to_search)) \
                    .update({
                    LstPixelInformation.pixel_id: Checkers.check_field_not_null(
                        LstPixelInformation.pixel_id, pixel_id_to_update),
                    LstPixelInformation.pixel_group_number: Checkers.check_field_not_null(
                        LstPixelInformation.pixel_group_number, pixel_group_number_to_update),
                    LstPixelInformation.pixel_pos_x: Checkers.check_field_not_null(LstPixelInformation.pixel_pos_x,
                                                                                   pixel_pos_x),
                    LstPixelInformation.pixel_pos_y: Checkers.check_field_not_null(LstPixelInformation.pixel_pos_y,
                                                                                   pixel_pos_y),
                    LstPixelInformation.pixel_pos_z: Checkers.check_field_not_null(LstPixelInformation.pixel_pos_z,
                                                                                   pixel_pos_z)
                },
                    synchronize_session=False
                )
                self.__session.commit()
                pixel_info_after: PixelInformationDto = self.get_pixel_info_by_id(id_record,
                                                                                  Checkers.check_field_not_null(
                                                                                      pixel_info_before.pixel_id,
                                                                                      pixel_id_to_update),
                                                                                  Checkers.check_field_not_null(
                                                                                      pixel_info_before.pixel_group_number,
                                                                                      pixel_group_number_to_update))
                if pixel_info_before.__dict__ != pixel_info_after.__dict__:
                    print(
                        "RECORD UPDATE IN TABLE '{}' WITH PIXEL_ID '{}'".format(LstPixelInformation.__tablename__.name,
                                                                                pixel_id_to_search))
                else:
                    print(
                        " THE RECORD OF TABLE '{}' HAS NOT BEEN UPDATED".format(LstPixelInformation.__tablename__.name))

            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE UPDATED ".format(LstPixelInformation.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def delete_pixel_info(self, id_record, pixel_id, pixel_group_number):
        try:
            pixel_info_before: PixelInformationDto = self.get_pixel_info_by_id(id_record, pixel_id,
                                                                               pixel_group_number)
            if Checkers.validate_int(pixel_id, LstPixelInformation.pixel_id.name) and \
                    Checkers.validate_int(pixel_group_number, LstPixelInformation.pixel_group_number.name) and \
                    Checkers.validate_int(id_record, LstPixelInformation.id_record.name) and \
                    pixel_info_before.id_record is not None and \
                    pixel_info_before.pixel_id is not None and \
                    pixel_info_before.pixel_group_number is not None:
                self.__session.query(LstPixelInformation).filter(LstPixelInformation.pixel_id.like(pixel_id),
                                                                 LstPixelInformation.pixel_group_number.like(
                                                                     pixel_group_number)) \
                    .delete(synchronize_session=False)
                self.__session.commit()
                pixel_info_after: PixelInformationDto = self.get_pixel_info_by_id(id_record, pixel_id,
                                                                                  pixel_group_number)
                if pixel_info_before.id_record is not None and \
                        pixel_info_before.pixel_id is not None and \
                        pixel_info_before.pixel_group_number is not None and \
                        pixel_info_after.pixel_id is None and \
                        pixel_info_after.pixel_group_number is None and \
                        pixel_info_after.id_record is None:
                    print("RECORD DELETE IN TABLE '{}' WITH ID '{}'".format(LstPixelInformation.__tablename__.name,
                                                                            pixel_id))
                else:
                    print(" THE RECORD OF TABLE '{}' WITH ID '{}' HAS NOT BEEN DELETED BECAUSE IT DID NOT EXIST".format(
                        LstPixelInformation.__tablename__.name,
                        pixel_id))
            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE DELETED".format(LstPixelInformation.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def get_all_pixel_info(self):
        pixel_info_dto_list = []
        try:
            self.__all_pixel_info: List[PixelInformationDto] = self.__session.query(LstPixelInformation).all()
            if len(self.__all_pixel_info) != 0:
                for row in self.__all_pixel_info:
                    pixel_info_aux = create_pixel_information(
                        row.id_record,
                        row.pixel_id,
                        row.pixel_group_number,
                        row.pixel_pos_x,
                        row.pixel_pos_y,
                        row.pixel_pos_z
                    )
                    pixel_info_dto_list.append(pixel_info_aux)
            else:
                Checkers.empty_list(LstPixelInformation.__tablename__.name)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return pixel_info_dto_list

    def get_pixel_info_by_id(self, id_record, pixel_id, pixel_group_number):
        try:
            self.__pixel_info_by_id: PixelInformationDto = self.__session.query(LstPixelInformation).filter(
                LstPixelInformation.id_record.like(id_record),
                LstPixelInformation.pixel_id.like(pixel_id),
                LstPixelInformation.pixel_group_number.like(pixel_group_number)).first()
            if self.__pixel_info_by_id is not None:
                return create_pixel_information(
                    self.__pixel_info_by_id.id_record,
                    self.__pixel_info_by_id.pixel_id,
                    self.__pixel_info_by_id.pixel_group_number,
                    self.__pixel_info_by_id.pixel_pos_x,
                    self.__pixel_info_by_id.pixel_pos_y,
                    self.__pixel_info_by_id.pixel_pos_z
                )
            else:
                Checkers.print_object_filter_null(
                    LstPixelInformation.pixel_id.name + ", " + LstPixelInformation.pixel_group_number.name,
                    str(pixel_id) + ", " + str(pixel_group_number))
                return create_pixel_information(None, None, None, None, None, None)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return create_pixel_information(None, None, None, None, None, None)
