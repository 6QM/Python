n0 = input()
n = abs(int(n0))
m = int(n)
l = len(str(n))
str0 = ""
if "-" not in n0:  # 先考虑正数,末尾不为0的情况
    while l >= 1 :
        m0 = m
        m %= 10         #获得原数的个位数、十位数
        # print(str(m),end="")
        str0 += str(m)
        m = (m0-m)//10
        l -= 1
    print(int(str0))    #结果转为整型，自动去掉卡前面多余的0

    # print(l1)
# 末尾有多个0
else:  # 考虑负数（剔除符号，最后一个角标值=l-1）
    print("-",end="")
    while l >= 1 :
        m0 = m
        m %= 10         #获得原数的个位数、十位数
        # print(str(m),end="")
        str0 += str(m)
        m = (m0-m)//10
        l -= 1
    print(int(str0))
