def fun(nums,k):	
	container = {0: -1}
    curr = 0
        
	for i, num in enumerate(nums):
		curr = (curr + num) % k
		if curr in container:
		    if i - container[curr] >= 2:
				return True
		else:
			container[curr] = i
	return False

    #     if curr in container:
    #         if i - container[curr] >= 2:
	# 		    return True
    #     else:
	# 	    container[curr] = i
	# return False

fun([23,2,4,6,7],6)