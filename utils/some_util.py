import logquicky

log = logquicky.load("hello")


def test_it(test_var: str) -> bool:
    log.debug(f"This is a debug message: {test_var}")
    return True