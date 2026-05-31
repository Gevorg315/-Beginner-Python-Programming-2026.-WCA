from typing import Any, Tuple, List

def get_pairs(l: List[Any]) -> List[Tuple[Any, Any]]:
    if len(l) > 1:
        t = zip(l[0::1], l[1::1])
        ls = list(t)
        return ls
    return []

lst = ['need', 'to', 'sleep', 'more']

print(get_pairs(lst))
if __name__ == "__main__":
    assert get_pairs(lst) == [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]