"""class Bird(object):         #定义一个类
    feather = True          #类的属性
    reprofuction = "egg"
    def set_color(self,color):       #在方法中通过self参数设定对象的属性
        self.color = color
    def chirp(self,sound):  #内部定义的函数 叫做方法
        print(sound)

    def __init__(self,fac):
        self.fac = fac
        print("it's fac is:",fac)
    def Facter(self):
        print(self.fac)

summer = Bird("good")   #创建对象，summer是属于鸟类的一个对象
summer.Facter()
#print(summer.reprofuction)
#summer.chirp(123456)
#summer.set_color('red')
#print(summer.color)
"""

class Bird(object):     #object充当所有类的祖先
    def chirp(self):
        print("make sound")

class Chicken(Bird):       #定义一个Bird的子类
    def chirp(self):       #子类可以定义一个和父类同名的属性方法
        super().chirp()    #通过super内置类，子类可以调用父类的方法
        print("jijiji")

bird = Bird()
bird.chirp()

summer = Chicken()
summer.chirp()


a = [1,2,3,4,5]
print(dir(a))

class girl(object):
    """
    My sex is a girl,I like the boy-Jingyukai, hope he like me too.
    """
    pass

print(help(girl))

a = (1,3,5)
print(a.count(3))

str = "  Hel lo World"
sub = "World"

str.count(sub)          #自带返回值
#print(str.rfind(sub))   #从右开始，查找sub在str中的第一次出现的位置
#print(str.index(sub))
print(str.isalnum())    #如果所有的字符都是字母或者数字
print(str.isdigit())    #如果所有的字符都是数字
print(str.istitle(),str.isspace(),"是否所有字符都是空格")    #如果所有词的首字母都是大写
print(str.split(" ",4))     #将字符串以空格为分隔符，分成两部分。str.split(分隔符，分割几次)，当然还有rsplit（）
print(str.join(sub))      #将sub中的元素，以str为分隔符
print(str.strip(sub))     #去掉字符串开头和结尾的sub

example_dic = {"a":1,"b":2}
for k in example_dic.keys():
    print(example_dic[k])

for v in example_dic.values():
    print(v)

for k,v in example_dic.items():
    print(k,v)

#example_iter = iter([1,2])
"""
print(example_iter.__next__())
print(example_iter.__next__())
print(example_iter.__next__())
"""
for item in iter([1,2]):
    print(item)


def gen():
    a = 100
    yield a
    a = a*8
    yield a
    yield 1000

for i in gen():
    print(i)

def gen():
    i = 0
    while i < 100000:
        i = i+1
        yield i
for i in gen():
    print(i)

class SampleMore(object):      #定义一个类
    def __call__(self, a):
        return a + 5
add_five = SampleMore()        #类的一个对象
print(add_five(2))

import time as t
import my_time

t.sleep(2)
my_time.sleep()

print(t.tzname)
