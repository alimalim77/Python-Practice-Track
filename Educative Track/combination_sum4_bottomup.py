class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {0:1}
        for i in range(1,target+1):
            cache[i] = 0
            for n in nums:
                cache[i] += cache.get(i-n,0)
        return cache[target]
            