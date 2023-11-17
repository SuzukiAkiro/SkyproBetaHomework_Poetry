import os
from datetime import datetime

import pytest

import src.decorators as decorators


def test_log_success():
    # Test when function works correctly
    @decorators.log(filename="log.txt")
    def test_function():
        return 42

    test_function()
    with open("log.txt", "r") as file:
        assert file.read() == f"{datetime.now().strftime('%Y-%m-%d %H:%M')} test_function ok!\n"
        os.remove("log.txt")


def test_log_failure():
    # Test when function raises an exception
    with pytest.raises(Exception):

        @decorators.log(filename="log.txt")
        def test_function2():
            raise Exception("Something went wrong")

        test_function2()
        with open("log.txt", "r") as file:
            assert (
                file.read()
                == f"{datetime.now().strftime('%Y-%m-%d %H:%M')} test_function Error: Something went wrong\n Inputs {''}, {''}\n"
            )
    os.remove("log.txt")
