#!/usr/bin/python

import functools

"""
map (fn, x) takes items in container makes new container
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

#filter

forfilter = [i for i in range(4)]
fnfilter = lambda x:  x >2
maxifhigher = list(filter(fnfilter, forfilter))
print(maxifhigher)
