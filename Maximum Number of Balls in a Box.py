class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def count(n):
            s=0
            while n:
                r=n%10
                n=n//10
                s=s+r
            return s
        d={}
        for i in range(lowLimit,highLimit+1):
            k=count(i)
            if k not in d.keys():
                d[k]=1
            else:
                d[k]+=1
        return max(d.values())
