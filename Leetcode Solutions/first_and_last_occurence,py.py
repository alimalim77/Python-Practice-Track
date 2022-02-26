def searchRange(nums, target):
        if nums == [] or target not in nums:
            print([-1,-1])
        ini = 0
        tot = len(nums)
        mid = (ini+tot)//2
        
        pos1 = 0
        pos2 = 0
        while ini <= tot:
            if nums[mid] == target:
                lower = mid -1
                if mid == 0 or nums[lower] != target:
                    pos1 = mid
                    break
                tot = mid-1
                mid = (ini+tot)//2
                    
            if target < nums[mid]:
                tot = mid -1
                mid = (ini+tot)//2
            elif target > nums[mid]:
                ini = mid+1
                mid = (ini+tot)//2
            
        
        ini = 0
        tot = len(nums)
        mid = (ini+tot)//2
        while ini <= tot:
            if nums[mid] == target:
                upper = mid+1
                if mid == len(nums)-1 or nums[upper] != target:
                    pos2 = mid
                    break
                ini = mid + 1
                mid = (ini+tot)//2
            
            if target < nums[mid]:
                tot = mid -1
                mid = (ini+tot)//2
            elif target > nums[mid]:
                ini = mid+1
                mid = (ini+tot)//2
        print([pos1,pos2])

searchRange( [5,7,7,8,8,10], 8)