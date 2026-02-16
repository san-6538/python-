

standard_input = '10'
n = int(input("enter a number:"))

if n <= 1:
    print("not prime")
else:
    is_prime = True
    for i in range(2,int(n**0.5)+1):
        if n % i ==0:
            is_prime = False
            break
        
if is_prime:
    print("prime")
else:
    print("not prime")
    