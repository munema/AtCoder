s=input().split()
num=int(input())
ans = []
for i in range(0,len(s)+1,num-1):
  ans.append(s[0][i])
print(ans)