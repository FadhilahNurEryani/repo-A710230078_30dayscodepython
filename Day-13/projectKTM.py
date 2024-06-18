import os
#membuat list data mahasiswa
data_mahasiswa = [
    {'Nama': 'KIM TAEHYUNG', 'NIM': 'A710xxx', 'Prodi': 'Pendidikan Teknik Informatika'},
    {'Nama': 'JEON JUNGKOOK', 'NIM': 'A710xxx', 'Prodi': 'Pendidikan Teknik Informatika'},
    {'Nama': 'HAN SO HEE', 'NIM': 'A710xxx', 'Prodi': 'Pendidikan Teknik Informatika'},
    {'Nama': 'LALISA', 'NIM': 'A710xxx', 'Prodi': 'Pendidikan Teknik Informatika'}
]

#fungsi mencari data mahasiswa berdasarkan nama
def cari_mahasiswa(nama):
    for mahasiswa in data_mahasiswa:
        if mahasiswa ['Nama'].lower() == nama.lower():
            return mahasiswa
    
#input nama mahasiswa yang dicari
while True:
    cari_nama = input("Masukkan nama Mahasiswa yang anda cari : ")

#tampilkan data
    hasil_cari =cari_mahasiswa(cari_nama)
    if hasil_cari:
        print("\nData Mahasiswa ditemukan:")
        print(f"Nama: {hasil_cari['Nama']}\nNIM: {hasil_cari['NIM']}\nProdi: {hasil_cari['Prodi']}\n")
        break
    else:
        print(f"\nData Mahasiswa dengan nama {cari_nama} tidak ditemukan. Silahkan coba lagi")
