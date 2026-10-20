# Praktik: Analisis Nilai Mahasiswa

def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    lulus = []

    for nilai in data:
        if nilai >= batas:
            lulus.append(nilai)

    return lulus


nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

jumlah_data = len(nilai)
total = sum(nilai)
rata = rata_rata(nilai)
minimum = min(nilai)
maksimum = max(nilai)

lulus = nilai_lulus(nilai)
jumlah_lulus = len(lulus)
jumlah_belum_lulus = jumlah_data - jumlah_lulus

print("=== ANALISIS NILAI MAHASISWA ===")
print(f"Data nilai       = {nilai}")
print(f"Banyak data      = {jumlah_data}")
print(f"Total nilai      = {total}")
print(f"Rata-rata        = {rata:.2f}")
print(f"Nilai minimum    = {minimum}")
print(f"Nilai maksimum   = {maksimum}")
print(f"Batas kelulusan  = 60")
print(f"Jumlah lulus     = {jumlah_lulus}")
print(f"Jumlah belum lulus = {jumlah_belum_lulus}")
print(f"Nilai yang lulus = {lulus}")