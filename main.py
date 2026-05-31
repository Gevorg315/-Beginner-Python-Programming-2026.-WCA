from typing import Union

NumType = Union[int, float]


def some_expression_with_rounding(a: NumType, b: NumType) -> NumType:
    result = (12 * a + 25 * b) / (1 + a ** (2 ** b))
    return result


print(some_expression_with_rounding(4, 6))
