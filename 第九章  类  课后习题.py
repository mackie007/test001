#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 9-1 餐馆 ： 创建一个名为Restaurant 的类， 其方法__init__( ) 设置两个属性： restaurant_name 和cuisine_type 。 创建一个名
# 为describe_restaurant( ) 的方法和一个名为open_restaurant( ) 的方法， 其中前者打印前述两项信息， 而后者打印一条消息， 指出餐馆正在营业。
# 根据这个类创建一个名为restaurant 的实例， 分别打印其两个属性， 再调用前述两个方法。
# 9-2 三家餐馆 ： 根据你为完成练习 9-1而编写的类创建三个实例， 并对每个实例调用方法describe_restaurant( ) 。
# 9-3 用户 ： 创建一个名为User 的类， 其中包含属性first_name 和last_name ， 还有用户简介通常会存储的其他几个属性。 在类User 中定义一个名
# 为describe_user( ) 的方法， 它打印用户信息摘要； 再定义一个名为greet_user( ) 的方法， 它向用户发出个性化的问候。
# 创建多个表示不同用户的实例， 并对每个实例都调用上述两个方法。
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name.title())
        print(self.cuisine_type.title())
    def open_restaurant(self):
        print('正在营业')
restaurant = Restaurant('王宝和大酒店','China')
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2略
class User():
    def __init__(self,first_name,last_name,location = 'local'):
        self.first_name = first_name
        self.last_name = last_name
        self.locations = location
    def greet_user(self):
        print('你好！ : '+ self.first_name + self.last_name)
    def describe_user(self):
        print('用户简介：'+ self.first_name + self.last_name)
a = User('wang','qiang')
b = User('liu','wei')
a.describe_user()
a.greet_user()
b.describe_user()
b.greet_user()

