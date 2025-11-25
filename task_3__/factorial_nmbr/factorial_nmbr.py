def factorial(num):
    fact=1
    if num==1 or num==0:
        fact=1
    else:
        for i in range(1,num+1):
            
         fact=fact*i 
         
    return fact
    
    
number=int(input("enter a nmbr:"))    
output=factorial(number)       
print(f"factorial of {number} is : {output}")