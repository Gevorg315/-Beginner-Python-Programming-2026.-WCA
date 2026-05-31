from time import time
from functools import wraps
import filecmp

def log(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time()
        result = fn(*args, **kwargs)
        end = time()
        execution_time = end - start
        # positional arguments
        arg_names = fn.__code__.co_varnames[:len(args)]
        args_text = ", ".join(
            f"{name}={value}"
            for name, value in zip(arg_names, args)
        )
        # keyword arguments
        kwargs_text = ", ".join(
            f"{key}={value}"
            for key, value in kwargs.items()
        )
        log_message = (
            f"{fn.__name__}; "
            f"args: {args_text}; "
            f"kwargs: {kwargs_text}; "
            f"execution time: {execution_time:.2f} sec.\n"
        )
        with open("log.txt", "a") as file:
            file.write(log_message)
        return result
    return wrapper

@log
def foo(a, b, c):
    return a + b + c


foo(1, 2, c=3)

if __name__ == "__main__":
    assert filecmp.cmp(add(2, 4, c=5, d=5), "Log.txt")