jo = list(map(str,input().split()))
jo_integer = int(''.join(jo))  
jo_integer += 1
sp_integer = str(jo_integer)
new_list = [int(i) for i in sp_integer]
print(new_list)