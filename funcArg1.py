from typing import Dict

def generate_squares(num: int) -> Dict[int, int]:
    return {i: i ** 2 for i in range(1, num + 1)}
print(generate_squares(5))
if __name__ == "__main__":
    assert generate_squares(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}