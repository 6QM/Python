n = int(input())
l1 = []
for i in range(n):
    l1 += input().split()
#读入所有实验组数据
# print(l1)
y = 0
x = 0
for i in range(0,len(l1),2):
    y = int(l1[i+1])/int(l1[i])      #注意i=0时，为x;注意除数与被除数：被除数/除数=每一种组的（每一行中的）左/右
    if i == 0 :
        x = y
        # print("x = %.5f" %x)        #这一条只为了获取x，无需输出任何值
    else:
        # print("y = %.5f" %y)        #对n-1组实验数据进行有效率的判断
        if x-y < -0.05:
            print("better")
        elif x-y > 0.05:
            print("worse")
        else:
            print("same")
