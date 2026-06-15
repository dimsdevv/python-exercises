# 1. STRING, INTEGER, FLOAT (Data Tunggal)
nama_lengkap = "Dimas Sholihulhadi" # Tipe: str
umur = 20                           # Tipe: int
ipk = 3.71                          # Tipe: float
is_aktif = True                     # Tipe: bool (Boolean)

# 2. LIST (Daftar mata kuliah - Bisa ditambah/hapus)
mata_kuliah = ["Algoritma", "Basis Data", "Sistem Informasi"]
mata_kuliah.append("Statistika") # Menambah data baru

# 3. TUPLE (Data yang tidak boleh berubah, misal: Tanggal Lahir & ID)
# Kita gunakan Tuple karena ID Mahasiswa bersifat permanen
identitas_tetap = ("SI-2024-001", "01-Januari-2004")

# 4. SET (Mencatat ID Ruangan yang pernah dikunjungi)
# Set otomatis menghapus duplikat
ruangan_dikunjungi = {"R.101", "R.202", "R.101", "Lab. Komputer"}

# 5. DICTIONARY (Data lengkap dalam satu wadah/objek)
# Sangat krusial di Data Science untuk representasi record
profil_mahasiswa = {
    "nama": nama_lengkap,
    "ipk": ipk,
    "status": is_aktif,
    "krs": mata_kuliah
}

# --- MENAMPILKAN HASIL ---
print("--- Laporan Data Mahasiswa ---")
print(f"Nama     : {profil_mahasiswa['nama']}")
print(f"ID       : {identitas_tetap[0]}")
print(f"Matkul 1 : {mata_kuliah[0]}") # Mengambil index ke-0
print(f"Ruangan  : {ruangan_dikunjungi}") # Lihat! R.101 hanya muncul sekali