nums1 = [1,2]
nums2 = [4,3]
nums = sorted(nums1 + nums2) 
length = len(nums)
mid = length // 2
print(float(nums[mid] if length % 2 else (nums[mid-1] + nums[mid]) / 2.0))