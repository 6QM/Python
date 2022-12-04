l1 = input()
x = float(l1.split()[0])
a = float(l1.split()[1])
b = float(l1.split()[2])
c = float(l1.split()[3])
d = float(l1.split()[4])
f = a*x**3 + b*x**2 + c*x +d

print("%.7f" % (f))                #字符串中的格式控制符，格式控制符只能出现在字符串中
