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
        This method collects the last elements and concatenates 
        them to form the event type field
    """
    @staticmethod
    def check_event_type(clean_list, length):
        event_type=""
        if len(clean_list) > length:
            for element in range(len(clean_list)-length):
                event_type = event_type + clean_list[element+length] + " "

        return event_type

    @staticmethod
    def check_run_number(run_string):
        run_number = int(run_string[run_string.index("Run") + len("Run"):len("Run") + 5])
        return run_number



