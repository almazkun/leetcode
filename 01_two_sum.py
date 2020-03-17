class Solution:
    def gen(self, nums, target):
        for i, A in enumerate(nums, 0):
            for k, B in enumerate(nums[i + 1:], i + 1):
                if target - A == B:
                    yield list((i, k))
                    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a in self.gen(nums, target):
            return a
