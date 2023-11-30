# Soal nomor 1
lamda = 1
miu = 1 / 2

p0 = 1 / (109 / 15)
print(round(p0, 2))

p1 = (lamda / miu) * p0
print(round(p1, 2))

p2 = ((lamda / miu) ** 2) * (1 / (1 * 2)) * p0
print(round(p2, 2))

p3 = ((lamda / miu) ** 3) * (1 / (1 * 2 * 3)) * p0
print(round(p3, 2))

p4 = ((lamda / miu) ** 4) * (1 / (1 * 2 * 3 * 4)) * p0
print(round(p4, 2))

p5 = ((lamda / miu) ** 5) * (1 / (1 * 2 * 3 * 4 * 5)) * p0
print(round(p5, 2))

saluran_sibuk = ((0 * p0) + (1 * p1) + (2 * p2) + (3 * p2) + (4 * p4) + (5 * p5)) * p0
print(round(saluran_sibuk, 2), "%")

proporsi_ditolak = saluran_sibuk * 100
print(round(proporsi_ditolak, 2), "%")

# # Soal nomor 4
# lamda = 5
# laju_pelayanan = lamda
# banyaknya_mesin = laju_pelayanan
# miu = 0.2
# s = 2

# p0 = 1 / (lamda / miu)
# print(round(p0, 2))
# # jadi nilai p0 =

# p1 = (lamda / miu) * p0
# print(round(p1))
# # jadi nilai p1 =

# p2 = (((lamda / miu) ** 2) * (1 / (1 * 2))) * p0
# print(round(p2))
# # jadi nilai p2 =

# p3 = ((lamda / miu) ** 3) * p0
# print(round(p3))
# # jadi nilai p3 =

# p4 = ((lamda / miu) ** 4) * p0
# print(round(p4))
# # jadi nilai p4 =

# p5 = ((lamda / miu) ** 5) * p0
# print(round(p5))
# # jadi nilai p5 =

# # Banyaknya mesin yang macet
# banyaknya_mesin_macet = (0*p0 + 1*p1 + 2*p2 + 3*p3 + 4*p4 + 5*p5)
# print (banyaknya_mesin_macet)

# banyak_antri = (1 * p4) + (2 * p5)
# print(round(banyak_antri))
# # jadi nilai banyak_antri =

# lama_antri = banyak_antri / laju_pelayanan
# print(round (lama_antri,2))
# # jadi nilai lama_antri =

# lama_macet = lama_antri + laju_pelayanan
# print(round(lama_macet,2))

# waktu_mesin_beroprasi = banyaknya_mesin - banyaknya_mesin_macet
# print (waktu_mesin_beroprasi)
