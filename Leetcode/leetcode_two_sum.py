nums=[3,2,4]
target = 6
num_map = {} 
a = []
for i, num in enumerate(nums):
    diff = target - num
    if diff in num_map:
        a= [num_map[diff], i]
        print(a)
    num_map[num] = i
if a == []:
    print(a)
