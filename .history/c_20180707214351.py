import math
num_str=input().split()
num = list(map(int, num_str))
n = list[0]
m = list[1]
d = list[2]
num = math.pow(n, m)
score=0
for i in range(m):
  for j in range(1, n + 1):
    if j + d <= n or (j - d > 0 and j - d <= n):
      score+=1
print(score/num)