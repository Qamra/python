from study3 import a
print(a)

while True:      #程序的异常处理，异常处理的程序需要包裹在try结构中，except说明当特定错误发生时，程序应该如何应对。
    inputStr = input("Please input a number:")
    try:
        num = float(inputStr)
        print("Input number:",num)
        print("result:",10/num)
    except:
        print("Please try again.")
import this

