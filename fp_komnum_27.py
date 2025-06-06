from math import factorial

# data dari tabel
f0 = 634575                   
delta_f0 = 1039299           
delta_f_1 = 449619            
delta2_f0 = 589680            
delta3_f0 = 292896           
delta3_f_1 = 438696           
delta4_f_1 = 145800          

# nilai s
xs = 14
x0 = 15
h = 3
s = (xs - x0) / h

# rata-rata di delta f(x) dan delta-3 f(x ) pada tabel
delta1 = 0.5 * (delta_f0 + delta_f_1)
delta3 = 0.5 * (delta3_f0 + delta3_f_1)

# nilai f(x) ketika x = 14 dengan menggunakan Stirling
f14 = (f0 + s * delta1 + (s * (s - 1) / factorial(2)) * delta2_f0 + (s * (s - 1) * (s - 2) / factorial(3)) * delta3 + ((xs / 4) * s * (s - 1) * (s - 2) / factorial(3)) * delta4_f_1)

# nilai f(x) ketika x = 14 dengan menggunakan Stirling dengan pembulatan 2 angka di belakang koma
f14 = round(f14, 2)

# Et
yt = 436366
Et = abs((yt - f14) / yt) * 100
Et = round(Et, 2)

# output
print(f"Nilai f(14) dengan interpolasi Stirling: {f14}")
print(f"Nilai Et: {Et}%")
