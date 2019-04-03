#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 10-1 Python学习 笔记 ：在文本编辑器中新建一个文件，
# 写几句话来总结一下你至此学到的Python知识， 其中每一行都以“In Python you can”打头。 将这个文件命名为learning_python.txt并将其存储到为完成本章练习而编写的程序所在的目 录中。 编写一个程序，
# 它读取这个文件， 并将你所写的内容打印三次： 第一次打印时读取整个文件； 第二次打印时遍历文件对象； 第三次打印时将各行存储在一个列表中， 再在with 代码块外打印它们。

#learning_python.txt
# In Python you can learn variable
# In Python you can learn list
# In Python you can learn Operation list
# In Python you can learn dictionary
# In Python you can learn class

#第一次打印时读取整个文件
with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents)

#第二次打印时读取整个文件
filename = 'learning_python.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

#第三次打印时将各行存储在一个列表中
print('text3')
# filename = 'learning_python.txt'
with open('learning_python.txt') as file_object:
    lines = file_object.readline()
for line in lines:
    print(line.rstrip())
print(lines)

# 10-2 C语言学习 笔记 ： 可使用方法replace( )
# 将字符串中的特定单词都替换为另一个单词。 下面是一个简单的示例， 演示了如何将句子中的' dog' 替换为' cat'
# >>> message = "I really like dogs. "
# >>> message. replace(' dog' , ' cat' )
# ' I really like cats. '
# 　读取你刚创建的文件learning_python.txt中的每一行， 将其中的Python都替换为另一门语言的名称， 如C。
# 将修改后的各行都打印到屏幕上。

filename = 'learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    c = line.replace('Python','c++')
    print(c)

# 10-3 访客 ： 编写一个程序， 提示用户输入其名字； 用户作出响应后， 将其名字写入到文件guest.txt中。
message = input('Hello,please input your name,and i will write it into a file: ')
filename = 'guest.txt'
with open(filename,'a') as file_object:
    file_object.write(message+'\n')

# 10-4 访客名单 ： 编写一个while 循环， 提示用户输入其名字。 用户输入其名字后， 在屏幕上打印一句问候语，
# 并将一条访问记录添加到文件guest_book.txt中。 确保这个文件中的每条记录都独占一行。

filename = 'guest_book.txt'
while True:
    message = input('请输入名字')
    if message == 'q':
        break
    else:
        with open(filename,'a') as file_object:
            file_object.write(message+'\n')

#10-5 关于编程的调查 ： 编写一个while 循环， 询问用户为何喜欢编程。 每当用户输入一个原因后，
# 都将其添加到一个存储所有原因的文件中。跟10-4一样略
filename = 'learning_python.txt'
with open(filename,'a') as file_object:
    while  True:
        message = input("Why do you lile programmming: ")
        if message == 'q':
            break
        else:
            print('Reason '+ message)
            reason = ''
            reason += message
            print(reason)
        file_object.write('\nReason '+ reason)


# 10-6 加法运算：提示用户提供数值输入时，常出现的一个问题是，用户提供的是
# 文本而不是数字。在这种情况下，当你尝试将输入转换为整数时，将引发 TypeError 异
# 常。编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。在用户输入的
# 任何一个值不是数字时都捕获 TypeError 异常，并打印一条友好的错误消息。对你编写
# 的程序进行测试：先输入两个数字，再输入一些文本而不是数字。
while True:
        num1 = input('Please input the first number:(\'q\' for quit)')
        if num1 == 'q':
                break
        try:
                num1_int = int(num1)
        except  ValueError:
                print('Please input number!')
                continue
        num2 = input('Please input the second number:(\'q\' for quit)')
        try:
                num2_int = int(num2)
        except  ValueError:
                print('Please input number!')
                continue
        print(num1_int + num2_int)

# 10-7 加法计算器：将你为完成练习 10-6 而编写的代码放在一个 while 循环中，让
# 用户犯错（输入的是文本而不是数字）后能够继续输入数字。 10-6 按照10-7 来写的


