#Contoh Definisi Variable Yang ada di Python
nama = "Dimas Sholihulhadi" #Tipe Data String
umur = 19                 #Tipe Data Integer
ipk = 3.71                #Tipe Data Float
Aktif = True              #Tipe Data Boolean

#Untuk Menampilkan Output:
#bisa menggunakan fungsi print() dengan format string
print(f"Mahasiswa Bernama {nama} dengan umur {umur} tahun, IPK {ipk}, dan status aktif: {Aktif}")

#bisa juga menggunakan fungsi print() dengan format string biasa
print("Mahasiswa Bernama {} dengan umur {} tahun, IPK {}, dan status aktif: {}".format(nama, umur, ipk, Aktif))

#bisa juga menggunakan fungsi print() dengan format string lama
print("Mahasiswa Bernama %s dengan umur %d tahun, IPK %.2f, dan status aktif: %s" % (nama, umur, ipk, Aktif))

#Operasi Sederhana
tahun_depan = umur + 1
print(f"Umur Tahun Depan: {tahun_depan}")


