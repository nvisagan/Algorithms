def foo(n):
  sq_root = int(math.sqrt(n))
  for i in range(0, sq_root):
    print(i)

#Linear O(log n)

def bar(x):
  sum = 0
  for i in range(0, 1463):
    i += sum
    for j in range(0, x):
      for k in range(x, x + 15):
        sum += 1

# Polynomial O(n^c)

def baz(array):
  print(array[1])
  midpoint = len(array) // 2
  for i in range(0, midpoint):
    print(array[i])
  for _ in range(1000):
    print('hi')

#Exponential O(c^n)