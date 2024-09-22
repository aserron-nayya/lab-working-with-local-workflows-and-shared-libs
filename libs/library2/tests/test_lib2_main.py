import pytest
from libs.library2.main import another_function

def test_another_function():
    assert another_function() == "yet another fn."