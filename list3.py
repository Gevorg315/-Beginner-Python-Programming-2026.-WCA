# from typing import List
#
# def foo(nums: List[int]) -> List[int]:
#     prod = 1
#     flag = 0
#     for i in range(len(nums)):
#         if nums[i] == 0:
#             flag += 1
#         else:
#             prod *= nums[i]
#     arr = [0 for _ in range(len(nums))]
#     for i in range(len(nums)):
#         if flag > 1:
#             arr[i] = 0
#         elif flag == 0:
#             arr[i] = (prod // nums[i])
#         elif flag == 1 and nums[i] != 0:
#             arr[i] = 0
#         else:
#             arr[i] = prod
#     return arr
#
#
# array = [1, 2, 3, 1, 5]
# ans = foo(array)
# print(ans)
# if __name__ == "__main__":
#
#     assert foo(array) == [30, 15, 10, 30, 6]


# from typing import List
#
# def foo(nums: List[int]) -> List[int]:
#     zero_count = nums.count(0)
#
#     if zero_count > 1:
#         return [0] * len(nums)
#
#     prod = 1
#     for num in nums:
#         if num != 0:
#             prod *= num
#
#     return [
#         0 if zero_count == 1 and num != 0
#         else prod if num == 0
#         else prod // num
#         for num in nums
#     ]
#
#
# array = [1, 2, 3, 1, 5]
# print(foo(array))

from typing import List

def foo(nums: List[int]) -> List[int]:
    zeros = nums.count(0)
    prod = 1

    for x in nums:
        if x:
            prod *= x

    return [
        0 if zeros > 1 else
        prod if x == 0 else
        prod // x if zeros == 0 else 0
        for x in nums
    ]

array = [1, 2, 3, 1, 5]
print(foo(array))