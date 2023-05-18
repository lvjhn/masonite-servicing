
from masonite.validation import BaseValidation


class IsPositive(BaseValidation):
    def passes(self, attribute, key, dictionary):
        return int(attribute) > 0

    def message(self, key):
        return f"{key} must be true or false"

    def negated_message(self, key):
        return "{key} must not be true or false"
