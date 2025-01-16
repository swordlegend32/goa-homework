nums = [1,2,3,4,5,6,7,8,9,10]

i = 0

while i < len(nums):
    num_to_delete = int(input("DELETE THY NUMBER "))
    nums.pop(num_to_delete)
    i += 1

print(nums)    