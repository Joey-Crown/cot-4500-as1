# Helpful utility functions for answering assignment questions
import numpy as np

# normalizes decimal value and returns three-digit chop
def chop(x):
    num = "{:.3e}".format(x).split('e')
    coeff = float(num[0]) / 10
    base = int(num[1]) + 1
    return np.floor(coeff * (10 ** base))


# normalizes decimal value and returns three-digit rounding
def round_value(x):
    num = "{:.3e}".format(x).split('e')
    coeff = float(num[0]) / 10
    base = int(num[1]) + 1
    return round(coeff, 3) * (10 ** base)


def polynomial(x):
    return (((x + 4) * x) * x) - 10


def derivative(x):
    return (3 * x * x) + (8 * x)

