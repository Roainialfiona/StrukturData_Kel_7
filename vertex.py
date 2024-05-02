class PetaJawaTimur:
    def _init_(self):
        self.cityList = {}
        self.totalEdge = 0
    
    def printPeta(self):
        for kota in self.cityList:
            print(kota, ":", self.cityList[kota])
        
    def tambahkanKota(self, kota):
        if kota not in self.cityList:
            self.cityList[kota] = []
            return True
        return False
    
    def hapusKota(self, kotaDihapus):
        if kotaDihapus in self.cityList:
            for kotalain in self.cityList:
                if kotaDihapus in self.cityList[kotalain]:
                    self.cityList[kotalain].remove(kotaDihapus)
                    self.totalEdge -= 1
            del self.cityList[kotaDihapus]
            return True
        return False
    
    def tambahkanJalan(self, kota1, kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            self.cityList[kota2].append(kota1)
            self.cityList[kota1].append(kota2)
            self.totalEdge += 1
            return True
        return False
    
    def hapusJalan(self, kota1, kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            self.cityList[kota2].remove(kota1)
            self.cityList[kota1].remove(kota2)
            self.totalEdge -= 1
            return True
        return False


petaJawaTimur = PetaJawaTimur()

# Daftar nama kota di Jawa Timur
kota_jawa_timur = ["Surabaya", "Malang", "Sidoarjo", "Probolinggo", "Pasuruan", 
                   "Kediri", "Jombang", "Madiun", "Blitar", "Lamongan",
                   "Batu", "Ponorogo", "Nganjuk", "Trenggalek", "Magetan", "Pacitan"]
# Ambil sejumlah acak antara 10 hingga 20 kota dari daftar kota
import random

jumlah_kota = random.randint(10, 20)
kota_terpilih = random.sample(kota_jawa_timur, jumlah_kota)

# Tambahkan kota-kota terpilih ke peta
for kota in kota_terpilih:
    petaJawaTimur.tambahkanKota(kota)

# Hubungkan setiap kota dengan jalan secara acak
while petaJawaTimur.totalEdge < 30:  # pastikan total edge adalah 30
    kota1, kota2 = random.sample(kota_terpilih, 2)
    if not (kota2 in petaJawaTimur.cityList[kota1] or kota1 in petaJawaTimur.cityList[kota2]):
        petaJawaTimur.tambahkanJalan(kota1, kota2)

# Tampilkan peta Jawa Timur
petaJawaTimur.printPeta()
print("Total edge:", petaJawaTimur.totalEdge)