# 9-4 就餐人数 ： 在为完成练习 9-1而编写的程序中， 添加一个名为number_served 的属性， 并将其默认值设置为0。 根据这个类创建一个名为restaurant 的实
# 例； 打印有多少人在这家餐馆就餐过， 然后修改这个值并再次打印它。
# 添加一个名为set_number_served( ) 的方法， 它让你能够设置就餐人数。 调用这个方法并向它传递一个值， 然后再次打印这个值。
# 添加一个名为increment_number_served( ) 的方法， 它让你能够将就餐人数递增。 调用这个方法并向它传递一个这样的值： 你认为这家餐馆每天可能接待的就
# 餐人数。
# 9-5 尝试登录次数 ： 在为完成练习 9-3而编写的User 类中， 添加一个名为login_attempts 的属性。 编写一个名为increment_login_attempts( ) 的方法，
# 它将属性login_attempts 的值加1。 再编写一个名为reset_login_attempts( ) 的方法， 它将属性login_attempts 的值重置为0。
# 根据User 类创建一个实例， 再调用方法increment_login_attempts( ) 多次。 打印属性login_attempts 的值， 确认它被正确地递增； 然后， 调用方
# 法reset_login_attempts( ) ， 并再次打印属性login_attempts 的值， 确认它被重置为0。
class Restaurant():
    '''
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    '''
    def __init__(self,restaurant_name,cuisine_type,number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    def describe_restaurant(self):
        print(self.restaurant_name.title())
        print(self.cuisine_type.title())
    def open_restaurant(self):
        print('正在营业')
    def set_number_served(self,num):
        self.number_served = num
        print('多少人在吃饭'+ str(self.number_served))
    def increment_number_served(self,num):
        while self.number_served<num:
                self.number_served += num
        print(str(self.number_served))
restaurant = Restaurant('王宝和大酒店','上海老字号')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(10)
restaurant.increment_number_served(13)

class User():
    def __init__(self,first_name,last_name,idNumber,login_attempts = 0,location = 'loca'):
        self.first_name = first_name
        self.last_name = last_name
        self.id = idNumber
        self.login_attempts = login_attempts
        self.location = location

    def describe_user(self):
        print("First name is " + self.first_name.title())
        print("Last name is " + self.last_name.title())
        print('login_attempts is ' + str(self.login_attempts))

    def greet_user(self):
        print('hello, how are you, ' + self.first_name + '.' + self.last_name + '?')
        print('your id is ' + self.id + ' , please remenber it.')
        print(self.location + ' is a nice place!')
        print('login_attempts is ' + str(self.login_attempts))
    def increment_login_attempts(self):
        self.login_attempts += 1
    def rest_login_attempts(self):
        self.login_attempts = 0
a = User('wangqiang','ligang','12')
for b in range(0,3):
    a.describe_user()
    a.greet_user()
    a.increment_login_attempts()
a.rest_login_attempts()
a.describe_user()

 # 9-6 冰淇淋小店 ： 冰淇淋小店是一种特殊的餐馆。 编写一个名为IceCreamStand 的类， 让它继承你为完成练习 9-1或练习 9-4而编写的Restaurant 类。 这两个版
# 本的Restaurant 类都可以， 挑选你更喜欢的那个即可。 添加一个名为flavors 的属性， 用于存储一个由各种口味的冰淇淋组成的列表。 编写一个显示这些冰淇淋
# 的方法。 创建一个IceCreamStand 实例， 并调用这个方法。
# 9-7 管理员 ： 管理员是一种特殊的用户。 编写一个名为Admin 的类， 让它继承你为完成练习 9-3或练习 9-5而编写的User 类。 添加一个名为privileges 的属性， 用
# 于存储一个由字符串（如" can add post" 、 " can delete post" 、 " can ban user" 等） 组成的列表。 编写一个名为show_privileges( ) 的方法， 它
# 显示管理员的权限。 创建一个Admin 实例， 并调用这个方法。
# 9-8 权限 ： 编写一个名为Privileges 的类， 它只有一个属性——privileges ， 其中存储了练习9-7 所说的字符串列表。 将方法show_privileges( ) 移到这
# 个类中。 在Admin 类中， 将一个Privileges 实例用作其属性。 创建一个Admin 实例， 并使用方法show_privileges( ) 来显示其权限。
# 9-9 电瓶升级 ： 在本节最后一个electric_car.py版本中， 给Battery 类添加一个名为upgrade_battery( ) 的方法。 这个方法检查电瓶容量， 如果它不是85， 就将它
# 设置为85。 创建一辆电瓶容量为默认值的电动汽车， 调用方法get_range( ) ， 然后对电瓶进行升级， 并再次调用get_range( ) 。 你会看到这辆汽车的续航里程增
# 加了。

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type,number_served = 0):#这里参数几个下面调用的时候就几个
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    def describe_retaurant(self):
        print('restaurant_name is '+self.restaurant_name+'\n'+'cuisine_type is '+self.cuisine_type)
    def open_restaurant(self):
        print('Restaurant does business')
    def set_number_served(self,num):
        self.number_served = num
    def increnment_number_served(self,num):
        while self.number_served<num:
            self.number_served += 1
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavors = [],number_served = 0):
        super().__init__(restaurant_name,cuisine_type,number_served)
        self.flavors = flavors
    def show_flavors(self):
        print('flavors is '+ str(self.flavors))
ice = IceCreamStand('Icelove','IceCream',['apple','banana'],34)
ice.show_flavors()


class User():
    def __init__(self,first_name,last_name,idNumber,login_attempts = 0,location = 'local'):
        self.first_name = first_name
        self.last_name = last_name
        self.id = idNumber
        self.login_attempts = login_attempts
        self.location = location
    def describe_user(self):
        print('first_name : '+ self.first_name+',last_name :'+self.last_name )
        print('login_attempts is '+str(self.login_attempts))

    def greet_user(self):
        print('hello, how are you, ' + self.first_name + '.' + self.last_name + '?')
        print('your id is ' + self.id + ' , please remenber it.')
        print(self.location + ' is a nice place!')
        print('login_attempts is ' + str(self.login_attempts))
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self,first_name,last_name,idNumber,login_attempts = 0,location = 'local'):
        super().__init__(first_name,last_name,idNumber,login_attempts = 0,location = 'local')
        self.privileges =["can add post", "can delete post", "can ban user"]
    def show_privileges(self):
        print('\nThe Admin\'s privileges is '+str(self.privileges))

a = Admin('AA', 'CC', 8, 3, 'China')
a.show_privileges()


#9-8
class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post","can ban user"]
    def show_prinileges(self):
        print(self.privileges)
class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempt = 0
    def describe_user(self):
        print('My first name is '+ self.first_name.title() + '\n'+ 'last_name is '+ self.last_name.title())
    def greet_user(self):
        full_name = self.first_name + '.'+ self.last_name
        print('Hello'+ full_name.title())
    def increment_attempt(self):
        self.login_attempt += 1
    def reset_login_attempts(self):
        self.login_attempt = 0
