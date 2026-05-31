from typing import Tuple

def get_tuple(num: int) -> tuple[int, ...]:
    digits = [int(char) for char in str(num)]
    print(tuple(digits))
    return tuple(digits)

if __name__ == "__main__":
    assert get_tuple(7345393649) == (7, 3, 4, 5, 3, 9, 3, 6, 4, 9)