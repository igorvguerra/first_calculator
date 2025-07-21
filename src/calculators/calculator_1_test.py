from .calculator_1 import Calculator1
from typing import Dict

class MockRequest:
    def __init__(self, body: Dict):
        self.json = body

def test_calculate():
    mock_request = MockRequest(body={"number": 1})
    calculator_1 = Calculator1()

    response = calculator_1.calculate(mock_request)
    print()
    print(response)

   
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "Result" in response["data"]

    assert response["data"]["Result" ] == 14.25
    assert response["data"]["Calculator"] == 1