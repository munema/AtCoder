import math
num_str=input().split()
num = list(map(int, num_str))
n = num[0]
m = num[1]
d = num[2]
num = math.pow(n, m)
score = 0
for i in range(1,m+1):
  for j in range(1, n + 1):
    for k in range(1, n + 1):
      if abs(j - k) == d:
        score += math.pow(n,m-i-1)
print(score/num)