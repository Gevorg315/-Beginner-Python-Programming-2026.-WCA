from typing import List, Tuple, Union

def seq_sum(sequence: Union[List, Tuple]) -> int:
    sum_ = 0
    for i in sequence:
        if type(i) == int:
            sum_ += i
        elif type(i) in [list, tuple]:
            sum_ += seq_sum(i)
    return sum_

seq = [1, 2, 3, [4, 5, (6, 7)]]
print(seq_sum(seq))
if __name__ == "__main__":
    assert seq_sum(seq) == 28