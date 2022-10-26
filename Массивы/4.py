nums = [int(i) for i in input().split()]
counted = []
for i in nums:
    if nums.count(int(i)) not in counted:
        counted.append(nums.count(int(i)))


print(max(counted))










