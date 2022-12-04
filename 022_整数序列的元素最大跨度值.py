n = input()
s = input().split()
maxV = minV = int(s[0])
for x in s:
    # if maxV < int[x] :
    #     maxV = int[x]
    maxV = max(maxV,int(x))             #注意x的含义是对应角标下的字符串中的元素！！
    minV = min(minV,int(x))
print(maxV-minV)
