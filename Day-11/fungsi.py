def apakah_prima(bilangan):
    if bilangan > 1 :
        for i in range(2, int(bilangan/2)+ 1):
            if (bilangan % i) == 0:
                return"Bukan bilangan prima"
        else :
            return"Bilangan prima"
    else :
        return"Bukan bilangan prima"
    
bilangan = int(input("Masukkan bilangan: "))
hasil = apakah_prima(bilangan)
print(hasil)