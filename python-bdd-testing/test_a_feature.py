import pytest
from pytest_bdd import given, when, then, scenarios, parsers

# Define the scenario(s)
scenarios('test_calculator.feature')

# Fixture for the calculator
@pytest.fixture
def calculator():
    return Calculator()  # Assuming Calculator is a class that represents the calculator


@given("I have two numbers")
def step_given_numbers():
    number1 = 5
    number2 = 3
    return number1, number2

@when("I add the numbers")
def step_when_add_numbers():
    result = 5 + 3
    return result
