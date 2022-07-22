#https://leetcode.com/problems/contains-duplicate/  
def containsDuplicate(nums):
  num1=set(nums)
  if len(nums)==len(num1):
    return False
  return True
        
#Sample 
print(containsDuplicate([1,2,3,1]))
