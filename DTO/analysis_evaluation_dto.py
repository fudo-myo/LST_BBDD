class AnalysisEvaluationDto:
    """
    This class is the transfer object of the `LST_ANALYSIS_EVALUATION` table.

    Attributes
    ----------
    id_analysis_evaluation: int
        primary identifier of the table
    id_lst_r1_data_check_plot: int
        TODO include description
    parameter_description: str
        TODO include description
    parameter_value: double
        TODO include description
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

    Arguments
    ---------

    id_analysis_evaluation: int
        primary identifier of the table
    id_lst_r1_data_check_plot: int
        TODO include description
    parameter_description: str
        TODO include description
    parameter_value: double
        TODO include description

    Returns
    -------
    AnalysisEvaluationDto:
        returns an instance of the transfer object
    """
    dto = AnalysisEvaluationDto()
    dto.id_analysis_evaluation = id_analysis_evaluation
    dto.id_lst_r1_data_check_plot = id_lst_r1_data_check_plot
    dto.parameter_description = parameter_description
    dto.parameter_value = parameter_value
    return dto
