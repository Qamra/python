import random
"""
def my_bin(num): #十进制转换成二进制
    la = []
    if num < 0:
        return '-' + my_bin(abs(num))
    while True:
        num, remainder = divmod(num, 2)
        la.append(str(remainder))
        if num == 0:
            return ''.join(la[::-1])


S = list()
T = list()
K = list()
for a in range(0,random.randint(0,255)): #随机生成0,255之间的一个序列作为种子密钥
    K.append(a)
for i in range(0,256): #生成初始序列S
    S.append(i)
    T.append(K[i % K.__len__()])
#print(K)
#print(S)
#print(T)
j = 0
for i in range(0,256): #S中的元素交换位置
    j = (j + S[i] + T[i]) % 256
    #print("before:",S[i],S[j])
    S[i],S[j] = S[j],S[i]
    #print("changed:",S[i],S[j])
#print(S)

i = 0
j = 0
t = int()
k = list()

while(k.__len__() <= 255): #伪随机密钥生成器
    i = (i + 1) % 256
    j = (j + S[i]) % 256
    S[i], S[j] = S[j], S[i]

    t = (S[i] + S[j]) % 256
    k.append(S[t])

#for b in range(0,k.__len__()):
   # print(my_bin(int(k[b])))

#print(k.__len__())
"""
def rc4():
    data = input("please enter your cleartext:") #输入明文

    def my_bin(num):  # 十进制转换成二进制
        la = []
        if num < 0:
            return '-' + my_bin(abs(num))
        while True:
            num, remainder = divmod(num, 2)
            la.append(str(remainder))
            if num == 0:
                return ''.join(la[::-1])

    data = my_bin(int(data)) #data转化为二进制


    S = list()
    T = list()
    K = list()
    for a in range(0, random.randint(0, 255)):  # 随机生成0,255之间的一个序列作为种子密钥
        K.append(a)
    for i in range(0, 256):  # 生成初始序列S
        S.append(i)
        T.append(K[i % K.__len__()])
    # print(K)
    # print(S)
    # print(T)
    j = 0
    for i in range(0, 256):  # S中的元素交换位置
        j = (j + S[i] + T[i]) % 256
        # print("before:",S[i],S[j])
        S[i], S[j] = S[j], S[i]
        # print("changed:",S[i],S[j])
    # print(S)

    i = 0
    j = 0
    t = int()
    k = list()

    while (k.__len__() <= 255):  # 伪随机密钥生成器
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]

        t = (S[i] + S[j]) % 256
        k.append(S[t])

        # for b in range(0,k.__len__()):
        # print(my_bin(int(k[b])))

        # print(k.__len__())
    secret = []
    secret.append(data ^ my_bin(int(str(k)))) #明文与密钥进行亦或，此处失败
    print(secret)


rc4()








