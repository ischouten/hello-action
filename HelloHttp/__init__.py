import os
import azure.functions as func
from applicationinsights.logging import LoggingHandler
import logquicky
from utils.some_util import test_it

app_insights_key = os.environ.get("APPINSIGHTS_INSTRUMENTATION_KEY")

log = logquicky.load("hello", level="DEBUG")
app_insights_handler = LoggingHandler(app_insights_key)
log.addHandler(app_insights_handler)


def main(req: func.HttpRequest) -> func.HttpResponse:
    log.info("Python HTTP trigger function processed a request.")

    test_it("test")
    log.debug("Test again?")

    log.warn("This is a warning")

    return func.HttpResponse("Hello you! This worked!", status_code=200)
