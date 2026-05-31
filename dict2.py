from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    u_value = set(val for dic in lst for val in dic.values())
    return u_value

ls = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
      {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
print(check(ls))
if __name__ == "__main__":

    assert check(ls) == {'S007', 'S001', 'S002', 'S009', 'S005'}