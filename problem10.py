N_num = int(input())
ABC = 0
for i in input().split():
  ABC += int(i)
if ABC >= N_num:
  print("Yes")
else:
  print("No")