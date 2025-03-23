#Latihan 6.1
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+ 1):
        if num % i == 0:
            return False
    return True
def primaTerdekat():
    angka = int(input("Masukkan angka yang mau dicek :\n>>> "))
    if is_prime(angka):
        print(f"{angka} itu Bilangan Prima.")
        return
    if angka <= 2:
        print("Angka prima terdekatnya adalah = 2")
        return
    for i in range(angka-1, 1, -1):
        if is_prime(i):
            print(f"Bilangan prima terdekat dari {angka} adalah {i}")
            return
primaTerdekat()

#Latihan 6.2
print("\n")
baris = int(input("Masukkan banyak baris:\n>>> "))
for angka in range(baris, 0, -1):
    faktorial = 1
    for i in range(1, angka + 1):
        faktorial *= i
    deret = " ".join(str(x) for x in range(angka, 0, -1))
    print(f"{faktorial} {deret}")

#Latihan 6.3
print("\n")
baris = int(input("Masukkan tingginya berapa\n>>> "))
kolom = int(input("Masukkan lebarnya berapa\n>>> "))
angka = 1
for i in range(baris):
    for j in range(kolom):
        print(angka, end=" ")
        angka += 1
    print()