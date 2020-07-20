head = ["序号","描述"]
value1 = ["1","登录功能测试"]
value2 = ["2","注册功能测试"]
#zip
data_list = list()
print(dict(zip(head,value1)))
print(dict(zip(head,value2)))
data_list.append(dict(zip(head,value1)))
data_list.append(dict(zip(head,value2)))
print(data_list)