import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    p=[]
    a=np.sum(np.exp(L))
    for i in L:
        p.append(np.exp(i)/a)
    return(p) 
