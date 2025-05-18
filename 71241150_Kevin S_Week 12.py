print("Soal 1\n")
data = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("key\tvalue\titem")
for key, value in data.items():
    print(f"{key}\t{value}\t{key}")

print("\nSoal 2\n")
lista = ['red', 'green', 'blue']
listb = ['#FF0000', '#008000', '#0000FF']
hasil = dict(zip(lista, listb)) #pakai zip untuk menggabungkan elemen dari kedua atau lebih list. Ini juga membuat dictionary baru dan ditaruh situ isinya.
print(hasil)

print("\nSoal 3\n")
filename = "mbox-short.txt"
hitung = {}
try:
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith("From "):
                kata = line.split()
                email = kata[1]
                hitung[email] = hitung.get(email, 0) + 1   
    print(hitung)
except FileNotFoundError:
    print(f"File {filename} tidak ditemukan.")
except Exception as e:
    print(f"Telah Terjadi Kesalahan: {e}")

print("\nSoal 4\n")
def hitung_pesan(nama_file):
    try:
        hitung = {}
        with open(nama_file, 'r') as file:
            for baris in file:
                if baris.startswith("From "): #mencari pola email yang ada from nya
                    kata = baris.split()
                    if len(kata) >=2:
                        email = kata[1]
                        if '@' in email:
                            domain = email.split('@')[1]
                            hitung[domain] = hitung.get(domain, 0) + 1
        return hitung
    except FileNotFoundError:
        return None
nama_file = "mbox-short.txt"
hasil = hitung_pesan(nama_file)
if hasil:
    print(hasil)
else:
    print(f"Error, {nama_file} tidak ditemukan.")
