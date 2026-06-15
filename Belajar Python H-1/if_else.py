#Filter Data Penjualan

stok_barang = 5

if stok_barang >= 20:
    print("Stok Melimpah.")
elif stok_barang >= 10 and stok_barang < 20:
    print("Stok Aman.")
else:
    print("Segera Restock!")
