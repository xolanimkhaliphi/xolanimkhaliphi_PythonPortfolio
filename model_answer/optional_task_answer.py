import numpy as np
import matplotlib.pyplot as plt

# Create a sequence of numbers going from 0 to 100 in intervals of 0.5
start_val = -100
stop_val = 100
n_samples = 200
X = np.linspace(start_val, stop_val, n_samples)

params = [1.2, 0.5, 2, -5]

"""
-----------------
Optional Task
------------------

Plot f(x) = P.X, where p is your params
"""

def generate_straight_line(X, params=np.array([0.5, 2, -5])):
    X_input = np.empty((params.shape[0], X.shape[0]))

    for i in range(X_input.shape[0] ):
        X_input[i] = X ** (len(params) - i)

    return np.dot(params, X_input)




plt.figure()
plt.plot(X, generate_straight_line(X))
plt.title("f(x) = 1.2x^3 + 0.5x^2 + 2x - 5")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("optional_answer.png")