class Admin(User):
        def __init__(self,first_name,last_name):
            super().__init__(first_name,last_name)
            self.privileges = Privileges()
user = Admin('wang','qiang')
user.privileges.show_prinileges()

#9-9
class Car:
    def __init__(self,make,model,years):
        self.make = make
        self.model = model
        self.years = years
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.years) + ' '+ self.make + ' '+ self.model
        return long_name
    def read_odometer(self):
        print('The car has ' + str(self.odometer_reading) + ' miles on it .')
    def update_odometer(self,milegeage):
        if milegeage >= self.odometer_reading:
            self.odometer_reading =milegeage
        else:
            print('You can\'t roll back an odometer')
    def increment_odometer(self,miles):
        self.odometer_reading += miles
class Battery():
    def __init__(self):
        self.battery_size = 70
    def describe_battery(self):
        print('This is car has a '+ str(self.battery_size) + '-kWh battery')
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        if self.battery_size == 85:
            range = 270
        message = 'This car can go approximately '+ str(range)
        message += ' miles on full charge'
        print(message)
        self.upgrade_battery()
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = Battery()
    def describe_battery(self):
        self.battery_size.describe_battery()
    def get_range(self):
        self.battery_size.get_range()

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.get_range()
my_tesla.get_range()

 # 9-10 导入Restaurant 类 ： 将最新的Restaurant 类存储在一个模块中。 在另一个文件中， 导入Restaurant 类， 创建一个Restaurant 实例， 并调
# 用Restaurant 的一个方法， 以确认import 语句正确无误。
# 9-11 导入Admin 类 ： 以为完成练习 9-8而做的工作为基础， 将User 、 Privileges 和Admin 类存储在一个模块中， 再创建一个文件， 在其中创建一个Admin 实例
# 并对其调用方法show_privileges( ) ， 以确认一切都能正确地运行。
# 9-12 多个模块 ： 将User 类存储在一个模块中， 并将Privileges 和Admin 类存储在另一个模块中。 再创建一个文件， 在其中创建一个Admin 实例， 并对其调用方
# 法show_privileges( ) ， 以确认一切都依然能够正确地运行。

from daoru import   Restaurant
a = Restaurant('wang','qiang')
a.describe_restaurant()
a.open_restaurant()


from daoru import Admin
b = Admin('wang','wei')
b.privileges.show_privileges()
user = Admin('ergou','yang')
user.privileges.show_privileges()

#9-12 其实就是两次的导入，创建两个文件，跟上面类似，所有调用的文件都是重复之前的函数

# 9-13 使用 OrderedDict： 在练习 6-4 中，你使用了一个标准字典来表示词汇表。请
# 使用 OrderedDict 类来重写这个程序，并确认输出的顺序与你在字典中添加键—值对的
# 顺序一致。

class OrderedDict():
    def __init__(self,vocabulary):
        self.vocabulary = vocabulary
    def show_vocabulary(self):
        for keys,value in self.vocabulary.items():
            print(keys +' :  '+ value)
vocabulary = {'int':'integer number','char':'the base element of string','class':'a base of OPP',
              'struct':'you can use this to develop your own data struct',
              'printf':'a function to print something on the screen'}
e = OrderedDict(vocabulary)
e.show_vocabulary()


# 9-14 骰子：模块 random 包含以各种方式生成随机数的函数，其中的 randint()返回
# 一个位于指定范围内的整数，例如，下面的代码返回一个 1~6 内的整数：
# from random import randint
# x = randint(1, 6)
# 请创建一个 Die 类，它包含一个名为 sides 的属性，该属性的默认值为 6。编写一
# 个名为 roll_die()的方法，它打印位于 1 和骰子面数之间的随机数。创建一个 6 面的骰
# 子，再掷 10 次。
# 创建一个 10 面的骰子和一个 20 面的骰子，并将它们都掷 10 次
from random import randint
class Die():
    def __init__(self):
        self.sides = 6
    def roll_die(self):
        print(str(randint(1,self.sides)))

g = Die()
print('10 tests')
for i in range(1,11):
    g.roll_die()
print('20 tests')
for i in range(1,21):
    print('------------')
    g.roll_die()











