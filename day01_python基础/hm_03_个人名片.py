'''
在控制台依次提示用户输入：姓名、公司、职位、电话、邮箱

'''
#  输入姓名
name = input('输入姓名')
#  输入公司名称
gs_name = input('输入公司名称')
#  输入职位
zw = input('输入职位')
#  输入电话号码
mobile = input('输入电话号码')
#  输入邮箱
email = input('输入邮箱')

print('**********************************************')
print('公司名称：%s' % (gs_name))
print('      ')
print('姓名:%s(%s)' % (name,zw))
print('      ')
print('电话:%s' % mobile)
print('邮箱:%s' % email)

