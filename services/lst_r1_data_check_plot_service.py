from typing import List

from sqlalchemy.exc import InvalidRequestError, OperationalError
from sqlalchemy.orm import Session

from DTO.r1_data_check_plot_dto import R1DataCheckPlotDto, create_r1_data_check_plot
from config.base import getSession
from utils.checkers import Checkers

try:
    from entities.lst_r1_data_check_plot import LstR1DataCheckPlot
except ImportError as error:
    Checkers.print_exception_one_param(error)


class LstR1DataCheckPlotService:

    def __init__(self):
        self.__session: Session = getSession()
        self.__all_r1_data_check_plot = None
        self.__r1_data_check_plot_by_id = None

    def insert_r1_data_check_plot(self, r1_data_check_plot_insert: R1DataCheckPlotDto):
        try:
            r1_data_check_plot_aux = LstR1DataCheckPlot(
                id_lst_r1_data_check_plot=r1_data_check_plot_insert.id_lst_r1_data_check_plot,
                id_r1_data_check=r1_data_check_plot_insert.id_r1_data_check,
                lst_r1_data_check_plot_path=r1_data_check_plot_insert.lst_r1_data_check_plot_path,
                lst_r1_data_check_plot_description=r1_data_check_plot_insert.lst_r1_data_check_plot_description
            )
            self.__session.add(r1_data_check_plot_aux)
            self.__session.commit()
            if r1_data_check_plot_aux.id_record is not None:
                r1_data_check_plot_insert.id_record = r1_data_check_plot_aux.id_record
                print("RECORD INSERTED IN TABLE '{}' WITH ID '{}'".format(LstR1DataCheckPlot.__tablename__.name,
                                                                          r1_data_check_plot_aux.id_lst_r1_data_check_plot))
            else:
                print(" THE RECORD OF TABLE '{}' HAS NOT BEEN INSERTED".format(LstR1DataCheckPlot.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def update_r1_data_check_plot(self, id_record, id_lst_r1_data_check_plot_to_search,
                                  id_lst_r1_data_check_plot_to_update=None, id_r1_data_check=None,
                                  lst_r1_data_check_plot_path=None,
                                  lst_r1_data_check_plot_description=None):
        try:
            r1_before: R1DataCheckPlotDto = self.get_r1_data_check_plot_by_id(id_record,
                                                                              id_lst_r1_data_check_plot_to_search)
            if Checkers.validate_int(id_lst_r1_data_check_plot_to_search,
                                     LstR1DataCheckPlot.id_lst_r1_data_check_plot.name) and \
                    Checkers.validate_int(id_record, LstR1DataCheckPlot.id_record.name) and \
                    r1_before.id_record is not None and \
                    r1_before.id_lst_r1_data_check_plot is not None:
                self.__session.query(LstR1DataCheckPlot).filter(LstR1DataCheckPlot.id_record.like(id_record)) \
                    .filter(LstR1DataCheckPlot.id_lst_r1_data_check_plot.like(id_lst_r1_data_check_plot_to_search)) \
                    .update({
                    LstR1DataCheckPlot.id_lst_r1_data_check_plot: Checkers.check_field_not_null(
                        LstR1DataCheckPlot.id_lst_r1_data_check_plot, id_lst_r1_data_check_plot_to_update),
                    LstR1DataCheckPlot.id_r1_data_check: Checkers.check_field_not_null(
                        LstR1DataCheckPlot.id_r1_data_check,
                        id_r1_data_check),
                    LstR1DataCheckPlot.lst_r1_data_check_plot_path: Checkers.check_field_not_null(
                        LstR1DataCheckPlot.lst_r1_data_check_plot_path, lst_r1_data_check_plot_path),
                    LstR1DataCheckPlot.lst_r1_data_check_plot_description: Checkers.check_field_not_null(
                        LstR1DataCheckPlot.lst_r1_data_check_plot_description, lst_r1_data_check_plot_description)
                },
                    synchronize_session=False
                )
                self.__session.commit()
                r1_after: R1DataCheckPlotDto = self.get_r1_data_check_plot_by_id(id_record,
                                                                                 Checkers.check_field_not_null(
                                                                                     r1_before.id_lst_r1_data_check_plot,
                                                                                     id_lst_r1_data_check_plot_to_update))
                if r1_before.__dict__ != r1_after.__dict__:
                    print("RECORD UPDATE IN TABLE '{}' WITH ID '{}'".format(LstR1DataCheckPlot.__tablename__.name,
                                                                            id_record))
                else:
                    print(
                        " THE RECORD OF TABLE '{}' HAS NOT BEEN UPDATED".format(LstR1DataCheckPlot.__tablename__.name))

            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE UPDATED ".format(LstR1DataCheckPlot.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def delete_r1_data_check_plot(self, id_record, id_lst_r1_data_check_plot):
        try:
            r1_before: R1DataCheckPlotDto = self.get_r1_data_check_plot_by_id(id_record, id_lst_r1_data_check_plot)
            if Checkers.validate_int(id_lst_r1_data_check_plot, LstR1DataCheckPlot.id_lst_r1_data_check_plot.name) and \
                    Checkers.validate_int(id_record, LstR1DataCheckPlot.id_record.name) and \
                    r1_before.id_record is not None and \
                    r1_before.id_lst_r1_data_check_plot is not None:
                self.__session.query(LstR1DataCheckPlot).filter(
                    LstR1DataCheckPlot.id_lst_r1_data_check_plot.like(id_lst_r1_data_check_plot)) \
                    .delete(synchronize_session=False)
                self.__session.commit()
                r1_after: R1DataCheckPlotDto = self.get_r1_data_check_plot_by_id(id_record, id_lst_r1_data_check_plot)
                if r1_before.id_record is not None and \
                        r1_before.id_lst_r1_data_check_plot is not None and \
                        r1_after.id_lst_r1_data_check_plot is None and \
                        r1_after.id_record is None:
                    print("RECORD DELETE IN TABLE '{}' WITH ID '{}'".format(LstR1DataCheckPlot.__tablename__.name,
                                                                            id_lst_r1_data_check_plot))
                else:
                    print(" THE RECORD OF TABLE '{}' WITH ID '{}' HAS NOT BEEN DELETED BECAUSE IT DID NOT EXIST".format(
                        LstR1DataCheckPlot.__tablename__.name,
                        id_lst_r1_data_check_plot))
            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE DELETED".format(LstR1DataCheckPlot.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def get_all_r1_data_check_plot(self):
        r1_data_check_plot_dto_list = []
        try:
            self.__all_r1_data_check_plot: List[R1DataCheckPlotDto] = self.__session.query(LstR1DataCheckPlot).all()
            if len(self.__all_r1_data_check_plot) != 0:
                for row in self.__all_r1_data_check_plot:
                    r1_aux = create_r1_data_check_plot(
                        row.id_record,
                        row.id_lst_r1_data_check_plot,
                        row.id_r1_data_check,
                        row.lst_r1_data_check_plot_path,
                        row.lst_r1_data_check_plot_description
                    )
                    r1_data_check_plot_dto_list.append(r1_aux)
            else:
                Checkers.empty_list(LstR1DataCheckPlot.__tablename__.name)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return r1_data_check_plot_dto_list

    def get_r1_data_check_plot_by_id(self, id_record, id_lst_r1_data_check_plot):
        try:
            self.__r1_data_check_plot_by_id: R1DataCheckPlotDto = self.__session.query(LstR1DataCheckPlot).filter(
                LstR1DataCheckPlot.id_lst_r1_data_check_plot.like(id_lst_r1_data_check_plot),
                LstR1DataCheckPlot.id_record.like(id_record)).first()
            if self.__r1_data_check_plot_by_id is not None:
                return create_r1_data_check_plot(
                    self.__r1_data_check_plot_by_id.id_record,
                    self.__r1_data_check_plot_by_id.id_lst_r1_data_check_plot,
                    self.__r1_data_check_plot_by_id.id_r1_data_check,
                    self.__r1_data_check_plot_by_id.lst_r1_data_check_plot_path,
                    self.__r1_data_check_plot_by_id.lst_r1_data_check_plot_description
                )
            else:
                Checkers.print_object_filter_null(LstR1DataCheckPlot.id_lst_r1_data_check_plot.name,
                                                  str(id_lst_r1_data_check_plot))
                return create_r1_data_check_plot(None, None, None, None, None)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return create_r1_data_check_plot(None, None, None, None, None)
