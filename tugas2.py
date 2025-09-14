# muhamad rizki ramadhan

suhu_mingguan = [28, 30, 29, 31, 27, 28, 30]

suhu_terpanas = max(suhu_mingguan)
suhu_terdingin = min(suhu_mingguan)
print(f"Suhu terpanas: {suhu_terpanas}°C")
print(f"Suhu terdingin: {suhu_terdingin}°C")

total_suhu = 0
for suhu in suhu_mingguan:
    total_suhu += suhu

rata_rata = total_suhu / len(suhu_mingguan)
print(f"Suhu rata-rata: {rata_rata:.2f}°C")

hari_diatas_rata = 0
for suhu in suhu_mingguan:
    if suhu > rata_rata:
        hari_diatas_rata += 1

print(f"Jumlah hari dengan suhu di atas rata-rata: {hari_diatas_rata}")

# -muhamad rizki ramadhan