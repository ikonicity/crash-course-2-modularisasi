"""
program menghitung luas segitiga
luas segitiga = alas * tinggi / 2
"""

alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas={luas_segitiga}')

alas = 20
tinggi = 2
luas_segitiga = alas * tinggi / 2
print(f'\nsegitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas={luas_segitiga}')

print('\nMembuat fungsi hitung luas segitiga')
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

print(f'menghitung luas segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(10,6)}')
print(f'menghitung luas segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(20,2)}')
print(f'menghitung luas segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(200,29)}')

print('\nbisa juga begini')
alas = 8
tinggi =90
print(f'dengan fungsi, segitiga dengan alas={alas} dan tinggi={tinggi} hasilnya = {hitung_luas_segitiga(alas,tinggi)}')