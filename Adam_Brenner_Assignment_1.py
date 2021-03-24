## Assignment 1 ##
# Adam Brenner #

import pandas as pd
import numpy as np

# Part 1

print("Part 1 \n")

elements = pd.read_csv(r"C:\Users\ajbre\Documents\2021 Winter Quarter\Data Visualization\Elements.csv")

print(elements, "\n")

new_row = {'Name':'Fluorine', 'Symbol':'F', 'Atomic Number':9}
new_row2 = {'Name':'Neon', 'Symbol':'Ne', 'Atomic Number':10}

elements = elements.append(new_row, ignore_index=True)
elements = elements.append(new_row2, ignore_index=True)

atomic_weight = [1.008, 4.0026, 6.94, 9.0122, 10.81, 12.011, 14.007, 15.999, 18.998, 20.180]
atomic_weight_round = [round(num) for num in atomic_weight]

elements['Atomic Weight'] = atomic_weight_round

print(elements, "\n")

# Part 2

print("Part 2 \n")

greek_letters = ['epsilon', 'rho', 'sigma', 'gamma', 'omega', 'zeta', 'lambda', 'delta', 'alpha']

rand1 = np.random.normal(10, 1.5, 9)
rand2 = np.random.normal(10, 1.5, 9)

angle = (2*np.pi) * np.random.random_sample((3,3))

cosine = np.cos(np.array([num for num in angle]))

dict1 = {'Greek Letters': greek_letters, 'Random 1': rand1, 'Random 2': rand2, 'Angle': angle, 'Cosine Angle': cosine}

dataframe2 = pd.DataFrame([dict1])

dataframe2 = dataframe2.explode('Greek Letters')
print(dataframe2)

dataframe2 = dataframe2.sort_values(by=['Greek Letters'])

dataframe2 = dataframe2.reset_index(drop=True)

#Drop 2 columns, Random 1 and Angle, and 1 row, row 3.
dataframe2 = dataframe2.drop(columns = ['Random 1', 'Angle'])
dataframe2 = dataframe2.drop([3])

print(dataframe2)

# Part 3

print("Part 3 \n")
def fibonacci():
    fib1 = [0 for i in range(12)]
    fib1[0] = 1
    print(fib1[0])
    fib1[1] = 1
    print(fib1[1])
    for i in range(2, len(fib1)):
        fib1[i] = fib1[i-2] + fib1[i-1]
        print(fib1[i])
    fibrat = []
    for j in range(11, 6, -1):
        fibrat.append(fib1[j] / fib1[j-1])
    print("Ratio of Predecessor: ", fibrat, "\n")

fibonacci()

# Part 4

print("Part 4 \n")

def rankine(x):
    return (x * (9/5))

kelvin = [100, 130, 160, 190, 220]

for k in kelvin:
    print(rankine(k))

print("Lambda: ", [(lambda x : x * (9/5))(x) for x in kelvin])
