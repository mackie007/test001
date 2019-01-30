#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 8-1 消息 ： 编写一个名为display_message() 的函数， 它打印一个句子， 指出你在本章学的是什么。 调用这个函数， 确认显示的消息正确无误。
# 8-2 喜欢的图书 ： 编写一个名为favorite_book() 的函数， 其中包含一个名为title 的形参。 这个函数打印一条消息， 如One of my favorite books is
# Alice in Wonderland 。 调用这个函数， 并将一本图书的名称作为实参传递给它。
def display_message():
    print('定义函数')
display_message()

def favorite_book(title):
    print('one of my favorite book is {0}'.format(title.title()))
favorite_book('Alice in Wonderland')

# 8-3 T恤 ： 编写一个名为make_shirt() 的函数， 它接受一个尺码以及要印到T恤上的字样。 这个函数应打印一个句子， 概要地说明T恤的尺码和字样。
# 使用位置实参调用这个函数来制作一件T恤； 再使用关键字实参来调用这个函数。
# 8-4 大号T恤 ： 修改函数make_shirt() ， 使其在默认情况下制作一件印有字样“I love Python”的大号T恤。 调用这个函数来制作如下T恤： 一件印有默认字样的大号T
# 恤、 一件印有默认字样的中号T恤和一件印有其他字样的T恤（ 尺码无关紧要） 。
# 8-5 城市 ： 编写一个名为describe_city() 的函数， 它接受一座城市的名字以及该城市所属的国家。 这个函数应打印一个简单的句子， 如Reykjavik is in
# Iceland 。 给用于存储国家的形参指定默认值。 为三座不同的城市调用这个函数， 且其中至少有一座城市不属于默认国家。

def make_shirt(size,word):
    print('\n你想要的尺寸{0}和字样{1}'.format(size,word))
make_shirt('xxxl','wo shi cai ji ')
make_shirt(size='xxl',word='人生苦短 ')

def make_shirt(size,word='i love Python'):
    print('\n你想要的尺寸{0}和字样{1}'.format(size, word))
make_shirt('xxl')
make_shirt('xxxl','i love php')

def describe_city(city_name,city_country='Ice land'):
    print('\n{0} is in {1}'.format(city_name.title(),city_country.title()))
describe_city('Reykjavik')
describe_city('Aierlan')
describe_city('beijing','china')

# 8-6 城市名 ： 编写一个名为city_country() 的函数， 它接受城市的名称及其所属的国家。 这个函数应返回一个格式类似于下面这样的字符串：
# "Santiago, Chile"
# 8-7 专辑 ： 编写一个名为make_album() 的函数， 它创建一个描述音乐专辑的字典。 这个函数应接受歌手的名字和专辑名， 并返回一个包含这两项信息的字典。 使
# 用这个函数创建三个表示不同专辑的字典， 并打印每个返回的值， 以核实字典正确地存储了专辑的信息。
# 给函数make_album() 添加一个可选形参， 以便能够存储专辑包含的歌曲数。 如果调用这个函数时指定了歌曲数， 就将这个值添加到表示专辑的字典中。 调用这个
# 函数， 并至少在一次调用中指定专辑包含的歌曲数。
# 8-8 用户的专辑 ： 在为完成练习8-7编写的程序中， 编写一个while 循环， 让用户输入一个专辑的歌手和名称。 获取这些信息后， 使用它们来调用函
# 数make_album() ， 并将创建的字典打印出来。 在这个while 循环中， 务必要提供退出途径。

#8-6 略

def make_album(singer, album,songNumber = 0):
    if  (songNumber == 0):
        singer_album = {singer:album}
        return singer_album
    else:
        singer_album = {singer: album, 'songNumber': songNumber}
        return singer_album
print(make_album('cc','rain in spain'))
print(make_album('mm','falling in spain'))
print(make_album('lily','roman',23))


def make_album(singer, album):
    singer_album = {singer: album}
    return singer_album

while True:
    a = input('please input name of singer:(q for qute)')
    if a == 'q':
        break
    else:
        b = input('please input name of album: ')
        print(make_album(a,b))

