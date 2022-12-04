import math
l1 = input().split()
a,b,c = float(l1[0]),float(l1[1]),float(l1[2])
if b*b == 4*a*c :                    #注意等号与赋值的区别
    x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)      #x1=x2
    x2 = x1
    print("x1=x2=%.5f" %(x1) )
elif b*b > 4*a*c :
    x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)          #x1>x2
    x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    print("x1=%.5f;x2=%.5f" %(x1,x2) )
elif b*b < 4*a*c :
    x1a = -b/(2*a)                   #x1实部

    x1b = math.sqrt(4*a*c-b*b)/(2*a)     #x1虚部
    # x1 = x1a + "+" + x1b + "i"        #x1>x2
    x2a = -b/(2*a)                  #x2实部
    x2b = math.sqrt(4*a*c-b*b)/(2*a)     #x2虚部
    # x2 = x1a + "-" + x1b + "i"        #x1>x2
    if abs(x1a) == 0 and abs(x2a) == 0 :
        x1a = abs(x1a)
        x2a = abs(x2a)

    elif abs(x2a) == 0 :
        x2a = abs(x2a)
    elif abs(x1a) == 0 :
        x1a = abs(x1a)
    # if abs(x1a) == 0 and abs(x2a) == 0 :
    #     print("x1=%.5f+%.5fi;x2=%.5f-%.5fi" % (abs(x1a), x1b, x2a, x2b))
    # elif abs(x2a) == 0 :
    #     print("x2=%.5f+%.5fi;x2=%.5f-%.5fi" % (x1a, x1b, abs(x2a), x2b))

    print("x1=%.5f+%.5fi;x2=%.5f-%.5fi" % (x1a, x1b, x2a, x2b))
