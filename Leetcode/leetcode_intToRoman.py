num = int(input("Enter the integer "))
roman_map = [
        ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
        ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
        ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
            ]
    
result = []

for symbol, value in roman_map:
    while num >= value:
        result.append(symbol)
        num -= value

roman = ''.join(result)
print(roman)