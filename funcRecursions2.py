from typing import Any, List

def linear_seq(sequence: List[Any]) -> List[Any]:
    gather = []
    for item in sequence:
        if isinstance(item, (list, tuple, set)):
            gather.extend(linear_seq(item))
        else:
            gather.append(item)
    return gather

nested = [1, 2, 3, [4, 5, (6, 7)]]
print(list(linear_seq(nested)))
if __name__ == "__main__":
    assert list(linear_seq(nested)) == [1, 2, 3, 4, 5, 6, 7]