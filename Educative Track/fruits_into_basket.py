'''
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Example 2:

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
'''



def basketcheck(chrs):
    bask = {}
    win_start = 0
    win_end = 0
    maxlen = float("-inf")

    for win_end in range(len(chrs)):
        right_fruit = chrs[win_end]
        if right_fruit not in bask:
            bask[right_fruit] = 0
        bask[right_fruit] += 1

        while len(bask) > 2:
            left_fruit = chrs[win_start]
            bask[left_fruit] -= 1
            if bask[left_fruit] == 0:
                del bask[left_fruit]
            win_start += 1
        maxlen = max(maxlen,win_end-win_start+1)
    return maxlen

# def basketcheck(chrs):
#     basket = {}
#     win_start, win_end = 0,0
#     maxlen = float("-inf")

#     for i in range(len(chrs)):
#         if chrs[win_end] not in basket:
#             basket[chrs[win_end]] = 0
#         basket[chrs[win_end]] += 1

#         while len(basket) > 2:
#             fr = chrs[win_start]
#             basket[fr] -= 1

#             if basket[fr] == 0:
#                 del basket[fr]
#             win_start += 1
#         maxlen = max(maxlen,sum(basket.values())) 
            
#         win_end += 1
#     return maxlen





print(basketcheck(['A','B','C','A','C'])) #3
print(basketcheck(['A', 'B', 'C', 'B', 'B', 'C'])) #5
