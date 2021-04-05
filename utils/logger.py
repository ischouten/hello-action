import os
import logging
import logging.handlers
from opencensus.ext.azure.log_exporter import AzureLogHandler

levels = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warn": logging.WARNING,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "critical": logging.CRITICAL,
    "disable": logging.NOTSET,
}


def setup_loggers(name: str, level: str):

    app_insights_key = os.environ.get("APPINSIGHTS_INSTRUMENTATIONKEY")
    app_insights_level = get_level(os.environ.get("APPINSIGHTS_LOG_LEVEL", "disabled"))

    formatter = logging.Formatter("[%(levelname)s] %(name)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    logging.basicConfig(formatter=formatter)
    logging.addLevelName(logging.WARNING, "WARN")

    logger_name = name if name is not None else os.environ.get("LOGGER_NAME")

    log = logging.getLogger(logger_name) if name is not None else logging.getLogger()

    root_logger = logging.getLogger()
    root_logger.setLevel(get_level(level))
    log.handlers.clear()
    log.propagate = False

    console_log_level = get_level(level if level else os.environ.get("CONSOLE_LOGGER_LEVEL", "info"))
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(console_log_level)
    log.addHandler(console_handler)

    if app_insights_key:  # and app_insights_level != logging.NOTSET:
        app_insights_handler = AzureLogHandler(connection_string=f"InstrumentationKey={app_insights_key}")
        app_insights_handler.setFormatter(formatter)
        app_insights_handler.setLevel(app_insights_level)

        log.addHandler(app_insights_handler)

    return log


def get_level(level_name: str):

    if level_name is None:
        level_name = "disabled"

    level_name = level_name.lower()
    level = levels.get(level_name, logging.INFO)
    return level
