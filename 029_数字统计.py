n = input().split()          #给定范围区间,将区间整数转化为字符串，进行遍历
total = 0
str1 = ""
# for i in range(int(0),int(1),1):
for i in range(int(n[0]),int(n[1])+1):           #注意 i是整型
    str1+=str(i)          #将遍历的序号转换为字符串，收集起来
    if "2" in str(i):          #对每一个字符串，进行单个字符检查
        c = len(str(i))
        while c != 0:
            if i %10 == 2:                 #对整型i进行（最右边的）个位数的检查，看是否有“2”,其次，检查其左边一位（办法：先除以10，在对2进行求余,看结果是否等于2）
                total += 1
            i = i //10
            c -= 1
# print(str1)
print(total)
