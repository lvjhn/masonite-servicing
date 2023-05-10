# flake8: noqa F401
from .providers.ServicingProvider import ServicingProvider

class ServiceResult:
    def __init__(self, *args): 
        self.status = args[0]
        self.message = args[1]
        self.data = args[2]

def result(*args):
   return ServiceResult(*args)

def respond(result):
    return {
        "status" : result.status, 
        "message" : result.message, 
        "data" : result.data
    }

def relay(result):
    return result[1]

def fetch(cb, *args): 
    return cb(*args).data

class SampleService:
    def add(self, x, y): 
        return result("ok", "added", x + y) 
    
def main():
    sample_service = SampleService()
    sample_service.add(3, 5)
