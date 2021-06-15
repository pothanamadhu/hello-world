class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d={}
        f=0
        for i in nums:
            if i not in d.keys():
                d[i]=1
            else:
                d[i]+=1
        for k,v in d.items():
            if v==1:
                f=f+k
        return f
