import os
import sys
import logging
import logging.handlers
from opencensus.ext.azure.log_exporter import AzureLogHandler


def setup_loggers(name: str):

    app_insights_key = os.environ.get("APPINSIGHTS_INSTRUMENTATIONKEY")
    app_insights_level = os.environ.get("APPINSIGHTS_LOG_LEVEL", logging.NOTSET)

    formatter = logging.Formatter("[%(levelname)s] %(name)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    logger_name = name if name is not None else os.environ.get("LOGGER_NAME")
    log = logging.getLogger(logger_name) if name is not None else logging.getLogger()
    log.handlers.clear()
    log.propagate = False

    logging.addLevelName(logging.WARNING, "WARN")

    console_log_level = os.environ.get("CONSOLE_LOGGER_LEVEL", logging.DEBUG)
    console_logger = logging.StreamHandler()
    console_logger.setFormatter(formatter)
    console_logger.setLevel(console_log_level)
    log.addHandler(console_logger)

    if app_insights_key:  # and app_insights_level != logging.NOTSET:
        app_insights_handler = AzureLogHandler(connection_string=f"InstrumentationKey={app_insights_key}")
        app_insights_handler.setFormatter(formatter)
        app_insights_handler.setLevel(app_insights_level)

        log.addHandler(app_insights_handler)

    return log
