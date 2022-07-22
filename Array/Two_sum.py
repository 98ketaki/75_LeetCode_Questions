#https://leetcode.com/problems/two-sum/

def twoSum(self, nums, target):
  dict={}
  for i in range(len(nums)):
     dict[nums[i]]=i
     for i in range(len(nums)):
         diff=target-nums[i]
         if diff in dict and dict[diff]!=i:
             return i, dict[diff]
             
nums=[2,7,11,15]
target=9
print(twoSum(nums, target))
