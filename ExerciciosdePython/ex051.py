t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = t + (10 - 1)* r
print(d)
for i in range(t, d+1, r):
     print('{}'.format(i),end=' -> ')
print('Acabou')

