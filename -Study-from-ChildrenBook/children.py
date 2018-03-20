class Animal:
    def __init__(self,species,number_of_legs,color):
        self.species = species
        self.number_of_legs = number_of_legs
        self.color = color



import copy
harry = Animal('hippogriff',6,'pink')
carrie = Animal('chaimera',4,'green polka dots')
billy = Animal('bogill',0,'paisley')
my_animal = [harry,carrie,billy]
more_animals = copy.copy(my_animal)
print(more_animals[2].species)

import random
import easygui
import sys
import time
import copy
import turtle
"""
num = random.randint(1,100)
print('Guess a number between 1 and 100')
while(True):
   guess = easygui.integerbox()
   #i = int(guess)
   if guess == num :
       print('You guessed right')
       break
   elif guess < num :
       print('try higher')
   elif guess > num:
       print('try lower')

desserts = ['ice cream','pancakes','brownies','cookies','candy']
random.shuffle(desserts)
choice = easygui.choicebox('chooese one','111 ',desserts)
print('you choosed',choice)

v = sys.stdin.readline()
print(v)
sys.stdout.write('333')


def lots_of_numbers(max):
    t1 = time.time()
    for x in range(0,max):
        print(x)
    t2 = time.time()
    print('it took %s seconds' % (t2-t1))

lots_of_numbers(10000000)


class Car:
    pass
car1 = Car()
car1.wheels = 4
car2 = car1
car2.wheels = 3
print(car1.wheels)
car3 = copy.copy(car1)
car3.wheels = 6
print(car1.wheels)


t = turtle.Pen()
t.reset()
for x in range(1,19):
    t.forward(100)
    if x%2 == 0:
        t.left(175)
    else:
        t.left(225)


t = turtle.Pen()
t.color(1,0,0)
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(60)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)
t.end_fill()

t.color(0,0,0)
t.up()
t.forward(10)
t.down()
t.begin_fill()
t.circle(10)
t.end_fill()

t.setheading(0)
t.up()
t.forward(90)
t.right(90)
t.forward(10)
t.setheading(0)
t.begin_fill()
t.down()
t.circle(10)
t.end_fill()

t.color(1,1,0)
t.begin_fill()
t.circle(50)
t.end_fill()
"""
def hello():
    print('hello')

from tkinter import *
tk = Tk()
canvas = Canvas(tk,width=500,height=500)
canvas.pack()
canvas.create_line(0,0,500,500)
