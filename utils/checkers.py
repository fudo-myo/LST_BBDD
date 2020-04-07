import datetime
import logging

from pandas._libs.parsers import basestring
from sqlalchemy import Integer, INTEGER, VARCHAR, DATETIME, String, DateTime
from sqlalchemy.dialects.mysql import DOUBLE


class Checkers:
    __log_format = '%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
    __log_date_format = '%Y-%m-%d:%H:%M:%S'

    @staticmethod
    def check_field_not_null(old_value, new_value):
        if new_value is not None:
            return new_value
        else:
            return old_value

    @classmethod
    def print_object_filter_null(cls, field, value):
        logging.basicConfig(level=logging.WARNING,
                            format=cls.__log_format,
                            datefmt=cls.__log_date_format)
        return logging.warning("************ Object not found with '{}': '{}' ************".format(field, value))

    @classmethod
    def empty_list(cls, table_name):
        logging.basicConfig(level=logging.WARNING,
                            format=cls.__log_format,
                            datefmt=cls.__log_date_format)
        return logging.warning(
            "************ No item has been retrieved from named table: '{}' ************".format(table_name))

    @classmethod
    def print_exception_two_params(cls, desc_error, code_error):
        logging.basicConfig(level=logging.ERROR,
                            format=cls.__log_format,
                            datefmt=cls.__log_date_format
                            )
        return logging.error(
            "*********** Error code number <<< {} >>>, Error description: <<< {} >>> ***********".format(code_error,
                                                                                                         desc_error))

    @classmethod
    def print_exception_one_param(cls, error):
        logging.basicConfig(level=logging.ERROR,
                            format=cls.__log_format,
                            datefmt=cls.__log_date_format)
        return logging.error(
            "*********** Error <<< {} >>> ***********".format(error))

    @classmethod
    def check_table_exists(cls, engine, name):
        ret = engine.dialect.has_table(engine, name)
        logging.basicConfig(level=cls.__get_level_logging(ret),
                            format=cls.__log_format,
                            datefmt=cls.__log_date_format)
        if ret:
            logging.info('*********** Table "{}" exists: {} ***********'.format(name, ret))
        else:
            logging.warning('*********** Table "{}" does not exists: {} ***********'.format(name, ret))

        return ret

    @staticmethod
    def __get_level_logging(flag):
        if flag:
            level_aux = logging.INFO
        else:
            level_aux = logging.WARNING
        return level_aux

    @classmethod
    def validate_int(cls, value, field):
        flag = False
        if isinstance(value, int):
            flag = True
        else:
            try:
                assert isinstance(value, int)
            except AssertionError:
                logging.basicConfig(level=logging.WARNING,
                                    format=cls.__log_format,
                                    datefmt=cls.__log_date_format)
                logging.warning(
                    "************ The field '{}' with value '{}' is not Integer ************".format(
                        field, value))
        return flag

    @classmethod
    def validate_datetime(cls, value, field):
        flag = False
        if isinstance(value, datetime.datetime):
            flag = True
        else:
            try:
                assert isinstance(value, datetime.datetime)
            except AssertionError:
                logging.basicConfig(level=logging.WARNING,
                                    format=cls.__log_format,
                                    datefmt=cls.__log_date_format)
                logging.warning(
                    "************ The field '{}' with value '{}' is not DateTime ************".format(
                        field, value))
        return flag

    @staticmethod
    def validate_double(value):
        if isinstance(value, float):
            value = float(value)
        else:
            assert isinstance(value, float)
        return value

    @staticmethod
    def validate_string(value):
        assert isinstance(value, basestring)
        return value

    @classmethod
    def get_validators(cls):
        validators = {
            Integer: cls.validate_int,
            INTEGER: cls.validate_int,
            DOUBLE: cls.validate_double,
            VARCHAR: cls.validate_string,
            DATETIME: cls.validate_datetime,
            String: cls.validate_string,
            DateTime: cls.validate_datetime,
        }
        return validators
