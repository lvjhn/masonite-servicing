from src.masonite_servicing import *

class CalculatorService: 
    def add(self, x, y):
        return result("OK", "Added", x + y)
    
    def subtract(self, x, y): 
        return result("OK", "Subtracted", x - y)

    def multiply(self, x, y): 
        z = x
        for i in range(y - 1):
            z = fetch(lambda: self.add(z, x)) 
        return result("OK", "Multiplied", z)

calculator_service = CalculatorService()