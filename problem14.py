import math
def solve(n: int, k: int) -> int:
  if n == 0:
    return 1
  else:
    return int(math.pow(k+1, n))

temp = list(map(int, input().split()))

print(solve(temp[0], temp[1]))