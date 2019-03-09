"""this is a calculator programme made by 
    Munjir Ibn Habib
          with python 3"""
                 #let's start...

from math import sqrt, factorial, log10

 # here I defined some one line  functions                 

add = lambda X, Y: ('%.4f' % (X+Y))
sub = lambda X, Y:('%.4f' % (X-Y))
mul = lambda X, Y: ('%.4f' % (X*Y))
div = lambda X,Y: ('%.4f' % (X/Y))
log = lambda X: ('%.4f' %(log10(X)))

"""I also used sqrt(),pow(),factorial() function 
    which are  imported from math """
    
print('    ======< CALCULATOR >=====')    
print('\nHey,what would you like to perform?')             

#you can perform this actions
print('0.Turn Off',
            '\n1.Sumation',
            '\n2.Subtraction',  
            '\n3.Multiplication',
            '\n4.Division',
            '\n5.Power',
            '\n6.Squar Root',
            '\n7.Factorial',
            '\n8.Log (Base 10)')

while True:
    A = input("\nEnter just the number of your choosen action: ")
    try:
        A = int(A)
    except ValueError:
        print('\nThis is NOT a number!')
        continue 
    if A == 0:
         print('\nTurned Off.\nTHANKS FROM Munjir')
         break
   
    while A>0 and A<9:     
        #this is to assing X and Y with conditions 
        X = input('Ok,enter your first  number: ')
        try:
            X = float(X)
        except ValueError:
            print('\nThis is NOT a number!')
            continue 
        if  A == 6 or A == 7 or A == 8:
            break 
        Y = input('Now,enter your second number: ')
        try:
            Y = float(Y)
        except ValueError:
            print('\nThis is NOT a number!')
            continue 
        break 

            #here starts the main part...
 
    if A == 1:
        print('\nSumation is: ',add(X,Y))
    elif A == 2:
        print('\nSubtraction is: ',sub(X,Y))
    elif A == 3:
        print('\nMultiplication is: ',mul(X,Y))
    elif A == 4:
        try:
            print('\nDivision is: ',div(X,Y))
        except ZeroDivisionError:
            print('\nMath ERROR!')
    elif A == 5:
        print('\nSecond number to the power first is: ',pow(X,Y))
    elif A == 6:
        print('\nSquare root of the first number is: ', sqrt(X))
    elif A == 7:
        try:
            print('\nFactorial of the first number is: ', factorial(X))
        except ValueError:
            print('\nMath ERROR!')
    elif A == 8:
        try:
            print('\nLogarithm of the first number is: ', log(X))
        except ValueError:
            print('\nMath ERROR!')
    else:
        print('\nOut of the given options!')
        continue 
        
#THANKS FROM Munjir!
 
