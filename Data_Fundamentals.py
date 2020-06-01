import numpy as np
import matplotlib.pyplot as plt

#The code below creates a graph using the matplotlib.pyplot library

steps, repeats = 100, 10
stepstaken = 0.01 * np.random.randn(steps, repeats)
positions = stepstaken.cumsum(axis = 0)
plt.plot(positions);
plt.xlabel('time');
plt.ylabel('position');
#plt.show();

# Using Python as a calculator
x = 1
y = 2
print (x+y) # This code prints the x+y = 3

# No need to specify a variable type.
my_val = 8.25
print(my_val)
print(my_val + 5)
print(my_val * 5)
my_val += 5
print(my_val)

my_new_val = abs(-5)
print(my_new_val)

# List data types

my_list = ["it's", True, 'we can hold it', False, ['lists of',['lists']], 10 ]

for item in my_list:
    print (item+item)


