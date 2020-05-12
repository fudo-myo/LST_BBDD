"""
This class is the transfer object of the Analysis Evaluation table,
it contains the following parameters:
:param id_analysis_evaluation: primary identifier of the table
:type Integer
:param id_lst_r1_data_check_plot: TODO include description
:type Integer
:param parameter_description: TODO include description
:type String
:param parameter_value: TODO include description
:type Double
"""


class AnalysisEvaluationDto:
    """
    class constructor that allows instantiating a class object with
    all null attributes
    :return an instance of the class AnalysisEvaluationDto
    """

    def __init__(self, id_analysis_evaluation=None, id_lst_r1_data_check_plot=None, parameter_description=None,
                 parameter_value=None):
        self.__id_analysis_evaluation = id_analysis_evaluation
        self.__id_lst_r1_data_check_plot = id_lst_r1_data_check_plot
        self.__parameter_description = parameter_description
        self.__parameter_value = parameter_value

    @property
    def id_analysis_evaluation(self):
        return self.__id_analysis_evaluation

    @property
    def id_lst_r1_data_check_plot(self):
        return self.__id_lst_r1_data_check_plot

    @property
    def parameter_description(self):
        return self.__parameter_description

    @property
    def parameter_value(self):
        return self.__parameter_value

    @id_analysis_evaluation.setter
    def id_analysis_evaluation(self, value):
        self.__id_analysis_evaluation = value

    @id_lst_r1_data_check_plot.setter
    def id_lst_r1_data_check_plot(self, value):
        self.__id_lst_r1_data_check_plot = value

    @parameter_description.setter
    def parameter_description(self, value):
        self.__parameter_description = value

    @parameter_value.setter
    def parameter_value(self, value):
        self.__parameter_value = value


def create_analysis_evaluation(id_analysis_evaluation, id_lst_r1_data_check_plot, parameter_description,
                               parameter_value):
    """
    This method create a DTO for Analysis Evaluation and set every field with
    the paremeters given as arguments
    :param id_analysis_evaluation: primary identifier of the table
    :param id_lst_r1_data_check_plot: TODO include description
    :param parameter_description: TODO include description
    :param parameter_value: TODO include description

    :return AnalysisEvaluationDto
    """
    dto = AnalysisEvaluationDto()
    dto.id_analysis_evaluation = id_analysis_evaluation
    dto.id_lst_r1_data_check_plot = id_lst_r1_data_check_plot
    dto.parameter_description = parameter_description
    dto.parameter_value = parameter_value
    return dto
