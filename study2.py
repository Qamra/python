print (1+9)
print (10%3)
print ("Vamei say:"+"Hello World")
print ("Vamei"*2)
print (860000*(0.15+0.2)<=400000 and 860000*0.15<130000)
tuple=(2,2.3,'yeah"',5.6,False)
list=[True,5,'smile']
print (type(tuple))
print (type(list))
print (tuple,list)
print(tuple[-5])
if list[1]>6:
    print(True)
else:
    print(False)
a = 5
if a in list:
    print(list.index(5))
total = 500000
interest_tuple = (0.01,0.02,0.03,0.035)
i     = 0
repay = 30000

while total>0:
    i = i + 1
    print("第",i,'年还是要还钱')
    if i <= 4:
        interest = interest_tuple[i - 1]
    else:
        interest = 0.05
    total = total * (interest + 1) - repay
print("第",i+1,"年终于还清了")
