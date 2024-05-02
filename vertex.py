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
