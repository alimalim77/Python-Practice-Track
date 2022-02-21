def validMountainArray(arr):
        if len(arr) < 3:
            return False
        flag = 0
        if arr[0] > arr[1]:
            return False
        for i in range(1,len(arr)):
            if arr[i] == arr[i-1]:
                return False
            if arr[i] > arr[i-1] and flag == 0:
                continue
            elif flag == 1 and arr[i] <  arr[i-1]:
                continue
            else:
                flag += 1
        print(flag)
validMountainArray([9,8,7,6,5,4,3,2,1,0])