import math

def is_prime(n):

    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        sqrt_n = int(math.sqrt(n)) + 1
        for i in range(3, sqrt_n, 2):
            if n % i == 0:
                return False
        return True



tub_sonlar = 0
for son in range(2, int(input())+1):
  if  is_prime(son):
    tub_sonlar += 1
if tub_sonlar % 2 == 0:
  print("Bobur")
else:
  print("Ali")