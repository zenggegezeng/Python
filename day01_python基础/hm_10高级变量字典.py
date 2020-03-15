user1 = {'name': '曾志勇',
         'age': '18',
         'money': '2000000000'}
#  显示所有的key
print(user1.keys())

#  显示所有的value值
print(user1.values())

#  显示字典中所有的元祖列表
print(user1.items())

#  查询name的值 key存在
print(user1['name'])

#  查询name的值 key不存在报错
#  print(user1['name1'])

#  取出key的值，key不存在不会报错
print(user1.get('name1'))  # key不存在值显示为None
print(user1.get('name'))
print("--------------------------")

#  循环获取字典键值对
for k in user1:
    print('%s :' % k, end='\t')
    print('%s ' % user1[k])

print("----------------------------")

#  for循环遍历列表数据为字典的数据
user_list = [{'name': '张三',
              'qq': '123456',
              'phone': '110'},
             {'name': '李四',
              'qq': '654321',
              'phone': '10010'}
             ]
# 遍历列表user_list
for dis in user_list:
    for k in dis:
        print('%s :' % k, end="\t")
        print('%s ' % dis[k])











