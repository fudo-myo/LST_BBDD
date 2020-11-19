from typing import List

from sqlalchemy.exc import InvalidRequestError, OperationalError
from sqlalchemy.orm import Session

from DTO.qp_data_dto import QpDataDto, create_qp_data
from config.base import get_session
from utils.checkers import Checkers

try:
    from entities.lst_qp_data import LstQpData
except ImportError as error:
    Checkers.print_exception_one_param(error)


class LstQpDataService:

    def __init__(self):
        self.__session: Session = get_session()
        self.__all_qp_data = None
        self.__qp_data_by_id = None

    def insert_qp_data(self, qp_data_insert: QpDataDto):
        try:
            qp_data_aux = LstQpData(
                pixel_id=qp_data_insert.pixel_id,
                id_dl1a=qp_data_insert.id_dl1a,
                q_average=qp_data_insert.q_average,
                q_rms=qp_data_insert.q_rms,
                time_average=qp_data_insert.time_average,
                time_rms=qp_data_insert.time_rms,
                dl1a_check_build=qp_data_insert.dl1a_check_build
            )
            self.__session.add(qp_data_aux)
            self.__session.commit()
            if qp_data_aux.id_qp_data is not None:
                qp_data_insert.id_qp_data = qp_data_aux.id_qp_data
                print("RECORD INSERTED IN TABLE '{}' WITH ID '{}'".format(LstQpData.__tablename__.name,
                                                                          qp_data_aux.id_qp_data))
            else:
                print(" THE RECORD OF TABLE '{}' HAS NOT BEEN INSERTED".format(LstQpData.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def update_qp_data(self, id_qp_data, pixel_id=None, id_dl1a=None, q_average=None, q_rms=None, time_average=None,
                       time_rms=None, dl1a_check_build=None):
        try:
            qp_before: QpDataDto = self.get_qp_data_by_id(id_qp_data)
            if Checkers.validate_int(id_qp_data, LstQpData.id_qp_data.name) and qp_before.id_qp_data is not None:
                self.__session.query(LstQpData).filter(LstQpData.id_qp_data.like(id_qp_data)) \
                    .update({
                    LstQpData.pixel_id: Checkers.check_field_not_null(LstQpData.pixel_id, pixel_id),
                    LstQpData.id_dl1a: Checkers.check_field_not_null(LstQpData.id_dl1a, id_dl1a),
                    LstQpData.q_average: Checkers.check_field_not_null(LstQpData.q_average, q_average),
                    LstQpData.q_rms: Checkers.check_field_not_null(LstQpData.q_rms, q_rms),
                    LstQpData.time_average: Checkers.check_field_not_null(LstQpData.time_average, time_average),
                    LstQpData.time_rms: Checkers.check_field_not_null(LstQpData.time_rms, time_rms),
                    LstQpData.dl1a_check_build: Checkers.check_field_not_null(LstQpData.dl1a_check_build,
                                                                              dl1a_check_build)
                },
                    synchronize_session=False
                )
                self.__session.commit()
                qp_after: QpDataDto = self.get_qp_data_by_id(id_qp_data)
                if qp_before.__dict__ != qp_after.__dict__:
                    print("RECORD UPDATE IN TABLE '{}' WITH ID '{}'".format(LstQpData.__tablename__.name,
                                                                            id_qp_data))
                else:
                    print(" THE RECORD OF TABLE '{}' HAS NOT BEEN UPDATED".format(LstQpData.__tablename__.name))
            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE UPDATED ".format(LstQpData.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def delete_qp_data(self, id_qp_data):
        try:
            qp_before: QpDataDto = self.get_qp_data_by_id(id_qp_data)
            if Checkers.validate_int(id_qp_data, LstQpData.id_qp_data.name) and qp_before.id_qp_data is not None:
                self.__session.query(LstQpData).filter(LstQpData.id_qp_data.like(id_qp_data)) \
                    .delete(synchronize_session=False)
                self.__session.commit()
                qp_after: QpDataDto = self.get_qp_data_by_id(id_qp_data)
                if qp_before.id_qp_data is not None and qp_after.id_qp_data is None:
                    print("RECORD DELETE IN TABLE '{}' WITH ID '{}'".format(LstQpData.__tablename__.name,
                                                                            id_qp_data))
                else:
                    print(" THE RECORD OF TABLE '{}' WITH ID '{}' HAS NOT BEEN DELETED BECAUSE IT DID NOT EXIST".format(
                        LstQpData.__tablename__.name,
                        id_qp_data))
            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE DELETED".format(LstQpData.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def get_all_qp_data(self):
        qp_data_dto_list = []
        try:
            self.__all_qp_data: List[QpDataDto] = self.__session.query(LstQpData).all()
            if len(self.__all_qp_data) != 0:
                for row in self.__all_qp_data:
                    qp_data_aux = create_qp_data(
                        row.id_qp_data,
                        row.pixel_id,
                        row.id_dl1a,
                        row.q_average,
                        row.q_rms,
                        row.time_average,
                        row.time_rms,
                        row.dl1a_check_build
                    )
                    qp_data_dto_list.append(qp_data_aux)
            else:
                Checkers.empty_list(LstQpData.__tablename__.name)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return qp_data_dto_list

    def get_qp_data_by_id(self, id_qp_data):
        try:
            self.__qp_data_by_id: QpDataDto = self.__session.query(LstQpData).filter(
                LstQpData.id_qp_data.like(id_qp_data)).first()
            if self.__qp_data_by_id is not None:
                return create_qp_data(
                    self.__qp_data_by_id.id_qp_data,
                    self.__qp_data_by_id.pixel_id,
                    self.__qp_data_by_id.id_dl1a,
                    self.__qp_data_by_id.q_average,
                    self.__qp_data_by_id.q_rms,
                    self.__qp_data_by_id.time_average,
                    self.__qp_data_by_id.time_rms,
                    self.__qp_data_by_id.dl1a_check_build
                )
            else:
                Checkers.print_object_filter_null(LstQpData.id_qp_data.name, str(id_qp_data))
                return create_qp_data(None, None, None, None, None, None, None, None)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return create_qp_data(None, None, None, None, None, None, None, None)
