#Using the Numpy for calc as roots-----------------------------------------
import numpy as np

#Functions for calc as roots of the equation second degree-----------------
def calc_roots(rootA, rootB, rootC):

    #Equation Coefficient--------------------------------------------------
    cofficient = [rootA, rootB, rootC]

    #Using numpy.roots for calc roots--------------------------------------
    roots = np.roots(cofficient)
    return roots

#Requesting Cofficients The User------------------------------------------
rootA = float(input('Enter the cofficient A: '))
rootB = float(input('Enter the cofficient B: '))
rootC = float(input('Enter the cofficient C: '))

#Calc Roots---------------------------------------------------------------
roots = calc_roots(rootA, rootB, rootC)

#Print The Result---------------------------------------------------------
print(f'The Roots of The Equation are: {roots[0]} is {roots[1]}')

#Example02----------------------------------------------------------------
import matplotlib.pyplot as plt
x = np.array(['A','B','C','D'])
y = np.array([3,8,1,10])

plt.bar(x, y)
plt.show()

#Example03----------------------------------------------------------------
#To generate Thousand Points Following and Normal Distribution
#With Average Twenty Divert Standard Two
#Display in a Histogram
#Use Import --matplotlib.pyplot-- and Import --numpy--
np.random.seed(1)
data = np.random.normal(loc = 20, scale = 2, size = 1000)
print(data)

plt.hist(data, color = 'lightblue', edgecolor = 'black')
plt.show()
