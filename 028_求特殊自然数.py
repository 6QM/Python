x = 49                                            # 从49开始
n10 = 0
str7 = ""
str71 = ""
str9 = ""
str91 = ""
while 1:  # and (1< int(str7)//100 < 9) and  (1< int(str91)//100 < 9):
    n10 = x
    n7 = n10
    n9 = n10
    while n10 != 0:  # 将10进制转换为7进制
        m0 = n10
        n10 %= 7
        str7 += str(n10)
        n10 = m0 // 7
    # print(str7+"7777777")                           # 逆序，则其该十进制的九进制为此数目的逆序
    l = len(str7) - 1
    for i in range(l, -1, -1):
        str71 += str7[i]              # 顺序，则其该十进制的七进制为此数目
    while n9 != 0:  # 将10进制转换为9进制
        m1 = n9
        n9 %= 9
        str9 += str(n9)
        n9 = m1 // 9
    # print(str9)  # 逆序，则其该十进制的九进制为此数目的逆序
    # 将字符串逆序为正常的九进制
    l = len(str9) - 1
    for i in range(l, -1, -1):
        str91 += str9[i]               # 顺序，则其该十进制的九进制为此数目
    # print(str91+"9999999")
    # 于此，求出这个十进制自然数的判断条件是：循环执行，使得其7进制的逆序与9进制的顺序“相等”时的三位十进制数值，为所求自然数
    # print(str(x))
    # print(str(x)+"到这一步了")
    if str91 == str7 or x >=1000 :
        print(str(x))
        print(str71)
        print(str91)
        break
    n10 = 0
    str7 = ""
    str71 =""
    str9 = ""
    str91 = ""
    x += 1
