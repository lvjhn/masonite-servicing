# flake8: noqa F401
from .providers.ServicingProvider import ServicingProvider
from masonite.validation import Validator

import uuid

# result status constants
OK = True 
NOT_OK = False 

# service result class
class ServiceResult: 
    def __init__(self, status, message, value): 
        self.id = ServiceResult.generate_id() 
        self.status = status 
        self.message = message 
        self.value = value

    def is_ok(self): 
        """ 
            Checks if the service result is ok.
        """ 
        return self.status == OK 

    def is_not_ok(self): 
        """ 
            Checks if the service result is not ok.
        """ 
        return self.status == NOT_OK 

    def generate_id():
        """ 
            Generates an id for the service result.
        """ 
        return uuid.uuid4() 

    def get(self):
        """
            Gets the value in a service result.   
        """
        return self.value
 
def relay(value): 
    return value

def ok(message, value): 
    """ 
        Creates an affirmative ResultObject.
    """ 
    return ServiceResult(OK, message, value)

def not_ok(message, value): 
    """
        Creates a non-affirmative ServiceResult object. 
    """ 
    return ServiceResult(NOT_OK, message, value)

def same(result_a, result_b):
    """
        Checks if two results are the same.  
    """ 

    # check if types are the same first 
    if type(result_a) is not type(result_b): 
        raise Exception(f"Type Error: Result A {result_a} must of the same type of Result B {result_b}")

    # check if values are the same
    return (
        (result_a.id == result_b.id) 
        and 
        (result_a.status == result_b.status)
        and 
        (result_a.message == result_b.message)
    )

def respond(request, validations, callback): 
    """ 
        Encapsulates a route response from a service call.
    """ 

    # check if there are errors 
    errors = request.validate(*validations) 
    
    # if there are errors, return validation error messages
    # as the response 
    if errors: 
        return {
            "status": "not-ok", 
            "message": "VALIDATION_ERROR", 
            "value": errors.all() 
        }

    # call and return callback function
    result = callback() 

    # transform result to dictionary 
    result_dict = {
        "status" : "ok" if result.status else "not-ok", 
        "message" : result.message, 
        "value" : result.value
    }

    return result_dict 

        
class ValidationTester: 
    def __init__(self): 
        self.should_error   = {} 
        self.should_pass    = {}
        self.validator      = {}

    def handle_error_cases(self, errors, should_error): 
        has_error = False 
        for field_name in should_error: 
            validation_items = should_error[field_name]
            for validation_item in validations_items: 
                validation_item_dict = {}
                validation_item[field_name] = validation_item 
                error = Validator().validate(validation_item_dict)
                if not error: 
                    errors.push("Field [" + field_name + "] should error on input [" + validation_item + "]")
                    has_error = True 
        return has_error 

    def handle_pass_cases(self, errors, should_pass): 
        has_error = False 
        for field_name in should_pass: 
            validation_items = should_pass[field_name]
            for validation_item in validations_items: 
                validation_item_dict = {}
                validation_item[field_name] = validation_item 
                error = Validator().validate(validation_item_dict)
                if error: 
                    errors.push("Field [" + field_name + "] should pass on input [" + validation_item + "]")
                    has_error = True 
        return has_error
    
    def report_errors(self, errors, context): 
        for error in errors:
            context.dump("Error (" + str(i) + "/" + str(len(errors)) +"): "  + error)

    def run(self, context): 
        should_error = self.should_error
        should_pass = self.should_pass

        errors = []

        # handle error cases 
        self.handle_error_cases(errors, should_error)

        # handle pass cases 
        self.handle_pass_cases(errors, should_pass)
   
        # dump errors
        self.report_errors(errors, context)

        assert(False)

class RouteInputTester: 
    def __init__(self): 
        self.should_error   = [] 
        self.should_pass    = [] 
        self.route          = "/" 
        self.method         = "get"

    def run(self, context):
        pass