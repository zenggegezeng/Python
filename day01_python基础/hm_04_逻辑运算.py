import random

if 10 > 5 and 11 > 12:
    print('666')
else:
    print('886')

print('---------------------------')

a = random.randint(10, 100)
print(a)

print('---------------------------')

a = 1
i = 1
while a <= 5:
    print('Hello Python')
    a += i

print('---------------------------')

b = 0
sum1 = 0
while b <= 100:
    if b % 2 == 0:
        sum1 += b
        b += 1
    else:
        b += 1
print('1-100至之间的偶数和是：%s' % sum1)

print('---------------------------')

count = 0
result = 0
while i <= 100:
    result += i
    i += 1
print('1-100至之间的和是：%s' % result)

print('---------------------------')

count1 = 0
result1 = 0
while count1 <= 100:
    if count1 == 10 or count1 == 20:
        count1 += 1
        continue
    else:
        result1 += count1
        count1 += 1
print('1-100之间(除去10和20)的和是：%s' % result1)

print('---------------------------')

count2 = 0
result2 = 0
while count2 <= 100:
    if count2 == 10 or count2 == 20:
        count2 += 1
        continue
    else:
        result2 += count2
        if result2 > 4500:
            break
        count2 += 1
print('1-100之间的和小于4500是：%s' % result2)

print('---------------------------')

count3 = 0
result3 = '*'
result4 = '*'
while count3 < 5:
    print(result3)
    result3 += result4
    count3 += 1

print('---------------------------')

#  九九乘法表
row = 1
while row <= 9:
    col = 1
    while col <= row:
        print('%s * %s = %s' %(col, row, row * col),end='\t')
        col += 1
    print(" ")
    row += 1


print('---------------------------')













