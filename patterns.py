#Square pattern
def pattern_1(n):
    for i in range (n):
        for j in range(n):
            print("*",end=" ")
        print()    
pattern_1(5) 
print()
#Increasing triangle pattern
def pattern_2(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print()
pattern_2(5)    
print()
#Decreasing triangle pattern
def pattern_3(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end =" ")
        print()
n=int(input("enter a value:"))   
pattern_3(n)  
print() 
#Right sided triangle pattern    
def pattern_4(n):
    for i in range(n):
        for j in range(n-i):
            print(" ", end =" ")
        for k in range(i+1):
            print("*",end=" ") 
        print()
pattern_4(5)
print()         
#Right sided decreasing triangle pattern 
def pattern_5(n):
    for i in range(n):
        for j in range(i+1):
            print(" ",end =" ")
        for k in range(n-i):
            print("*",end=" ")
                
        print()  
pattern_5 (5)  
print()
#Hill pattern
def pattern_hill(n):
    for i in range(n):
        for j in range(n-i):
            print(" ",end=" ")
        for k in range(i) :
            print("*", end=" ")
        for l in range(i+1):
            print("*",end=" ")   
        print( )                  
pattern_hill(5)
print()
#Reverse hill pattern
def pattern_reverse_hill(n):
    for i in range(n):
        for j in range(i+1):
            print(" ",end=" ")
        for k in range(i,n-1):
            print("*",end=" ")
        for l in range(n-i):
            print("*",end=" ")
        print()
pattern_reverse_hill(5)                  