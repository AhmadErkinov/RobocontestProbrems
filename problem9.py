input()
nums=[]
for i in input().split():
  nums.append(int(i))
for i in nums:
  if nums.count(i) == 1:
    print(i)
    break