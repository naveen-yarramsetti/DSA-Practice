n = int(input())
sums = 0

while n > 0:
    last = (n % 10)
    sums += last  
    n = n // 10
print(sums)
