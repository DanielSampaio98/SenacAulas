# determinando valor de a, b, c
a = 1
b = 5
c = 3

#determinei o valor de Delta e fiz ele receber a formula
delta = (b**2) - (4*a*c)

print(delta)
if delta > 0:
     x1 = (-b + (delta)**0.5) / (2*a)
     x2 = (-b - (delta)**0.5) / (2*a)
     print(f"As os valores raiz de x são: x1 = {x1}, x2 = {x2}")
if delta == 0:
     x1 = -b / (2*a) 
     print(f"o unico valor raiz de x é: x1 = {x1}")

