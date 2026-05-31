def divide(str_with_ints: str) -> str | float | None:
    my_list = str_with_ints.split()
    lis = [item for item in my_list]
    if lis[0].isdigit() and lis[1].isdigit() and lis[1] != 0:
        try:
            result = int(lis[0]) / int(lis[1])
            return result
        except ZeroDivisionError:
            return f"Error code: division by zero"
    elif not lis[0].isdigit() or not lis[1].isdigit():
        try:
            result = int(lis[0]) / int(lis[1])
            return result
        except ValueError:
            return f"Error code: invalid literal for int() with base 10: " \
                   f"'{lis[1] if lis[0].isdigit() else lis[0]}'"
    return None


if __name__ == "__main__":
    assert divide("4 0") == "Error code: division by zero"
    assert divide("4 2") == 2.0
    assert divide("* 1") == "Error code: invalid literal for int() with base 10: '*'"