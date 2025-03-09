#latihan 4.1
def cek_angka(angka1, angka2, angka3):
    if angka1 == angka2 or angka1 == angka3 or angka2 == angka3:
        return False
    if angka1 + angka2 == angka3 or angka1 + angka3 == angka2 or angka2 + angka3 == angka1:
        return True
    else:
        return False
print("Latihan 4.1")
print(cek_angka(5, 4, 9))
print(cek_angka(5, 2, 3))
print(cek_angka(1, 5, 8))
print(cek_angka(114, 0, 9))
print(cek_angka(15, 14, 9))
print("\nLatihan4.2")

#Latihan 4.2
def cek_digit_belakang(angka_1, angka_2, angka_3):
    angka1 = angka_1 % 10
    angka2 = angka_2 % 10
    angka3 = angka_3 % 10
    if angka1 == angka2 or angka1== angka3 or angka2== angka3:
        return True
    else:
        return False
print(cek_digit_belakang(30, 20, 18))
print(cek_digit_belakang(145, 5, 100))
print(cek_digit_belakang(71, 187, 18))
print(cek_digit_belakang(1024, 14, 94))
print(cek_digit_belakang(53, 8900, 658))
print("\nLatihan4.3")

#Latihan 4.3
c1 = 100
c2 = 80
c3 = 0

celcius_ke_FahrenheitLambda = lambda c : (9/5) * c + 32
celcius_ke_ReamurLambda = lambda c : 0.8 * c
print(celcius_ke_FahrenheitLambda(c1))
print(celcius_ke_ReamurLambda(c2))
print(celcius_ke_FahrenheitLambda(c3))
