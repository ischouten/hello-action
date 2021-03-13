import azure.functions as func
import logquicky
from utils.some_util import test_it

log = logquicky.load("hello", level="DEBUG")


def main(req: func.HttpRequest) -> func.HttpResponse:
    log.info("Python HTTP trigger function processed a request.")

    test_it("test")
    log.debug("Test again?")

    return func.HttpResponse("Hello you! This worked!", status_code=200)
