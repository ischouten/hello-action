import os
import azure.functions as func
import logquicky
from opencensus.ext.azure.log_exporter import AzureLogHandler
from utils.some_util import test_it

app_insights_key = os.environ.get("APPINSIGHTS_INSTRUMENTATIONKEY")

log = logquicky.load("hello", level="DEBUG")
app_insights_handler = AzureLogHandler(connection_string=f"InstrumentationKey={app_insights_key}")
log.addHandler(app_insights_handler)


def main(req: func.HttpRequest) -> func.HttpResponse:
    log.info("Python HTTP trigger function processed a request.")

    test_it("test")
    log.debug("Test again?")

    log.warn("This is a warning")

    return func.HttpResponse("Hello you! This worked!", status_code=200)
