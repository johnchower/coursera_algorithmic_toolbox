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
