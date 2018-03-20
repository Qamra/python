def square_sum(a,b):
    a = a**2
    b = b**2
    c= a + b
    return c
x = square_sum(3,4)
print(x)

def package_position(*all_arguments):
    print(type(all_arguments))
    print(all_arguments)

package_position(1,4,6)
package_position(5,6,7,1,2,3)

example_tuple = (2,2.3,4,5,"happy")
print(example_tuple[-1])    #序列最后一个元素
print(example_tuple[-3])    # 序列倒数第三个元素
print(example_tuple[1:-1])

example_dict = {"tom":11,"sam":57,"lily":100}  #定义一个字典
print(example_dict["tom"])

for a in [3,4.4,"life"]:
    print(a)

for i in range(5):
    print(i,"hello world!")

i=0

while i<10:
    print(i)
    i=i+1

def package_mix(*positions,**keywords): #一个*表示元组，两个*表示字典//包裹位置传参和包裹关键字传参可以混合使用
    print(positions)
    print(keywords)

package_mix(1, 2, 3, a=7, b=8, c=9)

sum = 0            #递归的例子——在非递归时
for i in range(1,101):
    sum = sum + i

print(sum)

def gaussian_sum(n):    #递归时
    if n == 1:
        return 1
    else:
        return n + gaussian_sum(n-1)
print(gaussian_sum(100))

def external_var():    #在函数内部和外部有同名变量时，函数会优先使用函数帧中的变量。对外部的变量不会产生影响。
    info = "Qamra is a nice girl"
    print(info)

info = "jing is a handsome boy"
external_var()
print(info)

a = 1      # 在函数调用时，会把数据赋值给变量，等到函数返回时，这些参数相关的变量会被清空。
           # （自己的话来说，应该就是形参和实参的关系）
def test(a):
    a = a + 1
    return a
print(a)
print(test(a))


