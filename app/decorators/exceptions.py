import functools
import logging

def exception(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Exception occurred in {func.__name__}: {e}")
            raise
    return wrapper
