s=input().split()
num=int(input())
ans = []
for i in range(0, len(s[0]) + 1, num ):
  print(i)
  ans.append(s[0][i])
print(ans)