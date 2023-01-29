import numpy as np
from helper import chop, round_value, polynomial, derivative
from decimal import *

# Question 1
# old value: 0 01110000000 001111111111
# new value: 0 10000000111 111010111001
val = "010000000111111010111001"
bin_arr = np.zeros(len(val), dtype=np.uint8)

for i in range(len(val)):
    if val[i] == '1':
        bin_arr[i] = 1

# split up array
s = bin_arr[0]
c = bin_arr[1:12]
f = bin_arr[12:]

# calculate exponent
exp = 0
for i in range(len(c)):
    if c[i] == 1:
        exp += 2 ** (len(c) - i - 1)

# calculate mantissa
mantissa = 0
for i in range(len(f)):
    if f[i] == 1:
        mantissa += 0.5 ** (i + 1)

# double precision formula
answer1 = ((-1) ** s) * (2 ** (exp - 1023)) * (1 + mantissa)
print(answer1, "\n")


# Question 2

# calculate mantissa using three-digit chopping
mantissa = 0
for i in range(len(f)):
    if f[i] == 1:
        mantissa += 0.5 ** (i + 1)

exp_chop = 2 ** (exp - 1023)
mantissa = 1 + mantissa
answer2 = ((-1) ** s) * exp_chop * mantissa
print(chop(answer2), "\n")


# Question 3

# calculate mantissa using three-digit rounding
mantissa = 0
for i in range(len(f)):
    if f[i] == 1:
        mantissa += 0.5 ** (i + 1)

exp_round = 2 ** (exp - 1023)
mantissa = 1 + mantissa
answer3 = ((-1) ** s) * exp_chop * mantissa
print('{0:.1f}'.format(round_value(answer3)), "\n")

# Question 4

# Absolute error

abs_err = Decimal(abs(answer1 - round_value(answer3)))
print(abs_err)

rel_err = Decimal(abs_err) / Decimal(abs(answer1))
print('{0:.31f}'.format(rel_err), "\n")

# Question 5

tol = 10 ** -4
f_x = 1
k = 0
sum_ = 0
sign = 1

# Iterate alternating series until tolerance condition met
# Expected result should be 22
while k <= 30:
    sign = -sign
    term = (f_x / ((k + 1) ** 3))
    sum_ += sign * term
    if term < tol:
        print(k, "\n")
        break
    k += 1


# Question 6

# Solve f(x) = x^3 + 4x^2 - 10 = 0
# Nested form: ((x + 4)x)x - 10 = 0

a = -4
b = 7
i = 1
fa = (a + 4) * a * a - 10

# a) Bisection method
while i <= 30:
    p = (a + b) / 2
    fp = (p + 4) * p * p - 10
    if p == 0 or (b - a) /2 < tol:
        print(i, "\n")
        break
    i += 1
    if np.sign(fa) == np.sign(fp):
        a = p
    else:
        b = p

# b) Newton-Raphson method
initial_approx = -4
i = 0
fa = polynomial(initial_approx)
f_prime = derivative(initial_approx)

approx = fa / f_prime
while i <= 40:
    if abs(approx) <= tol:
        print(i, "\n")
        break
    fa = polynomial(initial_approx)
    f_prime = derivative(initial_approx)
    approx = fa / f_prime
    initial_approx -= approx
    i += 1

