class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
            nums.sort()
            memo ={}
            def backtrack(current):
                
                if current > target:
                    return 0
                if current == target:
                    return 1

                
                if current in memo:
                    return memo[current]
                ctr = 0
                for i in range(len(nums)):
                    next_val = current+nums[i]
                    if next_val > target:
                        break
                    ctr += backtrack(next_val)

                memo[current] = ctr

                return memo[current]

            backtrack(0)
            return max(memo.values())