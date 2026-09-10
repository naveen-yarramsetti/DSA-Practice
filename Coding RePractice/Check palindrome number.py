num = int(input())

org = num 
palindrome = 0

while num > 0:
    last = num % 10 
    palindrome = palindrome * 10 + last
    num = num // 10 
if(palindrome == org):
    print("Palindrome")
else:
    print("Not Palindrome")
    
n = input()
palindrome = n[::-1]
if(palindrome == n):
    print("Palindrome")
