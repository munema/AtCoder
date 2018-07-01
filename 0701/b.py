n=int(input())
num_str=input().split()
num=list(map(int, num_str))
print(max(num)-min(num))