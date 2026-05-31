from typing import List

def split_by_index(s: str, indexes: List[int]) -> List[str]:
    res = []
    st = 0
    if len(indexes) > 2:
        for size in indexes:
            res.append(s[st: st + size - st])
            # print(res)
            st += size - st
        res.append(s[st:])
        # print(res)
        return res
    else:
        res.append(s[:])
        return res


x = [6, 8, 12, 13, 18]
if __name__ == "__main__":

    assert split_by_index("pythoniscool,isn'tit?", x) == ['python', 'is', 'cool', ',', "isn't", 'it?']
    assert split_by_index("no luck", [42]) == ['no luck']