# 10-8 猫和狗：创建两个文件 cats.txt 和 dogs.txt，在第一个文件中至少存储三只猫的
# 名字，在第二个文件中至少存储三条狗的名字。编写一个程序，尝试读取这些文件，并
# 将其内容打印到屏幕上。将这些代码放在一个 try-except 代码块中，以便在文件不存
# 在时捕获 FileNotFound 错误，并打印一条友好的消息。将其中一个文件移到另一个地
# 方，并确认 except 代码块中的代码将正确地执行。
while True:
    open_file_name = input('please input a file name to open it.( q for quit)')
    if open_file_name == 'q':
        break
    try:
            with open(open_file_name) as file_object:
                contents = file_object.read()
    except  FileNotFoundError:
        print('Sorry,I can not find your file.')
    else:
        print(contents)

# 10-9 沉默的猫和狗：修改你在练习 10-8 中编写的 except 代码块，让程序在文件不
# 存在时一言不发
while True:
    open_file_name = input('请输入你要找的文件： ')
    if open_file_name == 'q':
        break
    try:
        with open(open_file_name) as file_object:
                contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)


# 10-10 常见单词：访问项目 Gutenberg（http://gutenberg.org/），并找一些你想分析的
# 图书。下载这些作品的文本文件或将浏览器中的原始文本复制到文本文件中。
# 你可以使用方法 count()来确定特定的单词或短语在字符串中出现了多少次。例如，
# 下面的代码计算'row'在一个字符串中出现了多少次：
# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# >>> line.lower().count('row')
# 3
# 请注意，通过使用 lower()将字符串转换为小写，可捕捉要查找的单词出现的所有
# 次数，而不管其大小写格式如何。
# 编写一个程序，它读取你在项目 Gutenberg 中获取的文件，并计算单词'the'在每
# 个文件中分别出现了多少次。
#自己编写一个test1.txt文件
with open('test1.txt') as file_object:
    contents = file_object.read()
print('test1 use \'q\' for '+str(contents.lower().count('q'))+ ' times')


# 10-11 喜欢的数字：编写一个程序，提示用户输入他喜欢的数字，并使用
# json.dump()将这个数字存储到文件中。再编写一个程序，从文件中读取这个值，并打
# 印消息“I know your favourite number! It’s _____.”。
import json
favourate_num = input('Please input your favourate number: ')
with open('favourate_num.json','w') as file_object:
    json.dump('I know your favorite numeber! It\'s  '+ favourate_num,file_object)
with open('favourate_num.json') as file_object:
    contents = json.load(file_object)
print(contents)

# 10-12 记住喜欢的数字：将练习 10-11 中的两个程序合而为一。如果存储了用户喜
# 欢的数字，就向用户显示它，否则提示用户输入他喜欢的数字并将其存储到文件中。运
# 行这个程序两次，看看它是否像预期的那样工作。
import json
filename = 'favourate_num.json'
try:
    with open(filename) as file_object:
        contents = json.load(file_object)
except FileNotFoundError:
    favourate_num = input("Please input your favourite number: ")
    with open(filename,'w') as file_object:
        json.dump("I know your favorite number! It\’s "+favourate_num,file_object)
    with open(filename) as file_object:
        contents = json.load()
print(contents)

# 10-13 验证用户 ： 最后一个remember_me.py版本假设用户要么已输入其用户名， 要么是首次运行该程序。 我们应修改这个程序， 以应对这样的情形： 当前和最后一次
# 运行该程序的用户并非同一个人。
# 为此， 在greet_user( ) 中打印欢迎用户回来的消息前， 先询问他用户名是否是对的。 如果不对， 就调用get_new_username( ) 让用户输入正确的用户名。
import json

def get_stored_username():
	filename = 'username.json'
	with open(filename) as f_obj:
		username = f_obj.read()
	return username

def get_new_username():
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'a') as f_obj:
		json.dump(username, f_obj)
	return username

def greet_user():
	username = get_stored_username()
	username = str(username)
	if username:
		yep=input('Is ' + username + ' your name?(y/n)')
		print (yep)
		if  yep == 'y':
			print("Welcome back, " + username + "!")
		else:
			username = get_new_username()
			print("We'll remember you when you come back, " + username + "!")
	else:
		username = get_new_username()
		print("We'll remember you when you come back, " + username + "!")
greet_user()













