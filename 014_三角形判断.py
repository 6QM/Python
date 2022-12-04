line = input().split()
l1,l2,l3 = float(line[0]),float(line[1]),float(line[2])
if (l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1) and (l1 - l2 < l3 and l3 - l1 < l2 and l2 - l3 <= l1) :
    print("yes")
else :
    print("no")
