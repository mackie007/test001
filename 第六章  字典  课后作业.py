#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 6-1 人 ： 使用一个字典来存储一个熟人的信息， 包括名、 姓、 年龄和居住的城市。
#
# 　　　　该字典应包含键first_name 、 last_name 、 age 和city 。 将存储在该字典中的每项信息都打印出来。
#
# 6-2 喜欢的数字 ： 使用一个字典来存储一些人喜欢的数字。 请想出5个人的名字， 并将这些名字用作字典中的键；
#
# 　　　　　　　　想出每个人喜欢的一个数字， 并将这些数字作为值存
# 　　　　　　　　储在字典中。 打印每个人的名字和喜欢的数字。 为让这个程序更有趣， 通过询问朋友确保数据是真实的。
# 6-3 词汇表 ： Python字典可用于模拟现实生活中的字典， 但为避免混淆， 我们将后者称为词汇表。
# 　　　　　　想出你在前面学过的5个编程词汇， 将它们用作词汇表中的键， 并将它们的含义作为值存储在词汇表中。
# 　　　　　　以整洁的方式打印每个词汇及其含义。 为此， 你可以先打印词汇， 在它后面加上一个冒号， 再打印词汇的含义； 也可在一行打印词汇，
#
# 　　　　 　　再使用换行符（\n ） 插 入一个空行， 然后在下一行以缩进的方式打印词汇的含义。
friend = {'first_name ': 'wang', 'last_name ': 'qiang', 'age': 26, 'city': 'shanghai'}
print(friend['first_name '])
print(friend['last_name '])
print(friend['age'])
print(friend['city'])

name = {'ali':'1', 'taisen':'2', 'wo':'4', 'ta':'5', 'ni':'3'}
print(name['ali'])
print(name['taisen'])
print(name['wo'])
print(name['ta'])
print(name['ni'])
for ren,number in name.items():
    print(ren.title() + "'s favorite number is'" + str(number))

vocabulary = {'列表': '值可改', '元组':'值不可改'}
for name,meaning in vocabulary.items():
    print('\n',name + ':',meaning)

#  6-4 词汇表2 ： 既然你知道了如何遍历字典， 现在请整理你为完成练习 6-3而编写的代码， 将其中的一系列print 语句替换为一个遍历字典中的键和值的循环。 确定该
# # 　　　　　　循环正确无误后， 再在词汇表中添加5个Python术语。 当你再次运行这个程序时， 这些新术语及其含义将自动包含在输出中。
# # 6-5 河流 ： 创建一个字典， 在其中存储三条大河流及其流经的国家。 其中一个键—值对可能是' nile' : ' egypt' 。
# # 　　　　使用循环为每条河流打印一条消息， 如“The Nile runs through Egypt.”。
# # 　　　　使用循环将该字典中每条河流的名字都打印出来。
# # 　　　　使用循环将该字典包含的每个国家的名字都打印出来。
# # 6-6 调查 ： 在6.3.1节编写的程序favorite_languages.py中执行以下操作。
# # 　　　　创建一个应该会接受调查的人员名单， 其中有些人已包含在字典中， 而其他人未包含在字典中。
# # 　　　　遍历这个人员名单， 对于已参与调查的人， 打印一条消息表示感谢。 对于还未参与调查的人， 打印一条消息邀请他参与调查。

# 6-4 略
county_rivers ={'nile' : 'egypt','changjiang':'china','yamaxun':'baxi'}
for county,rivers in county_rivers.items():
    print('" The '+ county.title() + ' runs through ' + rivers + '."')
    for a in county_rivers.keys():
        print(a)
    for b in county_rivers.values():
        print(b)

favorite_languages = {
                    ' jen' : ' python' ,
                    ' sarah' : ' c' ,
                    ' edward' : ' ruby' ,
                    ' phil' : ' python' ,
                    }
people = {' jen' : ' Mark' ,' sarah' : ' tongtong' ,}
for name in favorite_languages.keys():
    if name in people:
        print(name + '感谢你参与调差')
    else:
        print(name + '请你参加调差')


# 6-7 人 ： 在为完成练习 6-1而编写的程序中， 再创建两个表示人的字典， 然后将这三个字典都存储在一个名为people 的列表中。 遍历这个列表， 将其中每个人的所有
# 信息都打印出来。
# 6-8 宠物 ： 创建多个字典， 对于每个字典， 都使用一个宠物的名称来给它命名； 在每个字典中， 包含宠物的类型及其主人的名字。 将这些字典存储在一个名为pets
# 的列表中， 再遍历该列表， 并将宠物的所有信息都打印出来。
# 6-9 喜欢的地方 ： 创建一个名为favorite_places 的字典。 在这个字典中， 将三个人的名字用作键； 对于其中的每个人， 都存储他喜欢的1~3个地方。 为让这个练
# 习更有趣些， 可让一些朋友指出他们喜欢的几个地方。 遍历这个字典， 并将其中每个人的名字及其喜欢的地方打印出来。
# 6-10 喜欢的数字 ： 修改为完成练习 6-2而编写的程序， 让每个人都可以有多个喜欢的数字， 然后将每个人的名字及其喜欢的数字打印出来。
# 6-11 城市 ： 创建一个名为cities 的字典， 其中将三个城市名用作键； 对于每座城市， 都创建一个字典， 并在其中包含该城市所属的国家、 人口约数以及一个有关该
# 城市的事实。 在表示每座城市的字典中， 应包含country 、 population 和fact 等键。 将每座城市的名字以及有关它们的信息都打印出来。
# 6-12 扩展 ： 本章的示例足够复杂， 可以以很多方式进行扩展了。 请对本章的一个示例进行扩展： 添加键和值、 调整程序要解决的问题或改进输出的格式。

people = {'caofu':{'first_name ':'cao','last_name':'fu','age':'25','city':'hefei'},
          'wangshi':{'first_name ':'wang','last_name':'shi','age':'64','city':'shenzhen'},
          'mayun':{'first_name ':'ma','last_name':'yun','age':'46','city':'haizhou'}}
for name,info in people.items():
    print('\n' + name )
    full_name = info['first_name '] + '' + info['last_name']
    city = info['city']
    age = info['age']
    print('\t Full_name ' + full_name.title())
    print('\t city ' + city.title())
    print('\t age ' + age)

lili = {'type':'dog','owner':'ergou'}
qq   = {'type':'cat','owner':'qiqi'}
pets = [lili,qq]
for a in pets:
    print(a)

favorite_places = {
    'wangqiang':['biejing','xi an'],
    'hedawei':['shanghai'],
    'yuhongqiang':['dali','lasa','chongqing'],}
for name,place in favorite_places.items():
    print('\n' + name +' favorite place')
    for city in place:
        print('\t' + city)

#6-10略
cities = {
    'Shanghai':{'country':'china','population':'*million','fact':'The political economic and cultural center'},
    'New York':{'country':'USA','population':'*million','fact':'International metropolis'},
    'Singapore':{'country':'singapore','population':'*million','fact':'city-state'}
}
for city,info in cities.items():
    print('\n' + city)
    for g,p in info.items():
        print('\t' + g)
        print('\t\t' + p)




