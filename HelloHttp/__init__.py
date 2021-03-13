import logging
import typing
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request. This line is also going to be way too long.")

    return func.HttpResponse("Hello! This worked!", status_code=200)
