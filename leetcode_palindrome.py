n = int(input("Enter a number to be checked "))
m=str(n)
if m[::] == m[::-1]:
    print(f"{m} is a palindrome")
else:
    print(f"{m} is not a palindrome")