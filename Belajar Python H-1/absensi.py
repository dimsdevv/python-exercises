#Membuat Absensi Sederhana

nilai_absensi = 90

if nilai_absensi >= 90:
    grade = "A (Sangat baik)" 
elif nilai_absensi >= 80:
    grade = "B (Baik)"
elif nilai_absensi >= 70:
    grade = "C (Cukup)"
else:
    grade = "D (Kurang)"

    print(f"Hasil Absensi: {grade}")