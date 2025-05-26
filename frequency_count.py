# Using for loop and comprehension

list1 = [1,2,2,3,1,4,1,2,4,3,1,5,2]
dit = {}
for i in list1:
    if i in dit:
        dit[i]+=1
    else:
        dit[i] = 1

print(dit)

max_value = max(dit.values())
max_keys = [k for k, v in dit.items() if v == max_value]

print("Max value:", max_value)
print("Keys with max value:", max_keys)


# Using Counter and comprehension
from collections import Counter 
list1 = [1,2,2,3,1,4,1,2,4,3,1,5,2]
d=Counter(list1)
print(d)

max_value = max(d.values())
max_keys = [k for k, v in d.items() if v == max_value]

print("Max value:", max_value)
print("Keys with max value:", max_keys)