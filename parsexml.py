from xml.dom.minidom import parse

# 读取文件
# dom = parse('stu.xml')
# # 获取文档元素对象
# data = dom.documentElement
# # 获取 student
# stus = data.getElementsByTagName('student')
# for stu in stus:
#     # 获取标签属性值
#     # st_id = stu.getAttribute('id')
#     # st_name = stu.getAttribute('name')
#     # 获取标签中内容
#     id = stu.getElementsByTagName('id')[0].childNodes[0].nodeValue
#     name = stu.getElementsByTagName('name')[0].childNodes[0].nodeValue
#     age = stu.getElementsByTagName('age')[0].childNodes[0].nodeValue
#     gender = stu.getElementsByTagName('gender')[0].childNodes[0].nodeValue
#     # print('st_id:', st_id,  ', st_name:',st_name)
#     print('id:', id, ', name:', name, ', age:', age, ', gender:',gender)

dom1 = parse('save.xml')
data = dom1.documentElement
interfaces = data.getElementsByTagName('interface')
interfaceNameList =  []
for interface in interfaces:
    interfaceName = interface.getElementsByTagName('name')[0].childNodes[0].nodeValue
    interfaceNameList.append(interfaceName)
print(interfaceNameList)


