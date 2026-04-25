from datetime import datetime
from functools import wraps


def _format_log_line(function_name, args, kwargs, result):
    """Build one uniform log line for every decorated call."""
    return (
        f"{datetime.now()} | "
        f"{function_name} | "
        f"args={args}, kwargs={kwargs} | "
        f"result={result}\n"
    )


def _write_log(path, function_name, args, kwargs, result):
    """Append a log line to the target file."""
    with open(path, 'a', encoding='utf-8') as f:
        f.write(_format_log_line(function_name, args, kwargs, result))


def logger(old_function):
    """Basic decorator that always writes to main.log."""

    @wraps(old_function)
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        _write_log('main.log', old_function.__name__, args, kwargs, result)
        return result

    return new_function


def logger_with_path(path):
    """Parameterized decorator that captures `path` in a closure."""

    def __logger(old_function):

        @wraps(old_function)
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            _write_log(path, old_function.__name__, args, kwargs, result)
            return result

        return new_function

    return __logger
