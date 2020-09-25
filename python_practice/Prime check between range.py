import numpy as np
def PrimeCalculate(P1,P2):
    a=[]
    k=0             #take it as a flag
    if(P1>P2):      #swap variables to reorder in ascending 
        var=P1      #     format
        P1=P2
        P2=var
    for i in range(P1,P2):
        for j in range(2,i):
            if(i%j==0):
                k=1         #change value of flag
                break
        if(k==0):    
            a.append(i)     #add values to list a if                        condition is satisfied
        k=0        #reset the value of k to 0.
    print(a)

PrimeCalculate(int(input('Please enter a number: ')), int(input('Please input enter another number: ')))
    