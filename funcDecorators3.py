def validate(func):
    def func_wrapper(x, y, z):
        if not (256 >= x >= 0 and 256 >= y >= 0 and 256 >= z >= 0):
            return "Function call is not valid!"
        res = func(x, y, z)
        return res
    return func_wrapper

@validate
def set_pixel(x: int, y: int, z: int) -> str:
    return "Pixel created!"

if __name__ == "__main__":
    assert set_pixel(0, 127, 300) == "Function call is not valid!"
    assert set_pixel(0, 127, 250) == "Pixel created!"