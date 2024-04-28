import numpy as np
import searchUtilsTeam01 as search

sortd  = np.array([1,2,3,5,7,11,13,17,19,23,29])
usortd = np.array([23,13,7,5,11,3,29,2,17,1,19])

print()
print("\nThe sorted array that will be analyzed:")
print(sortd)

x1l = search.searchutils.linearsearch(sortd,11)
x1b = search.searchutils.binarysearch(sortd,11)

print("Using Linear Search, the index that contains the value \"11\" is {0}".format(x1l))
print("Using Binary Search, the index that contains the value \"11\" is {0}".format(x1b))

print("\nThe unsorted array that will be analyzed:")
print(usortd)

x2l = search.searchutils.linearsearch(usortd,11)
x2b = search.searchutils.binarysearch(usortd,11)

print("Using Linear Search, the index that contains the value \"11\" is {0}".format(x2l))
print("Using Binary Search, the index that contains the value \"11\" is {0}".format(x2b))


print("\n")
