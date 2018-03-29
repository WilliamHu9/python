##九九乘法表
'''
for i in range(1,10):
  for j in range(1,i+1):
    print("{0}*{1} = {2:2}".format(j,i,i*j),end=" ")
  print('\n')
'''

f0, f1 = 0, 1
while f1 <= 100:
  print(f1, end = " ")
  t = f1
  f1 = t + f0
  f0 = t