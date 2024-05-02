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
kota_jawa_timur = ["Surabaya", "Malang", "Sidoarjo", "Probolinggo", "Pasuruan", "Mojokerto",
                   "Kediri", "Jombang", "Madiun", "Blitar", "Lamongan", "Tulungagung",
                   "Batu", "Ponorogo", "Nganjuk", "Trenggalek", "Magetan", "Pacitan"]
