from typing import Dict

def combine_dicts(*args: Dict[str, int]) -> Dict[str, int]:
    new_dictionary = {}

    for dictionary in args:
        for key, value in dictionary.items():

            if key not in new_dictionary:
                new_dictionary[key] = value
            else:
                new_dictionary[key] += value

    return new_dictionary


dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combine_dicts(dict_1, dict_2))
print(combine_dicts(dict_1, dict_2, dict_3))

if __name__ == "__main__":
    assert combine_dicts(dict_1, dict_2) == {
        'a': 300,
        'b': 200,
        'c': 300
    }

    assert combine_dicts(dict_1, dict_2, dict_3) == {
        'a': 600,
        'b': 200,
        'c': 300,
        'd': 100
    }