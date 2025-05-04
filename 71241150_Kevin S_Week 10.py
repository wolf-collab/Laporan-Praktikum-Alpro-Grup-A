print("Soal nomor 1")
with open("file1.txt", "r") as file1: #ini untuk membuka filenya
    with open("file2.txt", "r") as file2: #ini untuk membuka filenya
        files1 = [line.strip() for line in file1] #line.strip ini menghapus spasi/whitespace di awal/akhir baris
        files2 = [line.strip() for line in file2] #ini sama

baris = max(len(files1), len(files2)) #kalo ini agar semua baris ikut terbaca
for i in range(baris):
    baris1 = files1[i] if i < len(files1) else "Kalimat sama."
    baris2 = files2[i] if i < len(files2) else "Kalimat sama."
    if baris1 != baris2:
        print(f'Baris {i+1}:')
        print(f"File 1: {baris1}")
        print(f"File 2: {baris2}\n=======================\n")

print("Soal nomor 2")
def soal():
    print("nama file1: soal.txt")
    with open("soal.txt", "r") as file:
        for line in file:
            lineTemp = line.split("||", 1) #1 nya untuk memisah kan jadi cuma ada 2 parameter yakni 0 sebagai sebelum dan 1 sesudahnya
            pertanyaan = lineTemp[0].strip() #lineTemp.strip ini menghapus spasi/whitespace di awal/akhir baris
            jawaban_benar = lineTemp[1].strip().lower() #ini sama cuma ada tambahan .lower() agar hurufnya diubah jadi kecil semua incase of sensitive case nyeahh
            kujawab = input(f"{pertanyaan}\nJawab: ").strip().lower() #ini untuk masukkan jawaban sama juga fiturnya
            hasil = "Jawaban benar!" if kujawab == jawaban_benar else "Jawaban salah/tidak benar!" #ini if else yang disimpan didalam variabel
            #biasanya aku ga pernah pake tapi untuk kasus ini enaknya pake jadi tinggal panggil aja gitu ngga perlu panjang2 kodenya 
            print(f"""{hasil}
{'='*40}""") # ini optional biar jadi pemisah aja, biar rapi ga ruwet
soal()