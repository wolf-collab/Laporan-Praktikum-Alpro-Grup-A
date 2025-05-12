print("Soal 1")
def tigabesar(data):
    if len(data) < 3:
        raise ValueError("List harus memiliki minimal 3 elemen.")
    return sorted(data, reverse=True)[:3]
angka = input("Masukkan angka yang mau di cek, pisahkan dengan koma!\n>>> ")
list_angka =[]
for x in angka.split(','):
    try:
        angka =int(x.strip())
        list_angka.append(angka)
    except ValueError:
        print("Input tidak valid.")
hasil = tigabesar(list_angka)
print("3 angka terbesar\n>>> ", hasil)

print("\nSoal 2")
def rata2(data):
    if len(data) < 2:
        raise ValueError("List harus memiliki minimal 2 elemen.")
print("Menghitung rata-rata Bilangan.\nKetik 'done' untuk mengakhiri input yaa.\nMinimal input 2 angka yeah! Kalau ngga heem majukk")
angka = []
while True:
    user = input("Masukkan angka: ")
    if user.lower() == 'done':
        break
    try:
        ubah = float(user)
        angka.append(ubah)
    except ValueError:
        print("Error! Masukkan hanya angka atau done!\n")

if len(angka) > 0:
    hitung = sum(angka) / len(angka)
    print(f"\nHasil perhitungan:")
    print(f"Banyak angka    = {len(angka)}")
    print(f"Total nilai     = {sum(angka)}")
    print(f"Rata-rata       = {hitung:.2f}")
else:
    print("\nTidak ada/Kurang bilangan yang dimasukkan!")

print("\nSoal 3")
buka_file = input("Masukkan nama file yang mau dibuka (contoh: Mega Korupsi 271T.txt):\n>>> ")
try:
    with open(buka_file, 'r') as file:
        teks = file.read()
    pisah_kata = teks.split()
    
    kata_unik = []
    for kata in pisah_kata:
        kata = kata.lower()
        if kata not in kata_unik:
            kata_unik.append(kata)
    kata_unik.sort()
    print("\nKata unik:\n>>> ")
    for i, kata in enumerate(kata_unik, 1):
        print(f"{i}. {kata}")
except FileNotFoundError:
    print("File tidak ada! Cek nama dan lokasi file apakah sudah benar. ")
except:
    print("Telah terjadi Error saat membaca file.")