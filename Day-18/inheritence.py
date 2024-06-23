class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def kenalan(self):
        print(f"Halo, namaku {self.nama}, umurku {self.umur}")

class Mahasiswa(Orang):
    def __init__(self, nama, umur, universitas):
        super().__init__(nama, umur)
        self.universitas = universitas

    def kenalan(self):
        print(f"Halo, namaku {self.nama}, umurku {self.umur}, dan aku kuliah di {self.universitas}")

class Pekerja(Orang):
    def __init__(self, nama, umur, tempatkerja):
        super().__init__(nama, umur)
        self.tempatkerja = tempatkerja

    def kenalan(self):
        print(f"Halo, namaku {self.nama}, umurku {self.umur} dan aku kerja di {self.tempatkerja}")

objek1 = Orang('Dila', '19')
objek1.kenalan()
objek2 = Mahasiswa('Jennie', '19', 'UMS')
objek2.kenalan()
objek3 = Pekerja('Lisa', '19', 'UMS')
objek3.kenalan()