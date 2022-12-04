l1 = input().split()
a,b = int(l1[0]),int(l1[1])       #max()和min()的使用，需要结合遍历：for i in listx
if a < b:
    a,b = b,a
c = 1
# print("%d is bigger than %d" % (a,b))
while a%b != 0:          #终止条件：根据辗转相除法原理，a/b的余数为0
    c = a%b              # c余数       #除数作为下一个的被除数，余数作为下一个的除数
    a = b              #新的被除数
    b = c
print(b)
