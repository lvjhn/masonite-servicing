from masonite.controllers import Controller
from masonite.request import Request 
from masonite.validation import Validator
from masonite.views import View

from masonite_servicing import * 

from masonite_servicing.services import calculator_service

class CalculatorController(Controller):
    
    def add(self, request: Request, validate: Validator): 
        return respond(
            request, 
            [
                validate.required(["a", "b"])
            ], 
            lambda: calculator_service.add(
                int(request.input("a")),
                int(request.input("b"))
            )
        )

        
    def subtract(self, request: Request, validate: Validator): 
        return respond(
            request, 
            [
                validate.required(["a", "b"])
            ], 
            lambda: calculator_service.subtract(
                int(request.input("a")),
                int(request.input("b"))
            )
        )

            
    def multiply(self, request: Request, validate: Validator): 
        return respond(
            request, 
            [
                validate.required(["a", "b"])
            ], 
            lambda: calculator_service.multiply(
                int(request.input("a")),
                int(request.input("b"))
            )
        )

    def divide(self, request: Request, validate: Validator): 
        return respond(
            request, 
            [
                validate.required(["a", "b"])
            ], 
            lambda: calculator_service.divide(
                int(request.input("a")),
                int(request.input("b"))
            )
        )