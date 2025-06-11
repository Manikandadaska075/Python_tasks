# s = str(input("Enter the string:"))
s = "tmmzuxt"
dictionary = {}
left=0
length =0
j=1
for right in range(len(s)):
    char = s[right]
    if char in dictionary and dictionary[char]>=left:
        left = dictionary[char]+1
    else:
        length = max(length, right-left+1)
    dictionary[char] = right
print(length)