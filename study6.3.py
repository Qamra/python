"""import turtle
turtle.forward(90)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(50)

turtle.reset()
turtle.forward(50)
turtle.left(120)
turtle.forward(50)
turtle.left(120)
turtle.forward(50)

turtle.reset()
for i in range(1,5):
    turtle.up()
    turtle.forward(20)
    turtle.down()
    turtle.forward(50)
    turtle.up()
    turtle.forward(20)
    turtle.right(90)

twinkies = int(input("how much cake do you have?"))
if twinkies <100 or twinkies > 500:
    print("not so little or too many")

money = int(input("huw much money do you have?"))
if money >=100 and money <= 500:
    print("you are too poor")
elif money >=1000 and money <=5000:
    print("you sre rich")

test_list = ['a','b','c','d','e',666]
for i in test_list:
    print(i)

hugehairypants = ['huge','hairy','pants']
for i in hugehairypants:
    print(i)
    for j in hugehairypants:
        print(j)

found_coins = 20
magic_coins = 70
stolen_coins = 3
coins = found_coins
for week in range(1,53):
    coins = coins + magic_coins -stolen_coins
    print('Week %s = %s' % (week,coins))
for x in range(0,20):
    print('hello %s'%x)
    if x < 9:
        break
i = 0
j = 0
while i <= 21 and j == 0:
    if i % 2 == 0:
        print(i)
    i = i+1

ingredient = ['snails','leeches','gorilla belly-button lint','caterpillar eyebrows','centipede toes']
for i in range(0,5):
    print('%s %s'%(i+1,ingredient[i]))

weight = 53
for i in range(1,16):
    weight = weight+1
    print('%s year,my weight is %s'%(i,weight*0.165))
    print(weight)

def testfunc(myname,yourname):
    print('Hello %s, %s like you, but you don\'t know' % (yourname,myname))
testfunc('Qamra','Markrov')

def saving(pocket_money,paper_rout,spending):
    return pocket_money + paper_rout - spending
print(saving(10,10,5))


import sys
print(sys.stdin.readline())

def moon_weight(weight,each,year):
    for i in range(0,year):
        weight = weight + each
        print('%s year,my weight is %s' % (i, weight * 0.165))
        print(weight)

moon_weight(53,1,15)

import sys
def moon_weight():
    print('Please enter your current Earth weight')
    weight = int(sys.stdin.readline())
    print('Please enter the amount your weight migth increase each year')
    each = int(sys.stdin.readline())
    print('Please enter the number of years')
    year = int(sys.stdin.readline())
    for i in range(0, year):
        weight = weight + each
        print('%s year,my weight is %s' % (i, weight * 0.165))
        print(weight)

moon_weight() #第七章课后习题
"""
"""
import turtle
class Things:
    pass
class Inanimate(Things):
    pass
class Animate(Things):
    pass
class Sidewalks(Inanimate):
    pass
class Animals(Animate):
    def breathe(self):
        print('breathing')
    def move(self):
        #print('moving')
        self = turtle.Pen()
        self.forward(60)

        self.reset()
        self.backward(60)
        self.reset()
        self.left(90)
        self.forward(60)
        self.reset()
        self.right(90)
        self.forward(60)
    def eat_food(self):
        print('eating food')
class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding young')
class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print('eating leaves')
    def find_food(self):
        self.move()
        print("I\'ve found food!")
        self.eat_food()
    def dance_a_jig(self):
        self.move()
    def __init__(self,spots):
        self.giraffe_spots = spots

reginald = Giraffes(50)
#reginald.move()
#reginald.eat_leaves_from_trees()
#reginald.breathe()
#reginald.eat_food()
#reginald.find_food()
reginald.dance_a_jig()

print(reginald.giraffe_spots)

import turtle
avery = turtle.Pen()
kate = turtle.Pen()
jacob = turtle.Pen()
avery.forward(50)
avery.right(90)
avery.forward(20)

kate.left(90)
kate.forward(100)

jacob.left(180)
jacob.forward(80)

kate = turtle.Pen()
kate.right(90)
kate.forward(100)




import turtle
class Turtle:
    def move(self,b,c,d):
        self = turtle.Pen()
        self.forward(100)
        d = turtle.Pen()
        d.forward(100)
        self.left(90)
        self.forward(50)
        d.right(90)
        d.forward(50)
        c,b = turtle.Pen(),turtle.Pen()
        c.forward(120)
        b.forward(120)
        c.left(90)
        c.forward(30)
        b.right(90)
        b.forward(30)

t = Turtle()
b = Turtle()
c = Turtle()
d = Turtle()
t.move(b,c,d)

year = input("Year of birth")
if not bool(year.rstrip()): #判断用户是否输入
    print("you must input your year")
"""

test_file = open('/home/qamra/JYK.txt','w')
text = test_file.write('I miss you as don\'t see you severl hours' )
test_file = open('/home/qamra/JYK.txt')
text_1 = test_file.read()
print(text_1)

a = abs(10) + abs(-10)
print(a)
b = abs(-10) + -10
print(b)


print("this if is you not are a reading very this good then way".rsplit('t'))

