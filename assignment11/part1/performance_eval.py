import numpy as np
import searchUtilsTeam01 as search
import time as tm

print()

arr = np.linspace(-10,10,10**7)
x = arr[-2]
idx = 10**7-1


#searching using LinearSearch
t_0 = tm.time()
indl = search.searchutils.linearsearch(arr,x)
t_f = tm.time()
tlin = t_f-t_0
print(f"It took linearsearch {tlin:2.10E} seconds to find the value {x} at index {idx}")


#searching using BinearSearch
t_0 = tm.time()
indb = search.searchutils.binarysearch(arr,x)
t_f = tm.time()
tbin = t_f-t_0
print(f"It took binarysearch {tbin:2.10E} seconds to find the value {x} at index {idx}")


#searching using np.searchsorted
t_0 = tm.time()
indns = np.searchsorted(arr,x)
t_f = tm.time()
tnumps = t_f-t_0
print(f"It took numpy.searchsorted() {tnumps:2.6E} seconds to find the value {x} at index {idx}")



print()
