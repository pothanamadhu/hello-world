class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected=heights.copy()
        expected.sort()
        k=0
        for i in range(len(heights)):
            if heights[i]!=expected[i]:
                k=k+1
        return k
