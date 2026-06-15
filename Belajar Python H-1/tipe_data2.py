#Membuat List Hobi
list_hobi = ["Membaca", "Olahraga", "Musik", "Traveling"]

#Menambah Data Append
list_hobi.append("Memasak")
list_hobi.append("Koding")
list_hobi.append("Fotografi")

#Mengubah Data
list_hobi[1] = "Menonton Film"
list_hobi[2] = "Bermain Game"
list_hobi[3] = "Berkebun"

#Menghapus Data
list_hobi.remove("Membaca")

print(f"Daftar Hobi Terbaru: {list_hobi}")
print(f"Jumlah Hobi: {len(list_hobi)}")