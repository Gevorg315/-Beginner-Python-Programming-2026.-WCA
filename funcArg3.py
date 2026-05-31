def union(*args) -> set:
    my_set = set()
    for arg in args:
        my_set.update(arg)
    return my_set

def intersect(*args) -> set:
    my_list = list(set(arg) for arg in args)
    result = set(args[0])
    for s in my_list:
        result = result.intersection(s)
    return result

if __name__ == "__main__":
    assert union(('S', 'A', 'M'), ['S', 'P', 'A', 'C']) == {'S', 'P', 'A', 'M', 'C'}
    assert intersect(('S', 'A', 'C'), ('P', 'C', 'S'), ('G', 'H', 'S', 'C')) == {'S', 'C'}