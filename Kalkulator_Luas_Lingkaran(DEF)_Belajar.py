def luas_lingkaran(pi:float, r:float) -> float :
    return pi * r * r
    
print("Pilih pi")
print("A.3.14")
print("B.22/7")
pilihan = input("Masukan Pilihan: ").upper()

r = float(input("Masukan Jari-Jari: "))

if pilihan == 'A' :
    pi=3.14
elif pilihan == 'B' :
    pi=22/7
else :
    print("Error")
    exit()
    
hasil = luas_lingkaran(pi, r)
print(f"Jadi Hasilnya Adalah {round(hasil, 2)} ")  
      
    
        
    