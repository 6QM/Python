l1 = input().split()
n,x,y = int(l1[0]),int(l1[1]),int(l1[2])
fin = n - y/x             # 所有苹果-虫子吃掉的苹果（包括正在吃的）
if int(fin//1) <= 0 :
    print(0)
elif fin%1 == 0 :
    print(int(fin))
else:
    print(int(fin//1))         # n=10 , x = 3, y = 5 -> fin = 10 - 5/3
