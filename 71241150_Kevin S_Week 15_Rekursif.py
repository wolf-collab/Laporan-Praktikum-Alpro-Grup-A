print("Soal No.1")
def cek_prima(n, i=2): #n itu bilangan yang mau dicek, kalau 1 itu bilangan pembagi n.
    if n <= 1: #angka yang negatif itu bukan prima.
        return False, ("Bukan Bilangan Prima")
    if n == 2:
        return True, ("Bilangan Prima")
    if i > int(n**0.5):
        return True, ("Bilangan Prima")
    if n % i == 0:
        return False, ("Bukan Bilangan Prima")
    return cek_prima(n, i+1)
print(cek_prima(5))
angka = int(input("Masukkan angka untuk di cek\n>>> "))
print(cek_prima(angka))

print("\nSoal No.2")
def cek_palindrom(kata):
    kalimat = kata.lower()
    n = len(kalimat)
    if n <= 1:
        return True, (f"{teks} adalah Palindrom")
    if kalimat[0] != kalimat[-1]:
        return False, (f"{teks} itu bukan Palindrom")
    return cek_palindrom(kalimat[1:-1])
teks = input("Masukkan kalimat/kata yang mau dicek palindrom apa ngga..?\n>>> ")
print(cek_palindrom(teks))

print("\nSoal No.3")
def deret(n):
    if type(n) is not int or n < 1:
        return "Masukkan bilangan bulat positif aja ya"
    if n == 1:
        return 1
    else:
        return deret(n-1) + (2**(n) - 1)
angka = int(input("Masukkan angka: "))
print(deret(angka))

print("\nSoal No.4")
def hitung(n):
    if type(n) is not int or n < 1:
        return "Masukkan bilangan bulat positif aja ya"
    if n < 10:
        return str(n)
    else:
        angka_akhir = n % 10
        sisa = n //10
        return str(angka_akhir) + "+" + hitung(sisa)

bilangan = int(input("Masukkan angka: "))
hasil_awal = hitung(bilangan)
if hasil_awal.isdigit() or '+' in hasil_awal:
    hasil = eval(hasil_awal)
    print(f"{hasil_awal} = {hasil}")
else:
    print(hasil_awal)

print("\nSoal No.5")
def kombinasi(n, r):
    if r == 0 or r == n:
        return 1
    elif r > n:
        return 0
    else:
        return kombinasi(n-1, r-1) + kombinasi(n-1, r)
n = int(input("Nilai n: "))
r = int(input("Nilai r: "))
hasil = kombinasi(n, r)
print(f"C({n}, {r}) = {hasil}")