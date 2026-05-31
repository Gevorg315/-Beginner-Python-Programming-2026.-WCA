def decorator_apply(lambda_func):
    def decorating(fn):
        def wrapper(num):
            result = fn(lambda_func(num))
            return result
        return wrapper
    return decorating

@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) -> int:
    return num

if __name__ == "__main__":
    assert return_user_id(42) == 43