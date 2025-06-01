print("Soal no.1\n")
n = int(input("Masukkan jumlah kategori: "))
data_aplikasi = {}
for i in range(n):
    nama_kategori = input('Masukkan nama kategori: ')
    print('\nMasukkan 5 nama aplikasi di kategori', nama_kategori)
    aplikasi = []
    for j in range(5):
        nama_aplikasi = input('Nama aplikasi: ')
        aplikasi.append(nama_aplikasi)
    data_aplikasi[nama_kategori] = aplikasi
print(data_aplikasi)
daftar_aplikasi_list = []
for aplikasi in data_aplikasi.values():
    daftar_aplikasi_list.append(set(aplikasi))
print(daftar_aplikasi_list)
hasil = daftar_aplikasi_list[0]
for i in range(1, len(daftar_aplikasi_list)):
    hasil = hasil.intersection(daftar_aplikasi_list[i])
print("\nAplikasi yang muncul di semua kategori:", hasil)
hitung_aplikasi = {}
for kategori_aplikasi in daftar_aplikasi_list:
    for aplikasi in kategori_aplikasi:
        hitung_aplikasi[aplikasi] = hitung_aplikasi.get(aplikasi, 0) + 1
aplikasi_satu_kategori = set()
for aplikasi, jumlah in hitung_aplikasi.items():
    if jumlah == 1:
        aplikasi_satu_kategori.add(aplikasi)
print("\nAplikasi yang hanya muncul di satu kategori:", aplikasi_satu_kategori)
if n > 2:
    aplikasi_dua_kategori = set()
    for aplikasi, jumlah in hitung_aplikasi.items():
        if jumlah == 2:
            aplikasi_dua_kategori.add(aplikasi)
    print("\nAplikasi yang muncul tepat di dua kategori:", aplikasi_dua_kategori)
    
print("\nSoal no. 2\n")
def ubah_data():
    try:
        # Input list
        list_angka = input("Masukkan angka untuk list (pisahkan dengan koma): ")
        list_angka = list_angka.split(",")  
        list_angka = [int(x) for x in list_angka] 

        print("\nList awal:", list_angka)
        set_angka = set(list_angka)  #ngubah ke set
        print("Set setelah diubah:", set_angka)
        list_angka2 = list(set_angka)  # set jadi list
        print("List setelah diubah:", list_angka2)

        tuple_angka = input("\nMasukkan angka untuk tuple (pisahkan dengan koma): ")
        tuple_angka = tuple_angka.split(",") 
        tuple_angka = tuple(int(x) for x in tuple_angka) #tuple ke integer

        print("\nTuple awal:", tuple_angka)
        set_angka2 = set(tuple_angka)  # Ubah ke set
        print("Set setelah diubah:", set_angka2)
        tuple_angka2 = tuple(set_angka2)  # Ubah ke tuple
        print("Tuple setelah diubah:", tuple_angka2)

    except ValueError:
        print("\nError: Masukkan angka saja, dipisahkan koma.")
ubah_data()


print("\nSoal no. 3\n")
def bukafile(file1, file2):
    try:
        kata_sama = set()  #ini bikin set baru buat taruh kata yang sama di kedua file
        with open(file1, "r") as f1, open(file2, "r") as f2:
            kata_file1 = set()
            kata_file2 = set()
            
            for baris in f1:
                kata = baris.lower().split()
                for i in kata:
                    kata_file1.add(i)

            for baris in f2:
                kata = baris.lower().split()
                for i in kata:
                    kata_file2.add(i)

            kata_sama = kata_file1.intersection(kata_file2) # Menghitung irisan di dalam blok with

        print("Kata-kata yang sama di kedua file:\n", kata_sama)

    except FileNotFoundError:
        print("Error: File tidak ditemukan!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


file1_nama = input("Masukkan nama file pertama: ")
file2_nama = input("Masukkan nama file kedua: ")

bukafile(file1_nama, file2_nama)