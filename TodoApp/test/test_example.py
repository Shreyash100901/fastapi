import pytest


def test_equal_notequal():
    assert 3 == 3


class Student:
    def __init__(self, first_name: str, last_name: str, major: str, years: str):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.years = years

@pytest.fixture
def default_employee():
    return Student('John', 'Doe', 'Computer', 3)

def test_person_initialization(default_employee):
    p = Student('John', 'Doe', 'Computer', 3)
    assert default_employee.first_name == 'John', 'First name should be John'
    assert default_employee.last_name == 'Doe', 'Last name should be Doe'
    assert default_employee.major == 'Computer'
    assert default_employee.years == 3
