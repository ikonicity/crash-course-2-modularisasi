#from geometri.segitiga import hitung_luas_segitiga
# geometri.segitiga import as gs
from geometri.segitiga import hitung_luas_segitiga, info as info_segitiga
from geometri.kotak import hitung_luas_kotak, info as info_kotak

print(info_segitiga())
print(f'hitung_luas_segitiga {hitung_luas_segitiga(99, 789)}')
print(info_kotak())
print(f'hitung_luas_kotak {hitung_luas_kotak(99, 789)}')