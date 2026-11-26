import sys

print(f"python {sys.version}")

import numpy as n

print(f"Numpy {n.__version__}")
a = n.array([1,2,3])
print(f"Vector: {a}, dot product with itself: {n.dot(a,a)}")