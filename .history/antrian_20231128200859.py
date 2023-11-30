lamda = 5
miu = 1 / 5
s = 2

p0 = 1 / (lamda / miu)
print(round(p0, 2))

p1 = (lamda / miu) * p0
print(round(p1, 2))

p2 = ((lamda / miu) ** 2 ) * p0
print(round(p2, 2))

p3 = ((lamda / miu) ** 3) * p0
print(round(p3, 2))

p4 = ((lamda / miu) **4) * p0
print(round(p4, 2))