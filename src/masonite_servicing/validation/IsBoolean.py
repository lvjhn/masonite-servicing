
from masonite.validation import BaseValidation


class IsBoolean(BaseValidation):
    def passes(self, attribute, key, dictionary):
        return attribute in ["true", "false"]

    def message(self, key):
        return "Must be true or false"

    def negated_message(self, key):
        return "Must not be true or false"
