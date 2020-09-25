def factorial(x):
    if(x==1 or x==0):
        return 1
    else:
        return x*factorial(x-1)
x,y = input('Please input two numbers x and y for x!/y! : ').split()
try:
    print(factorial(int(x))/factorial(int(y)))
except ValueError:
    print('Please enter valid arguments!')
    