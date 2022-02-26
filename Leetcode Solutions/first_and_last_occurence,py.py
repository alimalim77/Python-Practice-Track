def searchRange(nums , target):
        ini = 0
        mid = len(nums)//2
        tot = len(nums)
        pos1 = 0
        pos2 = 0
        while ini <= tot:
            if nums[mid] == target:
                if mid == 0 or nums[mid-1] != target:
                    pos1 = mid
                    break
                tot = mid-1
                    
            if target < nums[mid]:
                tot = mid -1
                mid = (ini+tot)//2
            elif target > nums[mid]:
                ini = mid+1
                mid = (ini+tot)//2
            
        
        ini = 0
        mid = len(nums)//2
        tot = len(nums)
        while ini <= tot:
            if nums[mid] == target:
                if mid == len(nums)-1 or nums[mid+1] != target:
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
            
        print(pos1,pos2)

searchRange( [5,7,7,8,8,10], 8)