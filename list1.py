from typing import List


def sort_unique_elements(str_list: List[str]) -> List[str]:
    result = list(sorted(set(str_list)))
    print(result)
    return result


str_l = ['red', 'white', 'black', 'red', 'green', 'black']

if __name__ == "__main__":
    assert sort_unique_elements(str_l) == ['black', 'green', 'red', 'white']
