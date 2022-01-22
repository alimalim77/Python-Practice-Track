'''
we will be considering the so-called “Look-and-Say” sequence. The first few terms of the sequence are:

1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ... 

Now, you can easily guess the sixth term. There you go:

111221 is read off as "three 1s, two 2s, then one 1" or 312211.
'''


def fun(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])
        i += 1
    return ''.join(result)

a= fun(str(11233311))
print(a)