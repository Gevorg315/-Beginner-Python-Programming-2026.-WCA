from time import time
from typing import Dict

execution_time: Dict[str, float] = {}
def time_decorator(fn):
    sleep = 0.2
    def wrap_func(*args, **kwargs):
        nonlocal sleep
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        sleep += (t2 - t1)
        execution_time[fn.__name__] = sleep
        print(execution_time)
        return result
    return wrap_func

@time_decorator
def func_add(a, b):
    return a + b

@time_decorator
def func_del(a, b):
    return a - b

if __name__ == "__main__":
    assert func_add(10, 20) == 30
    assert func_del(20, 30) == -10
    for key, value in execution_time.items():
        assert execution_time[key] == value