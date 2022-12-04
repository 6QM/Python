d = int(input())
l1 = []
for i in range(d):
    l1 += input().split()         # 添加>>>.split()<<<可以将键入字符间的多余的空格去掉
a = len(l1)
# print(a)
Au = 0
Ag = 0
Cu = 0
while a != 0 :
    b = a - 1
    c = a - 2
    a -= 3
    Cu += int(l1[a-1])           #注意角标最开始是从l1[0]开始，因而对长度应该左偏移1个位置
    Ag += int(l1[b-1])
    Au += int(l1[c-1])
# print(l1)
print("%d %d %d %d" %(Au,Ag,Cu,(Au+Ag+Cu)))
