# Uses python3
from fn_find_max_prod import find_max_prod
from memory_profiler import profile
import psutil

# @profile
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = find_max_prod(n,a)  
print(result)
