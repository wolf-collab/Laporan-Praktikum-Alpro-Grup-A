print("Soal Nomor 1")
import random
def anagram(teks):
    teks = teks.lower() #untuk membuat semua huruf menjadi kecil
    kata = list(teks) #untuk mengubah tipe data teks menjadi list
    random.shuffle(kata) #untuk mengacak urutannya
    return ''.join(kata) #untuk mengembalikan hasil random
teks = input("Masukkan teks yang mau dicek:\n>>> ")
hasil = anagram(teks)
print(f"Anagram dari {teks} ==> {hasil}.\n")

print("Soal nomor 2")
import re
kalimat = "Saya mau makan. Makan itu wajib. Mau siang atau malam saya wajib makan."
kalimat = kalimat.lower() #untuk membuat semua huruf menjadi kecil
jawab = kalimat.split(" ") #untuk memelah string menjadi substring dengan jarak/spasi
x = re.findall("makan", kalimat) #ini untuk mencari kata "makan" dalam kalimat yang telah di split
for i in x: #perulangan i yang menyimpan data x
    print(i) #mencetak nilai i
hasil = len(x) #ini untuk menghitung banyaknya x dan disimpan di hasil
print(f"Makan ada: {hasil} buah.\n")

print("Soal nomor 3")
def hapus_spasi(jamak):
    return " ".join(jamak.split())
contoh = "saya tidak suka memancing ikan   Bun hidup berjalan seperti      gorengan"
hasil = hapus_spasi(contoh)
print(f"{hasil}\n")

print("Soal nomor 4")
def kalimat_panjang_pendek(kalimat):
    kata = teks.lower()
    kata = teks.split()
    
    terpendek = kata[0]
    terpanjang = kata[0]
    for i in kata:
        if len(i) < len(terpendek):
            terpendek = i
        if len(i) > len(terpanjang):
            terpanjang = i
    return terpendek, terpanjang

teks = input("Masukkan teks yang mau dicek\n>>> ")
terpendek, terpanjang = kalimat_panjang_pendek(kalimat)
print(f"\nterpendek: {terpendek}, terpanjang: {terpanjang}\n")

print("Soal nomor 5")
import re
from datetime import datetime, date
def tanggal_waktu(hasil):
    tanggal_list = re.findall(r'\d{4}-\d{2}-\d{2}', teks)
    hariini = date.today()
    
    for hari_str in tanggal_list:
        try:
            tanggal = datetime.strptime(hari_str, "%Y-%m-%d").date()
            tanggal_baru = tanggal.strftime("%d-%m-%Y")
            selisih = (hariini - tanggal).days
            print(f"{hari_str} 00:00:00 selisih {selisih} hari")
        except ValueError:
            print(f"Format tanggal '{hari_str}' tidak valid.")

teks = ("Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02).")
tanggal_waktu(hasil) #maaf ini bergelut dengan waktu T_T🥲😭

print("\nSoal nomor 6")
import re
import random
import string

def generate_password(length=8):
    """Generates a random password of specified length."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def username(teks):
    """Finds emails, extracts usernames, and generates passwords."""
    for email_string in teks: #Iterasi melalui setiap string dalam tuple
        email_list = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email_string)
        for email in email_list:
            username = email.split('@')[0]
            password = generate_password()
            print(f"{email} username: {username} , password: {password}")

teks = ("anton@mail.com", "budi@gmail.co.id", "mamakmia@yahoo.com", "slamet@bernadya.com", "gala@yutub.co.id", "bunga@floristjasmine.com", "matahari@tokopedia.com")
username(teks)