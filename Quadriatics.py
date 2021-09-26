#Basic math program for quadriatics
#KYGM - 9/22/21
import math
from fractions import Fraction

cont = 1

while cont == 1:
    
    print("Welcome to the quadriatics app. \n This app helps solve quadriatics with \n a max degree of 2")
    
    a = input("Enter a: ")
    b = input("Enter b: ")
    c = input("Enter c: ")
    
    #casting necessary... thanks python
    a = int(a)
    b = int(b)
    c = int(c)
    
    #Determinant = b^2-4ac
    d = ((b**2)-(4*(a*c)))
    
    print("Determinant: " + str(d))
    
    #where h = -b/2a
    bta = -b/(2*a)
    print("H: " + str(bta))
    
    #where k = f(h)
    fbta = a*((bta)**2)+b*bta+c
    print("K: " + str(fbta))
    
    #where vertex = (H,K)
    print("Vertex: (",bta,",",fbta,")")
    
    #where yint = f(0)
    yint = a*((0)**2)+b*0+c
    
    print("Y int: " + str(yint))
    
    if d < 0:
        print("Nonreal Solution")
    else:
        print("Quadritic!")
        q = Fraction(-b + math.sqrt(d))/(2*a)
        r = Fraction(-b - math.sqrt(d))/(2*a)

        if q == r: 
            print("Root: ", q)
        else:
            print("Roots: ", q,",", r)
        
    cont = input("Another? 0 for no 1 for yes: ")
    cont = int(cont)