class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        q=0
        i=0
        while i<len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
            else:
                i+=1
        w = len(nums)
        return w
    
obj = Solution()
nums = list(map(int,input("Enter the list ").split()))
r = obj.removeDuplicates(nums)
print(r)