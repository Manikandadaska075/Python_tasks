
dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
s = str(input("Input ")).upper()
Number = 0
i = 0
n = len(s)
while i < n:
    if i + 1 < n and dic[s[i]] < dic[s[i + 1]]:
        Number += dic[s[i + 1]] - dic[s[i]]
        i += 2 
    else:
        Number += dic[s[i]]
        i += 1
print(Number)

        