import math
num_str=input().split()
num = list(map(int, num_str))
n = num[0]
m = num[1]
d = num[2]
num = math.pow(n, m)
score = 0
for i in range(m):
  for j in range(1, n + 1):
    for k in range(1, n + 1):
      if abs(j - k) == d:
        count=1
        for product in range((i + 2), m):
          print(1)
          product += math.pow(n,count)
          count+=1
        score+=1*(i+2)
print(score/num)