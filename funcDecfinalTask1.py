from typing import List

def split(data: str, sep=None, maxsplit=-1) -> List[str]:
    if maxsplit == 0:
        return [data.strip()] if sep is None else [data]
    if sep is None:
        result = []
        word = ""
        splits = 0
        for index, char in enumerate(data):
            if char.isspace():
                if word:
                    result.append(word)
                    word = ""
                    splits += 1
                    if maxsplit != -1 and splits >= maxsplit:
                        rest = data[index + 1:].strip()
                        if rest:
                            result.append(rest)
                        return result
            else:
                word += char
        if word:
            result.append(word)
        return result
    # custom separator
    result = []
    current = ""
    i = 0
    splits = 0
    while i < len(data):
        if (
            data[i:i + len(sep)] == sep and
            (maxsplit == -1 or splits < maxsplit)
        ):
            result.append(current)
            current = ""
            i += len(sep)
            splits += 1
        else:
            current += data[i]
            i += 1
    result.append(current)
    return result

print(split('    Hi     Python    world!'))
print(split('a,b,c', ','))
print(split('a,b,c,d', ',', 2))
print(split('asdf 5 7', None, 0))
print(split('asdf 5 7', None, 1))
print(split('adf 5 7', None, 1))

if __name__ == "__main__":
    assert split('    Hi     Python    world!') == ['Hi', 'Python', 'world!']
    assert split('a,b,c', ',') == ['a', 'b', 'c']
    assert split('a,b,c,d', ',', 2) == ['a', 'b', 'c,d']
    assert split('asdf 5 7', None, 0) == ['asdf 5 7']
    assert split('asdf 5 7', None, 1) == ['asdf', '5 7']
    assert split('adf 5 7', None, 1) == ['adf', '5 7']