from masonite.tests import TestCase 
import pytest
from unittest.mock import patch

from masonite_servicing import *
import uuid

class TestMasoniteServicing(TestCase):
    
    
    def setUp(self):
        super().setUp()

    def test_status_codes(self): 
        assert(OK == True)
        assert(NOT_OK == False)

    def test_service_result(self): 
        service_result = ServiceResult(OK, "foo", "bar")

        # check id 
        assert(service_result.id != None)
        assert(len(service_result.id) == len(str(uuid.uuid4()))) 

        # check status 
        assert(service_result.status == OK)

        # check message
        assert(service_result.message == "foo") 

        # check value 
        assert(service_result.value == "bar")

    def test_service_result_is_ok(self): 
        service_result = ServiceResult(OK, "foo", "bar") 

        # check status
        assert(service_result.is_ok() == True)

    def test_service_result_is_not_ok(self): 
        service_result = ServiceResult(NOT_OK, "foo", "bar") 

        # check status 
        assert(service_result.is_not_ok() == True) 

    def test_service_result_same_should_return_true(self): 
        service_result_a = ServiceResult(OK, "foo", "bar") 
        service_result_b = ServiceResult(OK, "foo", "bar")
        service_result_b.id = service_result_a.id

        # check same function 
        assert(same(service_result_a, service_result_b))

    def test_service_result_same_should_return_false(self): 
        service_result_a = ServiceResult(OK, "foo", "bar") 
        service_result_b = ServiceResult(OK, "foo", "bar")

        # check same function 
        assert(same(service_result_a, service_result_b) == False)


    @pytest.mark.dependency(depends=[
        "test_service_same_should_return_true",
        "test_service_same_should_return_false"    
    ])
    def test_ok(self): 
        service_result_a = ServiceResult(OK, "foo", "bar")
        service_result_b = ok("foo", "bar") 
        service_result_b.id = service_result_a.id 
        
        # check that service results to true
        assert(same(service_result_a, service_result_b))

    @pytest.mark.dependency(depends=[
        "test_service_same_should_return_true",
        "test_service_same_should_return_false"    
    ])
    def test_not_ok(self): 
        service_result_a = ServiceResult(NOT_OK, "foo", "bar")
        service_result_b = not_ok("foo", "bar") 
        service_result_b.id = service_result_a.id 
        
        # check that service results to true
        assert(same(service_result_a, service_result_b))

    
    def test_relay_should_return_identity(self): 
        service_result_a = ServiceResult(OK, "foo", "bar") 
        assert(relay(service_result_a) == service_result_a) 
    
    def test_respond_should_return_validation_error(self): 
        class Request: 
            def validate(validations): 
                class Errors: 
                    def all(self): 
                        return [1, 2, 3]
                return Errors()   

        is_callback_called = False 

        def callback():
            global is_callback_called
            is_callback_called = True
        
        result = respond(Request(), [], callback)

        assert(result["status"] == "input-error")
        assert(result["message"] == "VALIDATION_ERROR")
        assert(result["is_validation_error"] == True)
        assert(is_callback_called == False)

    
    @pytest.mark.dependency(depends=[
        "test_ok"
    ])
    def test_respond_should_proceed(self): 
        class Request: 
            def validate(validations): 
                return None

        is_callback_called = False 
        
        def callback():
            global is_callback_called
            is_callback_called = True
            return relay(ok("CALLBACK_CALLED", True))
        
        result = respond(Request(), [], callback)

        assert(result["status"] == "not-ok")
        assert(result["message"] == "CALLBACK_CALLED")
        assert(result["value"] == True)
        assert(is_callback_called == True)

    def test_validation_tester(self): 
        from masonite_servicing.validation.IsBoolean import IsBoolean
        
        tester = ValidationTester()

        tester.validation = IsBoolean
        tester.should_pass = ["true", "false"] 
        tester.should_error = ["yes", "no"]
        
        tester.run(self) 

    
    def test_route_tester(self): 
        tester = RouteTester()

        tester.should_pass = [
            { "a": 1, "b" : 1 }, 
            { "a": "2", "b" : "3" }
        ]

        tester.should_fail = [
            { "a": -1, "b" : -1 }, 
            { "a": 0.1, "b" : 0.1 }, 
            { "a": 0, "b": 0 }
        ]

        tester.route = "/calculator/add"
        tester.method = "get"

        tester.run(self)