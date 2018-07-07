s=input().split()
num=int(input())
ans = ""
for i in range(0, len(s[0]), num):
  print(i)
  ans=ans+s[0][i]
print(ans)