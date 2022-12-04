l1 = input()
n1 = l1.split()[0][0]
n2 = l1.split()[0][1]
n3 = l1.split()[1][0]
n4 = l1.split()[1][1]
print(int(n1+n2)+int(n3+n4))       # 对字符串线拼接，再转为整型
