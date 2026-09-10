n = int(input())
odd = 0 
even  = 0

while n > 0:
    last_digit = n % 10 
    if last_digit % 2 == 0:
        even += 1 
    else:
        odd += 1 
    n = n // 10 
print("Even", even)    
print("Odd", odd)    
