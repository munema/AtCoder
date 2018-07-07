num_str=input().split()
num=list(map(int, num_str))
a=num[0]
b=num[1]
if a+b==15:
  print ("+")
elif a*b==15:
  print ("*")
else:
  print ("x")