# def check_str(s: str):
    # if s != "":
    #     import re
    #     s = re.sub("[^A-Za-z]", "", s).lower()
    #     first, last = 0, len(s) - 1
    #     while first < last:
    #         if s[first] == s[last]:
    #             first += 1
    #             last -= 1
    #         else:
    #             return False
    #     return True
    # else:
    #     return None

    # import re
    # if s != "":
    #     s = re.sub("[^A-Za-z]", "", s).lower()
    #     for index, _char in enumerate(s):
    #         if s[index] != s[-index - 1]:
    #             return False
    #     return True
    # else:
    #     return None

import re

def check_str(s: str):
    if s == "":
        return None
    s = re.sub(r"[^A-Za-z]", "", s).lower()
    for index in range(len(s) // 2):
        if s[index] != s[-index - 1]:
            return False
    return True

if __name__ == "__main__":
    assert check_str("A dog! a panic in a pagoda!")
    assert not check_str("A dog! a panichgin a pagoda!")
    assert check_str("") is None
    assert check_str("Hannah")

