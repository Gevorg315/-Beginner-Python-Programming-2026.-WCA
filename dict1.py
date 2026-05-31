from typing import Dict

def get_dict(s: str) -> Dict[str, int]:
    myDict = {}
    for i in s.lower():
        if i in myDict:
            myDict[i] += 1
        else:
            myDict[i] = 1
    myKeys = list(myDict.keys())
    myKeys.sort()
    sorted_dict = {i: myDict[i] for i in myKeys}
    return sorted_dict

s = 'Oh, it is python'
print(get_dict(s))
if __name__ == "__main__":

    assert get_dict(s) == {' ': 3, ',': 1, 'h': 2, 'i': 2, 'n': 1, 'o': 2, 'p': 1, 's': 1, 't': 2, 'y': 1}