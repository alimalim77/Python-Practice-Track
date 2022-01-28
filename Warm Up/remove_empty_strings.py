'''
Exercise 14: Remove empty strings from a list of strings
Given:
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
Expected Output:
Original list of sting
['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']
 
After removing empty strings
['Emma', 'Jon', 'Kelly', 'Eric']

'''
def fun(*name):
    li = list(filter(None,name))
    print(li)





fun("Emma", "Jon", "", "Kelly", None, "Eric", "")

#using arbitrary arguments and filter function