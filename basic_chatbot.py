import time
import datetime

colors = [
    "\033[91m",  # merah
    "\033[92m",  # hijau
    "\033[93m",  # kuning
    "\033[94m",  # biru
    "\033[95m",  # ungu
    "\033[96m",  # cyan
]
reset = "\033[0m"

text = "Selamat datang di ChatBot sederhana saya!"

# Efek mengetik dengan warna-warni
for i, char in enumerate(text):
    color = colors[i % len(colors)]
    print(color + char + reset, end="", flush=True)
    time.sleep(0.05)

print("\n")
time.sleep(1.5)

print("Kamu tahu hari ini tanggal berapa?")
time.sleep(2)

# Mengambil waktu saat ini
now = datetime.datetime.now()

# Ubah ke Bahasa Indonesia
hari_indo = {
    "Monday": "Senin", "Tuesday": "Selasa", "Wednesday": "Rabu",
    "Thursday": "Kamis", "Friday": "Jumat", "Saturday": "Sabtu", "Sunday": "Minggu"
}
bulan_indo = {
    "January": "Januari", "February": "Februari", "March": "Maret", "April": "April",
    "May": "Mei", "June": "Juni", "July": "Juli", "August": "Agustus",
    "September": "September", "October": "Oktober", "November": "November", "December": "Desember"
}

# Terjemahkan hari dan bulan dari format bahasa Inggris bawaan Python
hari = hari_indo[now.strftime("%A")]
bulan = bulan_indo[now.strftime("%B")]

# Cetak tanggal yang sudah diterjemahkan
print(f"Hari ini adalah {hari}, {now.strftime('%d')} {bulan} {now.strftime('%Y, %H:%M:%S')}")

time.sleep(2)

n = input("Siapa nama kamu? ")
print(n + " Nama yang bagus, ya!")
time.sleep(1.5)

k = input("Kamu kelas berapa? ")
cleaned_input = k.lower()
time.sleep(1.5)

# Pengecekan Kelas (Sudah Disesuaikan untuk Jenjang SMA)
if "10" in cleaned_input:
    print("Kelas 10? Selamat datang di SMA Citra Negara!")
elif "11" in cleaned_input:
    print("Wah, ternyata kamu kelas 11 ya...")
elif "12" in cleaned_input:
    print("Senior di SMA nih? Semangat mengejar kelulusan ya!")
else:
    print("Oh ternyata kamu bukan anak SMA, ya...")
    
time.sleep(1.5)

h = input("Hobby kamu apa? ")
print("Oh hobby kamu " + h + " ya?")
time.sleep(1.5)

m = input("Makanan favorit kamu apa? ")
print("Wow " + m + " itu enak juga menurutku!")
time.sleep(1.5)

i = input("Minuman kesukaanmu? ")
print("Sepertinya " + i + " itu enak juga...")
time.sleep(1.5)

print("\nBerarti nama kamu " + n + ".")
time.sleep(1.5)

print("Kamu kelas " + k + ".")
time.sleep(1.5)

print("Hobby kamu itu " + h + ".")
time.sleep(1.5)

print("Makanan favorit kamu itu " + m + ".")
time.sleep(1.5)

print("Minuman kesukaanmu itu " + i + ".")
time.sleep(1.5)
