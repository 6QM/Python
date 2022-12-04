n = int(input())
s = [""]
m = n
while n != 0 :
    s+= input().split()          #用加号来对一个字符串连续存入多个字符
    n -= 1
    # print(s ,str(n))
total = 0
for i in range(1,m+1) :          #由于第一个字符内容为空，故角标从1开始
    total+=int(s[i])
print("%d %.5f" % (total,total/m))
