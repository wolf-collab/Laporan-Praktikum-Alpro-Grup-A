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
import re
def hitung_pesan(nama):
    try:
        with open(nama_file, 'r') as file:
            domain_counts = {}
        for line in file:
            match = re.search(r"From (\S+@\S+)", line) #mencari pola email
            if match:
                email = match.group(1)
                domain = email.split('@')[1] #mengambil domain
                domain_counts[domain] = domain_counts.get(domain, 0) + 1
        return domain_counts
    except FileNotFoundError:
        return None
nama_file = "mbox-short.txt"
hasil = hitung_pesan(nama_file)
if hasil:
    print(hasil)
else:
    print(f"Error, {nama_file} tidak ditemukan.")