
import numpy as np

T = np.array([[0,1/2,1/2,0,0],
                  [1/2,0,0,0,1/2],
                  [1/2,0,0,1/2,0],
                  [0,0,0,1/2,1/2],
                  [0,0,0,1/2,1/2]])


x=np.array([[0,0.5,0,0.5,0,0,0,0,0]
,[1/3,0,1/3,0,1/3,0,0,0,0]
,[0,0.5,0,0,0,0.5,0,0,0]
,[1/3,0,0,0,1/3,0,1/3,0,0]
,[0,0.25,0,0.25,0,0.25,0,0.25,0]
,[0,0,1/3,1/3,0,0,0,0,1/3]
,[0,0,0,0.5,0,0,0,0.5,0]
,[0,0,0,1/3,0,1/3,0,0,1/3]
,[0,0,0,0,0,0,0,0,1]

])

def get_stationary(s,n):
    row = n
    pi = np.full((1, row), 1 / row)
    
    while True:
        new_pi = np.dot(pi, s)
        if np.allclose(pi, new_pi):
            pi_rounded = np.round(pi, 2)
            return pi_rounded 
            break
        pi = new_pi

print(get_stationary(T,5))




def get_transition(s,n):
   
    K = s
    for i in range(n) :
        new_pi = np.dot(K,s)
        K = new_pi
       
        pi_roundeds = np.round(K, 2)
    return pi_roundeds 
           
print(get_transition(x,15))

def get_n(s):
    n=0
    K = s
    while True :
        new_pi = np.dot(K,s)
        K = new_pi
        n=n+1
        pi_roundeds = np.round(K, 2)
        if pi_roundeds[0][8] >= 0.5:

           return n 
           break
           
print(get_n(x))