import logging

log = logging.getLogger("hello_app")


def test_it(test_var: str) -> bool:
    log.debug(f"This is a debug message: {test_var}")
    return True