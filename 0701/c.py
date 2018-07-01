import math
n=int(input())
num_str=input().split()
num=list(map(int, num_str))
num=[num[i]-i-1 for i in range(n)]
ans = math.inf
max_abs=max(max(num),abs(min(num)))
for b in range(-max_abs,max_abs):
    ans_element=list(map(lambda x:abs(x-b), num))
    now_ans=sum(ans_element)
    ans=min(ans,now_ans)
print(ans)