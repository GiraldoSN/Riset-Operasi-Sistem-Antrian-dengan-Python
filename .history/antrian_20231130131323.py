lamda = 5
miu = 0.2
s = 2

p0 = 1 / (lamda / miu)
print(round(p0, 2))
# jadi nilai p0 =

p1 = (lamda / miu) * p0
print(round(p1, 2))
# jadi nilai p1 =

p2 = (((lamda / miu) ** 2) * (1 / (1 * 2))) * p0
print(round(p2, 2))
# jadi nilai p2 =

p3 = ((lamda / miu) ** 3) * p0
print(round(p3, 2))
# jadi nilai p3 =

p4 = ((lamda / miu) ** 4) * p0
print(round(p4, 2))
# jadi nilai p4 =

p5 = ((lamda / miu) ** 5) * p0
print(round(p5, 2))
# jadi nilai p5 =

banyak_antri = (1 * p4) + (2 * p5)
print(round(banyak_antri))
