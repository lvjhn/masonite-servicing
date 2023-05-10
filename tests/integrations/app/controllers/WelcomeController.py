"""A WelcomeController Module."""
from masonite.views import View
from masonite.controllers import Controller

from tests.integrations.app.services.CalculatorService import *


class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def add(self, view: View):
        return respond(relay(calculator_service.add(5, 3)))

    def subtract(self, view: View):
        return respond(relay(calculator_service.subtract(5, 3)))

    def multiply(self, view: View):
        return respond(relay(calculator_service.multiply(5, 10)))