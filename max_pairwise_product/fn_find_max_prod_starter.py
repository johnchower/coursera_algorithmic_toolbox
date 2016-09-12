def find_max_prod_starter(n,a):
    result = 0

    for i in range(0,n):
        for j in range(i+1,n):
            if a[i]*a[j] >  result:
                result = a[i]*a[j]

    return result
