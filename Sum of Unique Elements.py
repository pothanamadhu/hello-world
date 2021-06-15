class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        k=0
        for i in nums:
            if nums.count(i)==1:
                k=k+i
        return k
