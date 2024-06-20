#membuat list harga barang
listharga = {
    'kopi': 2500,
    'teh': 3500,
    'susu': 5000
}
subtotal = {'kopi': 0, 'teh': 0, 'susu': 0}
barang_dibeli = []
while True:
    beli_barang = input("Masukkan nama barang(ketik 'end' untuk mengakhiri): ")
    if beli_barang == 'end':
        break

    if beli_barang in listharga:
        jumlah_barang = int(input("Masukkan jumlah barang: "))
        harga_barang = listharga[beli_barang]
        subtotal[beli_barang]+= harga_barang * jumlah_barang
        barang_dibeli.append((beli_barang, harga_barang, jumlah_barang))
total = sum(subtotal.values())

file = open('invoice.txt','w')
file.write('=======RINCIAN=======\n')
for barang, harga, jumlah, in barang_dibeli:
    file.write(f"{barang} : Rp{harga} x {jumlah}pcs\n")
file.write('=====================\n')
for barang, sub in subtotal.items():
    file.write(f"Subtotal{barang} : Rp{sub}\n")
file.write(f"TOTAL : Rp {total}\n")
file.close()
tampil_file = open('invoice.txt', 'r')
print(tampil_file.read())