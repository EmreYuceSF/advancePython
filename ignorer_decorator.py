import random

def ignorer_decorator(func):
    def inner(*args):
        #randomly ignore arguments with 50% change and store the rest in a list with list comprehension method, 
        #then unpack the list with "*" in to the func() as parameter
        func(*(arg for arg in args if 1 == random.choice([0,1])))
    return inner



print("Before decorating the print function ->", 0,1,2,3,4,5,6,7,8,9,10) # demonstration purposes
print("After decorating the print function  -> ", end="") # demonstration purposes

print = ignorer_decorator(print) # the print function is decorated and its behavior it is changed forever in this program

print(0,1,2,3,4,5,6,7,8,9,10) # demonstration purposes


