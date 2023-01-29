# Author: Zoey Vail

import time

start = time.time()
n = int(input("Enter a number between 15 and 35 inclusive: "))
fibArr = []
for i in range(n):
    if (len(fibArr) < 2):
        fibArr.append(i)
    else:
        fibArr.append(fibArr[i - 1] + fibArr[i - 2])
print("fib[",n,"] = ", fibArr[n-1])
print()
end = time.time()
print("fib[",n,"] took ", end - start, " seconds")
