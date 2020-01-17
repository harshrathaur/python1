a=int(input("Enter first number: ")) 
b=int(input("Enter second number: ")) 
n = 0
  
for i in range(1, min(a, b)+1): 
    if a%i==b%i==0: 
        print(i)
