#Emre Yuce CS231
#Write a functional-style program (ideally only one statement long) that displays the curvature of a sinusoid

from functools import reduce
from math import sin 

distance = 180 #length of x axis

col = distance+1
row = distance+1
center_row = row//2 # Starting from the middle for assigning coordinates to the matrix, as coordinates extend in both negative and positive directions
center_col = col//2

matrix = [[" " for _  in range(col)] for _ in range(row)] #creating a matrix to visualize curvature of a sinusoid
    

factorial = lambda num: reduce(lambda x,y: x*y, range(1, num+1)) # Factorial function, originally intended for a custom sin() function, is not used in this code.

def create_listX(distance):
    return ([num/10 for num in range(int(-distance/2), int(distance/2)+1)])  # Creating a list of decimal values for the x-axis

def create_listY(x_list):
    return list(map(lambda y: round(sin(y), 1), x_list)) # Creating y-axis coordinates for each x value from x_list, rounded to one decimal place for visualization. (keeping closer to integer)


coordinates = (zip(create_listX(distance), create_listY(create_listX(distance))))  # storing coordinates as a tuple together (x, y)



for x,y in coordinates: # I could not make this, one-line code 
    matrix[center_col + int(10*y)][center_row + int(10*x)] = "*" # multiplying with ten both x and y to make them integer is make assigning this numbers on matrix possible 


for i in range(center_row-20, center_row+21): #  curvature of a sinusoid can not go higher than 1 or lower than -1 that is why we dont need to print all the y axis 
    print(matrix[i]) 
    
    
"""  def sin(x, precision):  
r = x * 3.14 / 180
res = 0
operator = 1
for i in range(1, precision, 2):
    res += (r ** i) / factorial(i) * operator
    operator *= -1
return round(res, 2)  """ # I've spent a lot of time working on this simple function, but I haven't been able to achieve the results. I would appreciate it if you could tell me what is wrong and help me fix it.
    

