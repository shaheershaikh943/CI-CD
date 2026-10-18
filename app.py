from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Calculator API")


class CalculationRequest(BaseModel):
    operation: str
    operand1: float
    operand2: float
    result: float = 0

@app.get("/")
def home():
    return {"message": "Welcome to the Calculator API!"}

@app.post("/calculate")
def calculate(Calculator: CalculationRequest):
    if Calculator.operation == "add":
        result = Calculator.operand1 + Calculator.operand2
    elif Calculator.operation == "subtract":
        result = Calculator.operand1 - Calculator.operand2
    elif Calculator.operation == "multiply":
        result = Calculator.operand1 * Calculator.operand2
    elif Calculator.operation == "divide":
        if Calculator.operand2 == 0:
            return {"error": "Division by zero is not allowed."}
        result = Calculator.operand1 / Calculator.operand2
    else:
        return {"error": "Invalid operation. Supported operations are: add, subtract, multiply, divide."}

    return {
        "operation": Calculator.operation,
        "operand1": Calculator.operand1,
        "operand2": Calculator.operand2,
        "result": result
        }
