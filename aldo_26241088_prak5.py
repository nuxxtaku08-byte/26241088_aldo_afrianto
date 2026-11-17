# Nama: Aldo Afrianto
# Mata Kuliah: Pemrograman Dasar
# Tugas: Operator Komparasi dan Boolean

# Meminta input data mahasiswa
nama = input("Nama mahasiswa : ")
nim = input("NIM lengkap    : ")

# Meminta input dua digit terakhir NIM
digit_a = int(input("Digit A        : "))
digit_b = int(input("Digit B        : "))

print("\n===== DATA MAHASISWA =====")
print("Nama mahasiswa :", nama)
print("NIM lengkap    :", nim)
print("Digit A        :", digit_a)
print("Digit B        :", digit_b)

print("\n===== HASIL PERBANDINGAN =====")

print("A > B  :", digit_a > digit_b)
print("A < B  :", digit_a < digit_b)
print("A == B :", digit_a == digit_b)
print("A != B :", digit_a != digit_b)
print("A >= B :", digit_a >= digit_b)
print("A <= B :", digit_a <= digit_b)