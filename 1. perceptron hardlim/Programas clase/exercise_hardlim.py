from random import choice
from numpy import array, dot, random
# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np

unit_step = lambda x: 0 if x < 0 else 1

training_data = [
    (array([0,0,1]), 0),
    (array([1,1,1]), 0),
    (array([1,5,1]), 0),
    (array([2,2,1]), 0),
    (array([2,3,1]), 0),
    (array([3,1,1]), 0),
    (array([3,2,1]), 0),
    (array([4,1,1]), 0),
    (array([1,9,1]), 1),
    (array([1,10,1]), 1),
    (array([2,8,1]), 1),
    (array([2,9,1]), 1),
    (array([3,7,1]), 1),
    (array([3,8,1]), 1),
    (array([4,6,1]), 1),
    (array([4,7,1]), 1),
    (array([5,5,1]), 1),
    (array([5,6,1]), 1),
    (array([6,3,1]), 1),
    (array([6,4,1]), 1)
]

w = random.rand(3)
errors = []
eta = 0.2
n = 1000

for i in xrange(n):
    x, expected = choice(training_data)
    result = dot(w, x)
    error = expected - unit_step(result)
    errors.append(error)
    w += eta * error * x

for x, _ in training_data:
    result = dot(x, w)
    print("{}: {} -> {}".format(x[:2], result, unit_step(result)))

#test: 
print("TEST")
test_data = [
    (array([1,3,1]), 0),
    (array([4,8,1]), 1)
]

correctas=0
for x, r in test_data:
    result = dot(x, w)
    print("{}: {} -> {}".format(x[:2], result, unit_step(result)))
    if unit_step(result) == r:
        correctas = correctas +1

porcentaje = (correctas*100) / len(test_data)
print("Tu modelo tiene un porcentaje de {} '%'  de respuestas correctas.".format(porcentaje))