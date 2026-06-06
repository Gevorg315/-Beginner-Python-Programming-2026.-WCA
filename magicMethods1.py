from typing import List

class Counter:
    def __init__(self, values: List[int]):
        self.values = values

    def __add__(self, string):
        result = []
        for i in self.values:
            new_string = f"{i} {string}"
            result.append(new_string)
        return result

if __name__ == "__main__":
    assert Counter([1, 2, 3]) + "Mississippi" == ["1 Mississippi", "2 Mississippi", "3 Mississippi"]