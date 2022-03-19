'''
You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.
Input: nums = [3,2,3,2,2,2]
Output: true
Explanation: 
There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.
'''
from typing import Counter


def numsarray(nums):
    if len(nums) % 2 != 0:
        return False
    nums.sort()
    a  = Counter(nums)
    print(a)
    for i,j in a.items():
        if j % 2 != 0:
            return False
    return True

print(numsarray([1,2,1,2]))