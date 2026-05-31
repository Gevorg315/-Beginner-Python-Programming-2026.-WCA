from typing import List

def check(row_start: int, row_end: int, column_start: int, column_end: int) -> List[List[int]]:
    x = range(row_start, row_end + 1)
    y = range(column_start, column_end + 1)
    mult_table = [[i * j for j in y] for i in x]
    return mult_table

print(check(2,4,3,7))

if __name__ == "__main__":

    assert check(2, 4, 3, 7) == [[6, 8, 10, 12, 14], [9, 12, 15, 18, 21], [12, 16, 20, 24, 28]]