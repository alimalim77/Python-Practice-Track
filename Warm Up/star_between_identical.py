# def recfun(index,string,final):
#     if index == final:
#         return string
#     if 0 < index < final and string[index-1] == string[index]:
#          return recfun(index+1, string[:index] + "*" + string[index:], final+1)
#     return recfun(index +1, string, final)

# mystr = "abccbbaff"
# print(recfun(0,mystr,len(mystr)))


# def recfun(index,string,final):
#     if index == final:
#         return string
#     if 0 < index < final and string[index-1] == string[index]:
#         string.insert(index,"*")
#         return recfun(index+1, string, final+1)
#     return recfun(index +1, string, final)

# mystr = "abccbbaff"
# print(recfun(0,list(mystr),len(mystr)))