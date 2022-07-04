nums1 = [1, 2, 3, 5, 3, 6]
nums2 = [2, 3, 7, 3, 3, 8, 6, 5]

dict1 = {}
dict2 = {}

for i in range(len(nums1)):
    if nums1[i] in dict1:
        dict1[nums1[i]] += 1
    else:
        dict1[nums1[i]] = 1

for i in nums2:
    if i in dict2.keys():
        dict2[i] += 1
    else:
        dict2[i] = 1

print(dict1, dict2)
print(dict1.items())

for i in range(len(dict1)):
    a, *rest = dict1.items()
    print(type(a))