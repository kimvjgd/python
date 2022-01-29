nums = [1,2,3,4]
nums.append(5)
print(nums)

nums.insert(1,'123')
# nums[2:2] = ['123'] 과 같다.
print(nums)

list1 = [1,2,3,4,5]
list2 = [10,20,30]

list1.extend(list2)
print(list1)