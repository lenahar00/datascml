nums = [1, 2, 3, 4, 5, 6, 9.87654321]
numsum = 0
for i in nums:
    numsum = numsum + i
mean = numsum / len(nums)
print(f"List: ",nums)
print("The mean is:", mean)