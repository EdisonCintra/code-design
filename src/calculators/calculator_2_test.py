from typing import Dict
from .calculator_2 import Calculator2

class MockRequest:
    def __init__(self, body : Dict) -> None:
        self.json = body


def test_calculate():
    mock_request = MockRequest({"numbers" : [1, 2, 3, 4]})
    calculator_2 = Calculator2()
    calculator_2.calculate(mock_request)