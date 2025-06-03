class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        q = None
        if target in nums:
            q  = nums.index(target)
        
        else:
            for i in range(n):
                if i == n-1 and nums[i]<target:
                    q=i+1
                    break

                elif nums[i]>target:
                    q=i
                    break

        return q

nums = list(map(int,input("Enter the list ").split()))
target = int(input("Enter the target "))
obj = Solution()
r = obj.searchInsert(nums,target)
print(f"Intex ",r)