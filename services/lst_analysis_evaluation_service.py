from typing import List

from sqlalchemy.exc import InvalidRequestError, OperationalError
from sqlalchemy.orm import Session

from DTO.analysis_evaluation_dto import create_analysis_evaluation, AnalysisEvaluationDto
from config.base import getSession
from utils.checkers import Checkers

try:
    from entities.lst_analysis_evaluation import LstAnalysisEvaluation
except ImportError as error:
    Checkers.print_exception_one_param(error)


class LstAnalysisEvaluationService:

    def __init__(self):
        self.__session: Session = getSession()
        self.__all_analysis_eval = None
        self.__analysis_by_id = None

    def insert_analysis_eval(self, analysis_eval_insert: AnalysisEvaluationDto):
        try:
            analysis_eval_aux = LstAnalysisEvaluation(
                id_lst_r1_data_check_plot=analysis_eval_insert.id_lst_r1_data_check_plot,
                parameter_description=analysis_eval_insert.parameter_description,
                parameter_value=analysis_eval_insert.parameter_value
            )
            self.__session.add(analysis_eval_aux)
            self.__session.commit()
            if analysis_eval_aux.id_analysis_evaluation is not None:
                analysis_eval_insert.id_analysis_evaluation = analysis_eval_aux.id_analysis_evaluation
                print("RECORD INSERTED IN TABLE '{}' WITH ID '{}'".format(LstAnalysisEvaluation.__tablename__.name,
                                                                          analysis_eval_aux.id_analysis_evaluation))
            else:
                print(
                    " THE RECORD OF TABLE '{}' HAS NOT BEEN INSERTED".format(LstAnalysisEvaluation.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def update_analysis_eval(self, id_analysis_evaluation, id_lst_r1_data_check_plot=None, parameter_description=None,
                             parameter_value=None):
        try:
            analysis_dto_before: AnalysisEvaluationDto = self.get_analysis_by_id(id_analysis_evaluation)
            if Checkers.validate_int(id_analysis_evaluation,
                                     LstAnalysisEvaluation.id_analysis_evaluation) and analysis_dto_before.id_analysis_evaluation is not None:
                self.__session.query(LstAnalysisEvaluation).filter(
                    LstAnalysisEvaluation.id_analysis_evaluation.like(id_analysis_evaluation)) \
                    .update({
                    LstAnalysisEvaluation.id_lst_r1_data_check_plot: Checkers.check_field_not_null(
                        LstAnalysisEvaluation.id_lst_r1_data_check_plot, id_lst_r1_data_check_plot),
                    LstAnalysisEvaluation.parameter_description: Checkers.check_field_not_null(
                        LstAnalysisEvaluation.parameter_description, parameter_description),
                    LstAnalysisEvaluation.parameter_value: Checkers.check_field_not_null(
                        LstAnalysisEvaluation.parameter_value,
                        parameter_value)},
                    synchronize_session=False
                )
                self.__session.commit()
                analysis_dto_after: AnalysisEvaluationDto = self.get_analysis_by_id(id_analysis_evaluation)
                if analysis_dto_before.__dict__ != analysis_dto_after.__dict__:
                    print("RECORD UPDATE IN TABLE '{}' WITH ID '{}'".format(LstAnalysisEvaluation.__tablename__.name,
                                                                            id_analysis_evaluation))
                else:
                    print(" THE RECORD OF TABLE '{}' HAS NOT BEEN UPDATED".format(
                        LstAnalysisEvaluation.__tablename__.name))
            else:
                print(
                    " THE RECORD OF TABLE '{}' COULD NOT BE UPDATED ".format(LstAnalysisEvaluation.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def delete_analysis_eval(self, id_analysis_evaluation):
        try:
            analysis_dto_before: AnalysisEvaluationDto = self.get_analysis_by_id(id_analysis_evaluation)
            if Checkers.validate_int(id_analysis_evaluation,
                                     LstAnalysisEvaluation.id_analysis_evaluation) and analysis_dto_before.id_analysis_evaluation is not None:
                self.__session.query(LstAnalysisEvaluation).filter(
                    LstAnalysisEvaluation.id_analysis_evaluation.like(id_analysis_evaluation)) \
                    .delete(synchronize_session=False)
                self.__session.commit()
                analysis_dto_after: AnalysisEvaluationDto = self.get_analysis_by_id(id_analysis_evaluation)
                if analysis_dto_before.id_analysis_evaluation is not None and analysis_dto_after.id_analysis_evaluation is None:
                    print("RECORD DELETE IN TABLE '{}' WITH ID '{}'".format(LstAnalysisEvaluation.__tablename__.name,
                                                                            id_analysis_evaluation))
                else:
                    print(" THE RECORD OF TABLE '{}' WITH ID '{}' HAS NOT BEEN DELETED BECAUSE IT DID NOT EXIST".format(
                        LstAnalysisEvaluation.__tablename__.name,
                        id_analysis_evaluation))
            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE DELETED".format(LstAnalysisEvaluation.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def get_all_analysis_eval(self):
        analysis_evaluation_dto_list = []
        try:
            self.__all_analysis_eval: List[AnalysisEvaluationDto] = self.__session.query(LstAnalysisEvaluation).all()
            if len(self.__all_analysis_eval) != 0:
                for row in self.__all_analysis_eval:
                    analysis_eval_aux = create_analysis_evaluation(
                        row.id_analysis_evaluation,
                        row.id_lst_r1_data_check_plot,
                        row.parameter_description,
                        row.parameter_value
                    )
                    analysis_evaluation_dto_list.append(analysis_eval_aux)
            else:
                Checkers.empty_list(LstAnalysisEvaluation.__tablename__.name)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return analysis_evaluation_dto_list

    def get_analysis_by_id(self, id_analysis_evaluation):
        try:
            self.__analysis_by_id: AnalysisEvaluationDto = self.__session.query(LstAnalysisEvaluation).filter(
                LstAnalysisEvaluation.id_analysis_evaluation.like(id_analysis_evaluation)).first()
            if self.__analysis_by_id is not None:
                return create_analysis_evaluation(
                    self.__analysis_by_id.id_analysis_evaluation,
                    self.__analysis_by_id.id_lst_r1_data_check_plot,
                    self.__analysis_by_id.parameter_description,
                    self.__analysis_by_id.parameter_value)
            else:
                Checkers.print_object_filter_null(LstAnalysisEvaluation.id_analysis_evaluation.name,
                                                  str(id_analysis_evaluation))
                return create_analysis_evaluation(None, None, None, None)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return create_analysis_evaluation(None, None, None, None)
