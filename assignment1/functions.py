import math

def quotient_remainder(n,d):
    q = int(n/d)
    r = n - d*q
    return([q,r])

def gcd(a,b):
    dividend = a
    divisor = b
    qr = quotient_remainder(dividend,divisor)
    quotient = qr[0]
    remainder = qr[1]
    while remainder > 0:
        dividend = divisor
        divisor = remainder
        qr = quotient_remainder(dividend,divisor)
        quotient = qr[0]
        remainder = qr[1]
    return int(divisor)
        
def lcm(a,b):
    g = gcd(a,b)
    out = a*b/g
    return int(out)

def fib(n):
    fiblist = [0,1]
    if n <= 1: 
        out = n
    else:
        for i in range(2,n+1):
            newfib = fiblist[i-2] + fiblist[i-1] 
            fiblist.append(newfib)
        out = fiblist[-1] 
    return out

# Make a function here called create_pattern
# Inputs: m - a modulus, and n - a cuttoff point
# This function will generate a list of all Fibonacci numbers, mod m
# It will stop under one of 2 conditions:
    # 1. We've produced the nth Fibonacci number mod m
    # 2. The list has repeated (ie reached the pattern m-1, 1)
# The function will then return:
    # A flag telling the user why the exit was made.
    # The list that was produced.

def create_pattern(m, n=math.inf, zeroth = 0, first = 1):
    fiblist = [zeroth, first]
    i = 1
    pattern_repeats = False
    while (i < n) & (not pattern_repeats):
        newfib = fiblist[i-1] + fiblist[i] 
        newfib = quotient_remainder(newfib, m)[1]
        fiblist.append(newfib)
        is_zeroth = (fiblist[i] == zeroth)
        is_first = (fiblist[i+1] == first)
        pattern_repeats = is_zeroth & is_first
        i += 1

    if pattern_repeats:         
        out1 = fiblist[0:-2]
    else:
        out1 = fiblist

    return [pattern_repeats, out1]

pattern_fib_10 = create_pattern(10)[1]

def fibmod10(n):
    if n < 60:
        out = pattern_fib_10[n]
    else:
        nmod60 = quotient_remainder(n, 60)[1]
        out = pattern_fib_10[nmod60]
    return out

def fibmod(n,m):
    if n <= 1:
        out = n
    else:
        out = 3
    return out 

