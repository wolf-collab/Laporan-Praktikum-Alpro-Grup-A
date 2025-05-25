print("\nSoal 1")
def cek_isi(tapel):
    if not tapel: #ini ngecek kalau isi tapel nya kosng maka hasilnya False
        return False
    return all(x == tapel[0] for x in tapel) 
#ini ngecek apakah semua elemen dalem tapel itu sama ngga sama elemen pertamanya (tapel[0])

tA =(90,90,90,90)
print(f'tA = {tA}')
print({cek_isi(tA)})
#atau
tB = input("Masukkan 4 angka dan pisahkan dengan koma! (contoh: 1,2,3,4)\n>>>")
tb_tuple = tuple(map(int, tB.split(',')))
print({cek_isi(tb_tuple)})

print("\nSoal 2")
data = ('Kevin Surya Saputra', '71241150', 'Ps. Legi, Surakarta')
nama = data[0]
nimtapel = tuple(data[1])
namadepan = dict()
namadepan = data[0]
namatapel = tuple(data[0])
pisah = tuple(nama.split())
acak_nama = pisah[::-1]
baliknama2 = nama[::-1]
print(f"NIM             : {data[1]}")
print(f"NAMA            : {data[0]}")
print(f"ALAMAT          : {data[2]}\n")
print(f"NIM             : {nimtapel}")
print(f"NAMA DEPAN      : {namatapel[0:5]}")
print(f"NAMA TERBALIK   : {acak_nama}")
print(f"NAMA TERBALIK   : {baliknama2}\n")

print("\nSoal 3")
ini = input("Enter a file name (cth: mbox-short.txt): ")
hitung = dict()
try:
    with open(ini, 'r') as fhand:
        for baris in fhand:
            if baris.startswith("From "):
                cere = baris.split()
                waktu = cere[5]
                jam = waktu.split(':')[0]
                hitung[jam] = hitung.get(jam, 0) + 1
except FileNotFoundError:
    print(f"File {ini} tidak ada / tidak dapat dibuka.")
else:
    for jam in sorted(hitung):
        print(f"{jam} {hitung[jam]}")