class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k=nums.count(0)
        for i in range(k):
            nums.remove(0)
            nums.append(0)
        """
        Do not return anything, modify nums in-place instead.
        """
