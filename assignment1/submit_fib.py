import sys
import fibonacci_functions

input = sys.stdin.read()
tokens = input.split()

n = int(tokens[0])
print(fibonacci_functions.fib(n))
