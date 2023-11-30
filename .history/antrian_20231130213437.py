# Soal nomor 1
lamda = 1
miu = 1 / 2

p0 = 1 / (109 / 15)
print("P0 =", round(p0, 2))

p1 = (lamda / miu) * p0
print("P1 =", round(p1, 2))

p2 = ((lamda / miu) ** 2) * (1 / (1 * 2)) * p0
print("P2 =", round(p2, 2))

p3 = ((lamda / miu) ** 3) * (1 / (1 * 2 * 3)) * p0
print("P3 =", round(p3, 2))

p4 = ((lamda / miu) ** 4) * (1 / (1 * 2 * 3 * 4)) * p0
print("P4 =", round(p4, 2))

p5 = ((lamda / miu) ** 5) * (1 / (1 * 2 * 3 * 4 * 5)) * p0
print("P5 =", round(p5, 2))

saluran_sibuk = ((0 * p0) + (1 * p1) + (2 * p2) + (3 * p2) + (4 * p4) + (5 * p5)) * p0
print("Rata-rata saluran sibuk =", round(saluran_sibuk, 2))

proporsi_ditolak = saluran_sibuk * 100
print("Rata-rata proporsi ditolak =", round(proporsi_ditolak, 2), "%")

print("")
print("Soal Nomor 2")
print("""
lamda = 2
rate_kedatangan = 2
miu = 1
s = 3""")
lamda = 2
rate_kedatangan = 2
miu = 1
s = 3
p0 = 1 / (1 + (lamda / miu))
print("P0 =", round(p0, 2))

p1 = (lamda / miu) * p0
print("P1 =", round(p1, 2))

p2 = ((lamda / miu) ** 2) * (1 / (1 * 2)) * p0
print("P2 =", round(p2, 2))

p3 = ((lamda / miu) ** 3) * (1 / (1 * 2)) * p0
print("P3 =", round(p3, 2))

p4 = ((lamda / miu) ** 4) * (1 / (1 * 2 * 3 * 4)) * p0
print("P4 =", round(p4, 2))

p5 = ((lamda / miu) ** 5) * (1 / (1 * 23 * 4 * 5)) * p0
print("P5 =", round(p5, 2))

banyaknya_antri = (1 * p4) + (2 * p5)
print("Banyaknya yang antri", round(banyaknya_antri, 2))

lama_antri = banyaknya_antri * rate_kedatangan
print("Rata-rata lama antri =", round(lama_antri, 2))

Utilitas_komputer = (
    (0 * p0) + (1 * p1) + (2 * p2) + (3 * p3) + (4 * p4) + (5 * p5)
) / 3
print("Utilitas Komputer =", round(Utilitas_komputer, 2))

pendapatan_perhari = (1 - p5) * 2 * 8 * 1000
print("Rata-rata pendapatan per hari", round(pendapatan_perhari, 2))

# Soal nomor 4
lamda = 5
laju_pelayanan = lamda
banyaknya_mesin = laju_pelayanan
miu = 0.2
s = 2

p0 = 1 / (lamda / miu)
print("P0 =", round(p0, 2))
# jadi nilai p0 =

p1 = (lamda / miu) * p0
print("P1 =", round(p1))
# jadi nilai p1 =

p2 = (((lamda / miu) ** 2) * (1 / (1 * 2))) * p0
print("P2 =", round(p2))
# jadi nilai p2 =

p3 = ((lamda / miu) ** 3) * p0
print("P3 =", round(p3))
# jadi nilai p3 =

p4 = ((lamda / miu) ** 4) * p0
print("P4 =", round(p4))
# jadi nilai p4 =

p5 = ((lamda / miu) ** 5) * p0
print("P5 =", round(p5))
# jadi nilai p5 =

# Banyaknya mesin yang macet
banyaknya_mesin_macet = (0 * p0) + (1 * p1) + (2 * p2) + (3 * p3) + (4 * p4) + (5 * p5)
print("Banyaknya mesin yang rusak =", banyaknya_mesin_macet)

banyak_antri = (1 * p4) + (2 * p5)
print("Banyaknya yang antri =", round(banyak_antri))
# jadi nilai banyak_antri =

lama_antri = banyak_antri / laju_pelayanan
print("Rata-rata banyaknya yang antri =", round(lama_antri, 2))
# jadi nilai lama_antri =

lama_macet = lama_antri + laju_pelayanan
print("Rata-rata lama macet", round(lama_macet, 2))

waktu_mesin_beroprasi = banyaknya_mesin - banyaknya_mesin_macet
print("Rata-rata waktu mesin beroprasi =", round(waktu_mesin_beroprasi, 2))