s=input().split()
num=int(input())
ans = []
for i in range(0,len(s),num):
  ans=ans.append(s[i])
print(ans)