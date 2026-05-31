NumType = int | float


def some_expression_with_rounding(a: NumType, b: NumType) -> NumType:
    result = None
    if (1 + a ** (2 ** b)) != 0:
        result = round((12 * a + 25 * b) / (1 + a ** (2 ** b)), 2)
    print(result)
    return result


if __name__ == "__main__":
    assert some_expression_with_rounding(-1, 5) == 56.5
    assert some_expression_with_rounding(1, 4.0) == 56.0
    assert some_expression_with_rounding(3.0, 4.0) == 0.0
    assert some_expression_with_rounding(-1, 0) is None
