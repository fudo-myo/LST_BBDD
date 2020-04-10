from config.base import getSession
from utils.string_literals import StringLiterals


class TestUtils:

    @classmethod
    def print_test_started(cls, test_name):
        print(StringLiterals.PREFIX_ONE_TEST)
        print(StringLiterals.PREFIX_TWO_TEST)
        print(
            "                              RUNNING THE TEST: '{}'                                             ".format(
                test_name))
        print(StringLiterals.PREFIX_TWO_TEST)
        print(StringLiterals.PREFIX_ONE_TEST)

    @classmethod
    def print_test_finished(cls, test_name):
        print(StringLiterals.PREFIX_ONE_TEST)
        print(StringLiterals.PREFIX_TWO_TEST)
        print(
            "                              TEST RUN: '{}' FINISHED                                             ".format(
                test_name))
        print(StringLiterals.PREFIX_TWO_TEST)
        print(StringLiterals.PREFIX_ONE_TEST)

    @classmethod
    def clear_table_after_test(cls, table):
        session = getSession()
        session.query(table).delete(synchronize_session=False)
        session.commit()

    @classmethod
    def print_insert_trace(cls, table_name, id):
        print("############ RECORD INSERTED IN TABLE: '{}' WITH ID: '{}' ############".format(table_name, id))

    @classmethod
    def print_update_trace(cls, table_name, id):
        print("############ RECORD UPDATED IN TABLE: '{}' WITH ID: '{}' ############".format(table_name, id))

    @classmethod
    def print_delete_trace(cls, table_name, id):
        print("############ RECORD DELETED IN TABLE: '{}' WITH ID: '{}' ############".format(table_name, id))

    @classmethod
    def print_get_all_trace(cls, table_name, records):
        print("############ '{}' RECORDS HAVE BEEN OBTAINED FROM TABLE '{}' ############".format(records, table_name))

    @classmethod
    def print_get_by_id_trace(cls, table_name, record):
        print("############ RECORD WITH ID: '{}' HAS BEEN OBTAINED FROM TABLE '{}' ############".format(record,
                                                                                                        table_name))

    @classmethod
    def assert_insert_message(cls, table_name):
        return "Failed to insert into table '{}'".format(table_name)

    @classmethod
    def assert_update_message(cls, field):
        return "Field '{}' has not been updated".format(field)

    @classmethod
    def assert_delete_message(cls, id, table_name):
        return "Failed to delete record with id: '{}' in table '{}'".format(
            id, table_name)

    @classmethod
    def assert_get_all_message(cls, table_name):
        return "Error getting all the elements that are inserted in the table '{}'".format(
            table_name)

    @classmethod
    def assert_get_by_id_message(cls, table_name, id):
        return " Error in obtaining the object of table: '{}', with id:'{}'".format(
                                 table_name, id)
