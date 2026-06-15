#Aritmatika Python
target_penjualan = 70000
total_penjualan = 40000

#Cek apakah target penjualan tercapai
bonus_karyawan = total_penjualan > target_penjualan
print("Apakah karyawan mendapatkan bonus?", bonus_karyawan)

#Menghitung Presentase Penjualan
persentase = (total_penjualan / target_penjualan) * 100
print(f"Persentase Penjualan: {persentase:.2f}%")

