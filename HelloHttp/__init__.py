import os
import azure.functions as func
from opencensus.ext.azure.log_exporter import AzureLogHandler
import logquicky
from utils.some_util import test_it

log_instrumentation_key = os.environ.get("APPINSIGHTS_INSTRUMENTATION_KEY")


log = logquicky.load("hello", level="DEBUG")
log.addHandler(AzureLogHandler(connection_string=log_instrumentation_key))


def main(req: func.HttpRequest) -> func.HttpResponse:
    log.info("Python HTTP trigger function processed a request.")

    test_it("test")
    log.debug("Test again?")

    log.warn("This is a warning")

    return func.HttpResponse("Hello you! This worked!", status_code=200)
