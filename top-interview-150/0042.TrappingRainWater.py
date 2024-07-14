class Solution:
    def trap(self, height: List[int]) -> int:
        maxlarr = [None]*len(height)
        maxrarr = [None]*len(height)
        maxl = 0
        maxr = 0
        maxlarr[0] = 0
        for i in range(1,len(height)):
            maxl = max(maxl, height[i-1])        
            maxlarr[i] = maxl       
        maxrarr[len(height)-1] = 0   
        for i in range(len(height)-2,-1,-1):
            print(i)
            maxr = max(maxr, height[i+1])        
            maxrarr[i] = maxr
        total = 0
        for i in range(len(height)):
            val = min(maxrarr[i], maxlarr[i]) - height[i]
            if val > 0:
                total += val
        return total