# 8-9 魔术师 ： 创建一个包含魔术师名字的列表， 并将其传递给一个名为show_magicians( ) 的函数， 这个函数打印列表中每个魔术师的名字。
# 8-10 了不起的魔术师 ： 在你为完成练习 8-9而编写的程序中， 编写一个名为make_great( ) 的函数， 对魔术师列表进行修改， 在每个魔术师的名字中都加入字样“the
# Great”。 调用函数show_magicians( ) ， 确认魔术师列表确实变了。
# 8-11 不变的魔术师 ： 修改你为完成练习 8-10而编写的程序， 在调用函数make_great( ) 时， 向它传递魔术师列表的副本。 由于不想修改原始列表， 请返回修改后的
# 列表， 并将其存储到另一个列表中。 分别使用这两个列表来调用show_magicians( ) ， 确认一个列表包含的是原来的魔术师名字， 而另一个列表包含的是添加了字
# 样“the Great”的魔术师名字。

def show_magicians(name):
    for name in name:
        print(name)
name = ['abc,csd,sda']
show_magicians(name)

# 8-10 方法一
def show_magicians(name):
    for name in name:
        print(name)

def make_great(name1):
    for name2 in range(0,len(name1)):
        name1[name2] = 'The Great ' + name1[name2].title()
name1 = ['xuzhiqian','wangqiang','wangkang']
make_great(name1)
show_magicians(name1)

#8-10 方法二
name3 = ['wangbaoqiang','yaozhihang','chuanwanhongren']
name4 = []
def make_great(name3,name4):
    while name3:
        name5 = name3.pop()
        name6 = 'The Great '+ ''+name5
        name4.append(name6)
def show_magicianslis(name4):
    for name7 in name4:
        print(name7)
make_great(name3,name4)
show_magicianslis(name4)

# 8-11
name3 = ['test1','test2','test3']
name4 = []
def show_magicias(name4):
    for name2 in name4:
        print(name2)

def make_great(name3):
    for name in name3:
        name5 = 'The Great '+ name.title()
        name4.append(name5)
    return name4
a = make_great(name3[:])
show_magicianslis(a)
show_magicianslis(name3)

# 8-12 三明治 ： 编写一个函数， 它接受顾客要在三明治中添加的一系列食材。 这个函数只有一个形参（它收集函数调用中提供的所有食材） ， 并打印一条消息， 对顾客
# 点的三明治进行概述。 调用这个函数三次， 每次都提供不同数量的实参。
# 8-13 用户简介 ： 复制前面的程序user_profile.py， 在其中调用build_profile( ) 来创建有关你的简介； 调用这个函数时， 指定你的名和姓， 以及三个描述你的键-值
# 对。
# 8-14 汽车 ： 编写一个函数， 将一辆汽车的信息存储在一个字典中。 这个函数总是接受制造商和型号， 还接受任意数量的关键字实参。 这样调用这个函数： 提供必不可
# 少的信息， 以及两个名称—值对， 如颜色和选装配件。 这个函数必须能够像下面这样进行调用：

def sandwichs(*args):
    print(*args)
sandwichs('牛肉')
sandwichs("牛肉",'羊肉','猪肉')

def build_profile(first,last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for k,v in user_info.items():
        profile[k]=v
    return profile
user_profile = build_profile('cao' , 'fu' ,
location='hefei',field='finance',
character='better',ability='good',
appearance='shuai',iq='gao')
print(user_profile)


# 8-14 略
def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_prints = unprinted_designs.pop()
        completed_models.append(current_prints)

def show_complete_models(completed_models):
    print("\n   The following modle have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

#重新创建一个printing_functions.py文件进行调用
# def print_models(unprinted_designs, completed_models):
#     """
#     模拟打印每个设计，直到没有未打印的设计为止
#     打印每个设计后，都将其移到列表completed_models中
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#
#         # 模拟根据设计制作3D打印模型的过程
#         print("Printing model: " + current_design)
#         completed_models.append(current_design)
#
#
# def show_completed_models(completed_models):
#     """显示打印好的所有模型"""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
from printing_functions import *
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_complete_models(completed_models)

#函数的调用几种方式
import printing_functions
printing_functions.message()

from printing_functions import message
message()

from printing_functions import message as bc
bc()

import printing_functions as bc
bc.message()

from printing_functions import *
message()















