# from memory_profiler import profile

# @profile
def find_max_prod(n,a):
    top = 0
    top2 = 0
    
    for i in range(0, n):
        if a[i] >= top:
            top = a[i]
        elif a[i] >= top2 and a[i] < top:
            top2 = a[i]
    
    result = top*top2
    return [result, top, top2]
