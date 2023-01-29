# Author: Zoey Vail

import numpy
rng = numpy.random.default_rng()
rnd = []
for i in range(10):
    n = rng.random()
    rnd.append(n)
print("Random numbers: ")
for i in rnd:
    print(i)
mn = numpy.mean(rnd)
print ("Mean: ", mn)
mdn = numpy.median(rnd)
print("Median: ", mdn)
dev = numpy.std(rnd)
print("Standard deviaton: ", dev)