#!/usr/bin/python

import functools

"""
map (fn, x) takes items in container makes new container, applies function to sequence
reduce(fn, x) makes single object
filter(fn, x)
"""

maplist = [1,2,3]

mapfn = lambda x: x+4
complete = list (map(mapfn, maplist))

print(complete)

mapstring = "hello"
strmap = lambda s:s.swapcase()
comsr = list(map(strmap, mapstring))

print(comsr)

countwrd = ["the", "stuff"]
count = lambda w:len(w)
comc = list(map(count, countwrd))

print(comc)

ordinal = map(ord, "ordinal values for these words")
lo = [i for i in ordinal]
print(lo)

#with two parameters

x = [1,2,3,4]
y = [3,4,3,4]

dalamd = lambda a, b: a*b
times = list(map(dalamd, x,y))
print(times)

forreduce = (1,2,3)
fn = lambda x,y: x if x>y else y
thisvar = (functools.reduce(fn,forreduce))
print(thisvar)

#filter, returns only if true

forfilter = [i for i in range(4)]
fnfilter = lambda x:  x >2
maxifhigher = list(filter(fnfilter, forfilter))
print(maxifhigher)

positiveNumbers = lambda x: x>0
fpF = [1,-3,5,-7]
returnsPositive = list(filter(positiveNumbers, fpF))
print(returnsPositive)




