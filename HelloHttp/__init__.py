import azure.functions as func
from utils.logger import setup_loggers
import utils

log = setup_loggers("hello_app")


def main(req: func.HttpRequest) -> func.HttpResponse:
    log.info("Python HTTP trigger function processed a request.")

    utils.test_it("test")
    log.debug("Test again?")

    log.warn("This is a warning")

    log.error("Error")

    return func.HttpResponse("Hello you! This worked!", status_code=200)
