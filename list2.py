def get_fizzbuzz_list(n: int) -> list:
    ls = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            ls.append("FizzBuzz")
            continue
        elif i % 3 == 0:
            ls.append("Fizz")
            continue
        elif i % 5 == 0:
            ls.append("Buzz")
            continue
        ls.append(i)
    return ls

print(get_fizzbuzz_list(10))
if __name__ == "__main__":

    assert get_fizzbuzz_list(10) == [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz']