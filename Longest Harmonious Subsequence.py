class Solution:
    def findLHS(self, nums: List[int]) -> int:
        mi=min(nums)
        k=[]
        n=len(nums)
        c=nums.count(mi)
        for i in range(c):
            k.append(mi)
            nums.remove(mi)
        o=0
        r=0
        while True:#[3,2,2,5,2,3,7]
            if len(nums)==0:
                break
            mi2=min(nums)#5
            if mi2-mi==1:
                c1=nums.count(mi2)#2
                for i in range(c1):
                    k.append(mi2)#[2,2,2,3,3]
                    nums.remove(mi2)#[5,7]
                r=len(k)#5
                j=k.count(mi)
                for i in range(j):
                    k.remove(mi)#[3,3]
                mi=mi2#3
            else:
                k.clear()
                c1=nums.count(mi2)
                for i in range(c1):
                    k.append(mi2)
                    nums.remove(mi2)
                j=nums.count(mi)
                for i in range(j):
                    k.remove(mi)
                mi=mi2
            if r>o:
                o=r
                print(o)
        return o
