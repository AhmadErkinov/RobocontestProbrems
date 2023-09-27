def solve(n: int, k: int) -> int:
  if n == 0:
    return 0
  else:
    return k+1

temp = list(map(int, input().split()))

print(solve(temp[0], temp[1]))