nums = list(map(int, input("Enter the list: ").split()))
val = int(input("Enter the value to remove: "))

n = len(nums)
i=0

if n != 0: 
    while i !=n:
        if nums[i] == val:
            nums.pop(i)
            n-=1
        else:   
            i+=1              
k = len(nums)
print(k)
