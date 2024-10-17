def number_1(n):
    for i in range(n):
        for j in range(i+1):
            print("1",end=" ")
        print()
number_1(5)
print()
def number_2(n,p=1):
    for i in range(n):
        for j in range(n-i):
            print(p,end=" ")
        p+=1
        print()
number_2(5)
print()            

def number_3(n,p=1):
    for i in range(n):
        for j in range(i+1):
            print(" ",end=" ")
        for k in range(n-i):
            print(p,end=" ")    
        p+=1
        print()    
number_3(5) 
print()
def number_4(n,p=1):
    for i in range(n):
        for j in range(n-i):
            print(" ",end=" ")
        for k in range(i):
            print(p,end=" ")   
        for l in range(i+1):
            print(p,end=" ")
        p+=1    
        print()  
number_4(5) 
print()
def number_5(n,p=1):
    for i in range(n):
        for j in range(i+1):
            print(" ",end=" ")
        for k in range(i,n-1):
            print(p,end=" ")
        for l in range(n-i):
            print(p,end=" ")
        p+=1
        print()
number_5(5) 
print()
def number_6(n,p=5):
    for i in range(n):
        for j in range(i+1):
            print(p,end=" ")
        p-=1    
        print()
number_6(5)
print()
def number_7(n,p=5):
     for i in range(n):
        for j in range(i+1):
            print(" ",end=" ")
        for k in range(i,n-1):
            print(p,end=" ")
        for l in range(n-i):
            print(p,end=" ")
        p-=1    
        print()
number_7(5)   
print()
def number_8(n,p=0):
    for i in range(n):
        for j in range(i+1):
            print(p,end=" ")
        p+=2 
        print()
number_8(5) 
print() 
def number_9(n,p=0):
    for i in range(n):
        for j in range(i+1):
            if (i%2==0):
                print("1",end=" ")
            else:
                print("2",end=" ")
        print()
number_9(5) 
print() 
def hill(n):
    for i in range(n):
        for j in range(n-i):
            print(" ",end=" ")
        for k in range(i):
            if (i%2==0):
                print("#",end=" ")
            else:
                print("$",end=" ")
        for l in range(i+1):
            if(i%2==0):
                print("#",end=" ")
            else:
                print('$',end=" ")
        print()
hill(5) 
print()
def diamond_numptrn(n,p=1):
    for i in range(n-1):
        for j in range(n-i):
            print(" ",end=" ")
        for k in range(i):
            print(p,end=" ")
        for l in range(i+1):
            print(p,end=" ")
        p+=1 
        print()
    for i in range(n):
        for j in range(i+1):
            print(" ",end=" ")
        for k in range(i,n-1):
            print(p,end=" ")
        for l in range(n-i):
            print(p,end=" ")
        p+=1   
        print() 
diamond_numptrn(5)   
def diamond_1(n,p=1):
    for i in range(n-1):
        for j in range(n-i):
            print(" ",end=" ")
        for k in range(i):
            print(p,end=" ")
        for l in range(i+1):
            print(p,end=" ")
        p+=1
        print()
    for i in range(n):
        for j in range(i+1):
            print(" ",end=" ")
        for k in range(i,n-1):
            print(p,end=" ")
        for l in range(n-i):
            print(p,end=" ")
        p-=1
        print()
        
diamond_1 (5)     



