import sys

input = sys.stdin.read()
tokens = input.split()

n = int(tokens[0])

if n <= 1:
    print(n)
else:
    back1 = 0
    current_fib = 1
    for i in range(n-1):
        newback1 = current_fib
        current_fib = current_fib + back1
        back1 = newback1
    print(current_fib)
        
   
