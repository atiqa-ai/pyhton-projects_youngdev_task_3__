# Print Fibonacci sequence
def fabonacci():

 n = int(input("Enter how many terms you want: "))

 a, b = 0, 1  # first two numbers

 print("Fibonacci sequence:")
 for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


#function calling
fabonacci()