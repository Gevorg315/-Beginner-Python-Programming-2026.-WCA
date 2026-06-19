from time import time
from functools import wraps
import filecmp
import os

def log(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time()
        result = fn(*args, **kwargs)
        end = time()
        execution_time = end - start

        arg_names = fn.__code__.co_varnames[:len(args)]
        args_text = ", ".join(
            f"{name}={value}"
            for name, value in zip(arg_names, args)
        )

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
        # print(log_message)
        with open("log.txt", "a") as file:
            file.write(log_message)
        return result
    return wrapper

@log
def add(a, b, c, d):
    return a + b + c + d

if __name__ == "__main__":
    if os.path.exists("log.txt"):
        os.remove("log.txt")
    add(2, 4, c=5, d=5)

    with open("expected_log.txt", "w") as f:
        f.write("add; args: a=2, b=4; kwargs: c=5, d=5; execution time: 0.00 sec.\n")
    try:
        assert filecmp.cmp("expected_log.txt", "log.txt"), "The log files do not match!"
        print("Test passed successfully!")
    finally:
        if os.path.exists("expected_log.txt"): os.remove("expected_log.txt")

        if os.path.exists("log.txt"): os.remove("log.txt")