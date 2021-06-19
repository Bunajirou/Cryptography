import sympy
import math

max_prime = int(input('maximum prime?= '))
min_prime = int(input('minimum prime?= '))

p = sympy.randprime(min_prime, max_prime)
q = sympy.randprime(min_prime, max_prime)
while(p == q):
    q = sympy.randprime(min_prime, max_prime)

n = p * q
L = math.lcm(p-1, q-1)
max = max(p, q)
e = sympy.randprime(max+1, L)

print('p={0}\nq={1}\nn={2}\ne={3}'. format(p, q, n, e))