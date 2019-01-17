#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 3-1 姓名： 将一些朋友的姓名存储在一个列表中， 并将其命名为names 。 依次访问该列表中的每个元素， 从而将每个朋友的姓名都打印出来。
# 3-2 问候语： 继续使用练习 3-1中的列表， 但不打印每个朋友的姓名， 而为每人打印一条消息。 每条消息都包含相同的问候语， 但抬头为相应朋友的姓名。
# 3-3 自己的列表： 想想你喜欢的通勤方式， 如骑摩托车或开汽车， 并创建一个包含多种通勤方式的列表。 根据该列表打印一系列有关这些通勤方式的宣言， 如“
# I would like to own a Honda motorcycle”。
#3-1
names = ('wangqiang','limei','wanggang')
print(names[0])
print(names[1])
print(names[2])
#3-2
names = ('wangqiang','limei','wanggang')
print("Hi  " + names[0].title() + ".")
print("Hi  " + names[1].title() + ".")
print("Hi  " + names[2].title() + ".")
#3-3
Mode_of_travel = ('bicycle','motorcycle','car')
for a in range(0,3):
    print("i want have" + Mode_of_travel[a] + '. ok?')

# 3-4 嘉宾名单 ： 如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的） ， 你会邀请哪些人？ 请创建一个列表， 其中包含至少3个你想邀请的人； 然后， 使用
# 这个列表打印消息， 邀请这些人来与你共进晚餐。
# 3-5 修改嘉宾名单 ： 你刚得知有位嘉宾无法赴约， 因此需要另外邀请一位嘉宾。
# 以完成练习 3-4时编写的程序为基础， 在程序末尾添加一条print 语句， 指出哪位嘉宾无法赴约。
# 修改嘉宾名单， 将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
# 再次打印一系列消息， 向名单中的每位嘉宾发出邀请。
# 3-6 添加嘉宾 ： 你刚找到了一个更大的餐桌， 可容纳更多的嘉宾。 请想想你还想邀请哪三位嘉宾。
# 以完成练习 3-4或练习 3-5时编写的程序为基础， 在程序末尾添加一条print 语句， 指出你找到了一个更大的餐桌。
# 使用insert( ) 将一位新嘉宾添加到名单开头。
# 使用insert( ) 将另一位新嘉宾添加到名单中间。
# 使用append( ) 将最后一位新嘉宾添加到名单末尾。
# 打印一系列消息， 向名单中的每位嘉宾发出邀请。
# 3-7 缩减名单 ： 你刚得知新购买的餐桌无法及时送达， 因此只能邀请两位嘉宾。
# 以完成练习 3-6时编写的程序为基础， 在程序末尾添加一行代码， 打印一条你只能邀请两位嘉宾共进晚餐的消息。
# 使用pop( ) 不断地删除名单中的嘉宾， 直到只有两位嘉宾为止。 每次从名单中弹出一位嘉宾时， 都打印一条消息， 让该嘉宾知悉你很抱歉， 无法邀请他来共进
# 晚餐。
# 对于余下的两位嘉宾中的每一位， 都打印一条消息， 指出他依然在受邀人之列。
# 使用del 将最后两位嘉宾从名单中删除， 让名单变成空的。 打印该名单， 核实程序结束时名单确实是空的

list = ['成龙','李连杰','郭富城']
for b in range(0,3):
    print('我想和' + list[b] + '一起吃晚饭。')
print(list[2] + '无法赴约')
list.insert(2,'洪金宝')
print('我想和' + list[2] + '一起吃晚饭。')
print('\n哈哈，皇天不负有心人，找到更大的餐桌。')
list.insert(0,'王宝强')
list.insert(2,'马蓉')
list.append('王菊')
for c in range(0,6):
    print('邀请' + list[c] + "一起吃饭")
print('\n送餐桌的快递车着火了,所以现在只能邀请两位来了\n')
print(list)
for d in range(0,len(list)-2):
    popped_list = list.pop()
    print('很抱歉不能与你共进晚餐了' + popped_list)
for e in range(0,len(list)):
    print('我依然可以邀请'+ list[e] + '吃法国鹅肝')
del list[1]#del 因从后往前删，不然就会报错
del list[0]
print(list)

# 3-8 放眼世界 ： 想出至少5个你渴望去旅游的地方。
# 将这些地方存储在一个列表中， 并确保其中的元素不是按字母顺序排列的。
# 按原始排列顺序打印该列表。 不要考虑输出是否整洁的问题， 只管打印原始Python列表。
# 使用sorted( ) 按字母顺序打印这个列表， 同时不要修改它。
# 再次打印该列表， 核实排列顺序未变。
# 使用sorted( ) 按与字母顺序相反的顺序打印这个列表， 同时不要修改它。
# 再次打印该列表， 核实排列顺序未变。
# 使用reverse( ) 修改列表元素的排列顺序。 打印该列表， 核实排列顺序确实变了。
# 使用reverse( ) 再次修改列表元素的排列顺序。 打印该列表， 核实已恢复到原来的排列顺序。
# 使用sort( ) 修改该列表， 使其元素按字母顺序排列。 打印该列表， 核实排列顺序确实变了。
# 使用sort( ) 修改该列表， 使其元素按与字母顺序相反的顺序排列。 打印该列表， 核实排列顺序确实变了。
# 3-9 晚餐嘉宾 ： 在完成练习 3-4~练习 3-7时编写的程序之一中， 使用len( ) 打印一条消息， 指出你邀请了多少位嘉宾来与你共进晚餐。
# 3-10 尝试使用各个函数 ： 想想可存储到列表中的东西， 如山岳、 河流、 国家、 城市、 语言或你喜欢的任何东西。 编写一个程序， 在其中创建一个包含这些元素的列
# 表， 然后， 对于本章介绍的每个函数， 都至少使用一次来处理这个列表。
place = ['taiguo','meiguo','xinjiapo']
print(place)
print(sorted(place))
print(place)
print(sorted(place,reverse=True))
print(place)
place.reverse()
print(place)
place.reverse()
print(place)
place.sort(reverse=True)
print(place)

list = ['成龙','李连杰','郭富城']
for b in range(0,3):
    print('我想和' + list[b] + '一起吃晚饭。')
print(list[2] + '无法赴约')
list.insert(2,'洪金宝')
print('我想和' + list[2] + '一起吃晚饭。')
print('\n哈哈，皇天不负有心人，找到更大的餐桌。')
list.insert(0,'王宝强')
list.insert(2,'马蓉')
list.append('王菊')
for c in range(0,6):
    print('邀请' + list[c] + "一起吃饭")
print('\n送餐桌的快递车着火了,所以现在只能邀请两位来了\n')
print(list)
for d in range(0,len(list)-2):
    popped_list = list.pop()
    print('很抱歉不能与你共进晚餐了' + popped_list)
for e in range(0,len(list)):
    print('我依然可以邀请'+ list[e] + '吃法国鹅肝')
    print('我将邀请' + str(len(list))+'个人吃大餐')
del list[1]#del 因从后往前删，不然就会报错
del list[0]
print(list)