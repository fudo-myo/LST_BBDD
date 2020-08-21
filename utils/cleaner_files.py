import re
from datetime import datetime
from typing import List


class CleanerFiles:
    """
        This method returns only the night summary files from year to compare
        to current year
    """

    @staticmethod
    def get_night_summary_files_current_year(night_summary_files, year_to_compare):
        night_summary_cleaned = []
        for ns_file in night_summary_files:
            year = int(ns_file[ns_file.index("NightSummary_") + len("NightSummary_"):len("NightSummary_") + 4])
            if year >= year_to_compare:
                night_summary_cleaned.append(ns_file)

        return night_summary_cleaned

    """
        This method returns only the basic and standard files from year to compare
        to current year
    """

    @staticmethod
    def get_basic_and_standard_files_current_year(basic_files, basic_or_standard, year_to_compare):
        basic_files_cleaned = []
        for bs_or_st_file in basic_files:
            if basic_or_standard in bs_or_st_file:
                year = int(bs_or_st_file[bs_or_st_file.index("RUNs_FROM_") + len("RUNs_FROM_"):len("RUNs_FROM_") + 4])
                if year >= year_to_compare:
                    basic_files_cleaned.append(bs_or_st_file)

        return basic_files_cleaned

    """
        This method converts the 'nan' to None so there is no problem
        in the constructors of the DTO classes
    """

    @staticmethod
    def nan_to_none(list_element):
        for element in list_element:
            if element == 'nan':
                list_element[list_element.index(element)] = None

    """
        This method checks that all the lines are the same length and
        adds None until it is the correct length so that it does not
        fail in the constructor of the DTO class
    """

    @staticmethod
    def check_list_dimensions(list_element, length):
        while len(list_element) < length:
            list_element.append(None)

    """
        This method removes the header and footer of the basic file since
        they are not inserted in the table
    """

    @staticmethod
    def clean_header_and_footer(lines):
        lines_cleaned = []
        for element in lines:
            print(element)
            if not 'Date' in element and \
                    not '(YYYY-MM-DD HH:mm:ss)' in element and \
                    not 'TOTAL' in element and \
                    not 'S=Stereo' in element and \
                    not 'C=Calibration' in element and \
                    not 'P=Pedestal' in element and \
                    not 'U=Unknown' in element:
                lines_cleaned.append(element)

        return lines_cleaned

    """
        this method obtains the elements referred to the event type
        and concatenates them from the Night Summary files
    """

    @staticmethod
    def check_event_type(clean_list, length):
        event_type = ""
        if len(clean_list) > length:
            for element in range(len(clean_list) - length):
                event_type = event_type + clean_list[element + length] + " "

        return event_type

    """
        This method obtains the elements referred to the event type
        and concatenates them from the standard files
    """

    @staticmethod
    def check_event_type_standard_file(clean_list, index_start):
        event_type = None
        if clean_list[index_start] is not None:
            event_type = ""
            for element in clean_list[index_start:]:
                if element is not None and element != "R1":
                    event_type = event_type + element + " "
                else:
                    break
            event_type = event_type.strip()
        return event_type

    """
        This method obtains the elements referred to the process state
        and concatenates them from the standard files 
    """

    @staticmethod
    def check_proccess_state_standard_file(clean_list):
        try:
            index_process_state = clean_list.index("R1")
        except ValueError:
            index_process_state = None

        process_state = None

        if index_process_state is not None:
            process_state = ""
            for element in clean_list[index_process_state:]:
                if element is not None:
                    process_state = process_state + element + " "
                else:
                    break

            process_state = process_state.strip()

        return process_state

    """
        This method extract the run number from the basic files
    """

    @staticmethod
    def check_run_number(run_string):
        run_number = int(run_string[run_string.index("Run") + len("Run"):len("Run") + 5])
        return run_number

    """
        This method extract the date from the Night Summary file name
    """

    @staticmethod
    def get_date_from_ns_files(night_summary_file_name):
        date_string = night_summary_file_name[
                      night_summary_file_name.index("NightSummary_") + len("NightSummary_"):len("NightSummary_") + 8]
        return datetime.strptime(date_string, '%Y%m%d').date()

    """
        This method extract the date from the Basic file name
    """

    @staticmethod
    def get_date_from_basic_files(basic_file_name):
        date_string = basic_file_name[
                      basic_file_name.index("RUNs_FROM_") + len("RUNs_FROM_"):len("RUNs_FROM_") + 8]
        return datetime.strptime(date_string, '%Y%m%d').date()

    """
        This method removes the tab from the line and replaces it with a blank space
    """

    @staticmethod
    def remove_tab(line):
        return str(line).replace("\t", " ")

    """
        This method is used to obtain the stream attribute
    """

    @staticmethod
    def get_stream_attr(line_file):
        regular_expresion = re.search(r'\[(.*)\]', line_file)
        if regular_expresion is not None and len(regular_expresion.group(0)) != 0:
            line_file = line_file.replace(regular_expresion.group(0), "")
            return line_file, regular_expresion.group(0)

    @staticmethod
    def convert_string_to_number(string, number_type):
        value_aux = string
        if value_aux is not None:
            if number_type == "int":
                value_aux = int(string)
            elif number_type == "float":
                value_aux = float(string)
        return value_aux
