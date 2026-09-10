n = int(input())
reverse = 0

while n > 0:
    last = n % 10 
    reverse = reverse * 10 + last
    n = n // 10
print(reverse)
