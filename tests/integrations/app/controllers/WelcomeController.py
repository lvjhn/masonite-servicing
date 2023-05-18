"""A WelcomeController Module."""
from masonite.views import View
from masonite.controllers import Controller
from masonite.request import Request

from tests.integrations.app.services.CalculatorService import *


class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def add(self, request: Request, validate: Validator):
        return respond(
            request, 
            [
                validate.required(["x", "y"]),
                validate.numeric(["x", "y"])
            ], 
            lambda: calculator_service.add(
                int(request.input("x")), 
                int(request.input("y"))
            )   
        )

    def subtract(self, request: Request):
        return respond(
            request, 
            [], 
            lambda: calculator_service.subtract(5, 3)
        )

    def multiply(self, request: Request):
        return respond(request, [], lambda: calculator_service.multiply(5, 10))