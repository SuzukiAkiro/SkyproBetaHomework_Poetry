import pytest
import os
import src.decorators as decorators


def test_log_success():
    @decorators.log(filename="log.txt")
    def test_function():
        return 42

    # Test when function executes successfully
    assert test_function() == 42


def test_log_failure():
    # Test when function raises an exception
    with pytest.raises(Exception):

        @decorators.log(filename="log.txt")
        def test_function2():
            raise Exception("Something went wrong")

        test_function2()
