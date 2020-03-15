import hm_07_分割线

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]

#  del list1[3]

# print(len(list1))


for name in list1:
    print(name)

hm_07_分割线.分割线(50)

list1.extend(list2)
list1.sort(reverse=True)
for name in list1:
    print(name)

hm_07_分割线.分割线(50)


list1.sort()
for name in list1:
    print(name)

hm_07_分割线.分割线(50)
list1.clear()
print(len(list1))
