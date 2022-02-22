def maxArea(height):
        left  = 0
        right = len(height) -1
        maxnum = 0
        
        while left < right:
            maxnum = max(maxnum, min(height[left],height[right]) * (right-left))
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        print(maxnum)
maxArea([1,8,6,2,5,4,8,3,7])