l1 = input().split()
h,r = int(l1[0]),int(l1[1])      #单位：cm
v = 3.14159*(r**2)*h/1000       #单位：1 cm^3 = 1e-3 mL
x = 20/v
if x%1 == 0 :
   print(int(x))
else :
   print(int(x+1))
