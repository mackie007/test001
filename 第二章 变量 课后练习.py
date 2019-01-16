#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 2-4 调整名字的大小写： 将一个人名存储到一个变量中， 再以小写、 大写和首字母大写的方式显示这个人名。
# 2-5 名言： 找一句你钦佩的名人说的名言， 将这个名人的姓名和他的名言打印出来。输出应类似于下面这样（包括引 号） ：
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”
# 2-6 名言2： 重复练习 2-5， 但将名人的姓名存储在变量famous_person 中， 再创建要显示的消息， 并将其存储在变量message 中， 然后打印这条消息。
# 2-7 剔除人名中的空白： 存储一个人名， 并在其开头和末尾都包含一些空白字符。 务必至少使用字符组合" \t" 和" \n" 各一次。
# 打印这个人名， 以显示其开头和末尾的空白。 然后， 分别使用剔除函数lstrip( ) 、 rstrip( ) 和strip( ) 对人名进行处理， 并将结果打印出来。
#2-9 最喜欢的数字： 将你最喜欢的数字存储在一个变量中， 再使用这个变量创建一条消息， 指出你最喜欢的数字， 然后将这条消息打印出来。
#2-4 2-5
name_message = 'Albert Einstein once said, “A person who never made a mistake never tried anything new.”'
print(name_message.upper())
print(name_message.lower())
print(name_message.title())

#2-6
famous_person = 'Albert Einstein'
message = famous_person + 'once said, “A person who never made a mistake never tried anything new.”'
print(message)

#2-7
name = " Alb\tert Ei\nnstein "
print(name)
print(name.rstrip())
print(name.lstrip())
print(name.strip())#好像就是空格越来越少了

#2-9
favorite_number = 4
print("My favorite number is " + str(favorite_number))
