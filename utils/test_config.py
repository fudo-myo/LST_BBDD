import os

os.environ["TEST_PROFILE"] = "test_mode"


def get_test_mode():
    return print("--------------- EXECUTING REQUESTS IN MODE: '{}' ---------------".format(os.getenv("TEST_PROFILE")))