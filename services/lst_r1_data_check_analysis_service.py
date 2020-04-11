from typing import List

from sqlalchemy.exc import InvalidRequestError, OperationalError
from sqlalchemy.orm import Session

from DTO.r1_data_check_analysis_dto import R1DataCheckAnalysisDto, create_r1_data_check_analysis
from config.base import getSession
from utils.checkers import Checkers

try:
    from entities.lst_r1_data_check_analysis import LstR1DataCheckAnalysis
except ImportError as error:
    Checkers.print_exception_one_param(error)


class LstR1DataCheckAnalysisService:

    def __init__(self):
        self.__session: Session = getSession()
        self.__all_r1_data_check_analysis = None
        self.__r1_data_check_analysis_by_id = None

    def insert_r1_data_check_analysis(self, r1_data_check_anaylis_insert: R1DataCheckAnalysisDto):
        try:
            r1_data_check_anaylis_aux = LstR1DataCheckAnalysis(
                id_r1_data_check=r1_data_check_anaylis_insert.id_r1_data_check,
                run_number=r1_data_check_anaylis_insert.run_number,
                id_r1_data_check_specific=r1_data_check_anaylis_insert.id_r1_data_check_specific
            )
            self.__session.add(r1_data_check_anaylis_aux)
            self.__session.commit()
            if r1_data_check_anaylis_aux.id_record is not None:
                r1_data_check_anaylis_insert.id_record = r1_data_check_anaylis_aux.id_record
                print("RECORD INSERTED IN TABLE '{}' WITH ID '{}'".format(LstR1DataCheckAnalysis.__tablename__.name,
                                                                          r1_data_check_anaylis_aux.id_r1_data_check))
            else:
                print(
                    " THE RECORD OF TABLE '{}' HAS NOT BEEN INSERTED".format(LstR1DataCheckAnalysis.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def update_r1_data_check_analysis(self, id_record, id_r1_data_check_to_search, id_r1_data_check_to_update=None,
                                      run_number=None, id_r1_data_check_specific=None):
        try:
            r1_before: R1DataCheckAnalysisDto = self.get_r1_data_check_analysis_by_id(id_record,
                                                                                      id_r1_data_check_to_search)
            if Checkers.validate_int(id_r1_data_check_to_search, LstR1DataCheckAnalysis.id_r1_data_check.name) and \
                    Checkers.validate_int(id_record, LstR1DataCheckAnalysis.id_record.name) and \
                    r1_before.id_record is not None and \
                    r1_before.id_r1_data_check is not None:
                self.__session.query(LstR1DataCheckAnalysis) \
                    .filter(LstR1DataCheckAnalysis.id_r1_data_check.like(r1_before.id_r1_data_check),
                            LstR1DataCheckAnalysis.id_record.like(r1_before.id_record)) \
                    .update({
                    LstR1DataCheckAnalysis.id_r1_data_check: Checkers.check_field_not_null(
                        LstR1DataCheckAnalysis.id_r1_data_check, id_r1_data_check_to_update),
                    LstR1DataCheckAnalysis.run_number: Checkers.check_field_not_null(LstR1DataCheckAnalysis.run_number,
                                                                                     run_number),
                    LstR1DataCheckAnalysis.id_r1_data_check_specific: Checkers.check_field_not_null(
                        LstR1DataCheckAnalysis.id_r1_data_check_specific, id_r1_data_check_specific)

                },
                    synchronize_session=False
                )
                self.__session.commit()
                r1_after: R1DataCheckAnalysisDto = self.get_r1_data_check_analysis_by_id(id_record,
                                                                                         id_r1_data_check_to_search)
                if r1_before.__dict__ != r1_after.__dict__:
                    print("RECORD UPDATE IN TABLE '{}' WITH ID '{}'".format(LstR1DataCheckAnalysis.__tablename__.name,
                                                                            id_r1_data_check_to_search))
                else:
                    print(" THE RECORD OF TABLE '{}' HAS NOT BEEN UPDATED".format(
                        LstR1DataCheckAnalysis.__tablename__.name))

            else:
                print(
                    " THE RECORD OF TABLE '{}' COULD NOT BE UPDATED ".format(LstR1DataCheckAnalysis.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def delete_r1_data_check_analysis(self, id_record, id_r1_data_check):
        try:
            r1_before: R1DataCheckAnalysisDto = self.get_r1_data_check_analysis_by_id(id_record, id_r1_data_check)
            if Checkers.validate_int(id_r1_data_check, LstR1DataCheckAnalysis.id_r1_data_check.name) and \
                    Checkers.validate_int(id_record, LstR1DataCheckAnalysis.id_record.name) and \
                    r1_before.id_record is not None and \
                    r1_before.id_r1_data_check is not None:
                self.__session.query(LstR1DataCheckAnalysis).filter(
                    LstR1DataCheckAnalysis.id_r1_data_check.like(id_r1_data_check)) \
                    .delete(synchronize_session=False)
                self.__session.commit()
                r1_after: R1DataCheckAnalysisDto = self.get_r1_data_check_analysis_by_id(id_record, id_r1_data_check)
                if r1_before.id_r1_data_check is not None and\
                        r1_before.id_record is not None and \
                        r1_after. id_record is None and \
                        r1_after.id_r1_data_check is None:
                    print("RECORD DELETE IN TABLE '{}' WITH ID '{}'".format(LstR1DataCheckAnalysis.__tablename__.name,
                                                                            id_r1_data_check))
                else:
                    print(" THE RECORD OF TABLE '{}' WITH ID '{}' HAS NOT BEEN DELETED BECAUSE IT DID NOT EXIST".format(
                        LstR1DataCheckAnalysis.__tablename__.name,
                        id_r1_data_check))
            else:
                print(
                    " THE RECORD OF TABLE '{}' COULD NOT BE DELETED".format(LstR1DataCheckAnalysis.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def get_all_r1_data_check_analysis(self):
        r1_data_check_analysis_dto_list = []
        try:
            self.__all_r1_data_check_analysis: List[R1DataCheckAnalysisDto] = self.__session.query(
                LstR1DataCheckAnalysis).all()
            if len(self.__all_r1_data_check_analysis) != 0:
                for row in self.__all_r1_data_check_analysis:
                    r1_aux = create_r1_data_check_analysis(
                        row.id_record,
                        row.id_r1_data_check,
                        row.run_number,
                        row.id_r1_data_check_specific
                    )
                    r1_data_check_analysis_dto_list.append(r1_aux)
            else:
                Checkers.empty_list(LstR1DataCheckAnalysis.__tablename__.name)
        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return r1_data_check_analysis_dto_list

    def get_r1_data_check_analysis_by_id(self, id_record, id_r1_data_check):
        try:
            self.__r1_data_check_analysis_by_id: R1DataCheckAnalysisDto = self.__session.query(
                LstR1DataCheckAnalysis).filter(LstR1DataCheckAnalysis.id_r1_data_check.like(id_r1_data_check),
                                               LstR1DataCheckAnalysis.id_record.like(id_record)).first()
            if self.__r1_data_check_analysis_by_id is not None:
                return create_r1_data_check_analysis(
                    self.__r1_data_check_analysis_by_id.id_record,
                    self.__r1_data_check_analysis_by_id.id_r1_data_check,
                    self.__r1_data_check_analysis_by_id.run_number,
                    self.__r1_data_check_analysis_by_id.id_r1_data_check_specific
                )
            else:
                Checkers.print_object_filter_null(LstR1DataCheckAnalysis.id_r1_data_check.name, str(id_r1_data_check))
                return create_r1_data_check_analysis(None, None, None, None)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return create_r1_data_check_analysis(None, None, None, None)
