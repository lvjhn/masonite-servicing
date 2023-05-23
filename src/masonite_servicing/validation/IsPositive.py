
from masonite.validation import BaseValidation


class IsPositive(BaseValidation):
    def passes(self, attribute, key, dictionary):
        return int(attribute) > 0

    def message(self, key):
        return "Must be positive"

    def negated_message(self, key):
        return "Must not be positive"
