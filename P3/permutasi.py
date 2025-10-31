import math

class Permutasi:

    def __init__(self, data):
        
        self.data = data
        self.n = len(data)

    # Tanpa Pengulangan 
    def tpAll(self):
        return self.__tpAll(self.data)
    

    def __tpAll(self, elemen):
        if len(elemen) == 1:
            return [elemen]
        
        hasil = []

        for i in range(len(elemen)):
            item = elemen[i]
            sisa = elemen[:i] + elemen[i+1:]

            for p in self.__tpAll(sisa):
                hasil.append([item] + p)
        
        return hasil
    
    def tpHalf(self, r):

        if r > self.n:
            raise ValueError("r melebihi n")
        
        return self.__tpHalf(self.data, r)

    def __tpHalf(self, elemen, r):
        if r == 1:
            return [[x] for x in elemen]
        
        hasil = []

        for i in range(len(elemen)):
            item = elemen[i]
            sisa = elemen[:i] + elemen[i+1:]

            for p in self.__tpHalf(sisa, r - 1):
                hasil.append([item] + p)

        return hasil
    
    # Dengan Pengulangan
    def dp(self, r):
        hasil = []
        self.__dp([], r, hasil)
        return hasil
    
    def __dp(self, susunan, r, hasil):
        if len(susunan) == r:
            hasil.append(susunan)
            return
        
        for elemen in self.data:
            self.__dp(susunan + [elemen], r, hasil)
    
    # Unsur Sama
    def us_hitung(self):
        n = len(self.data)
        terhitung = {}

        for x in self.data:
            terhitung[x] = terhitung.get(x, 0) + 1

        penyebut = 1
        for c in terhitung.values():
            penyebut *= math.factorial(c)
        
        return math.factorial(n)
    
    def us(self):

        hasil = []
        self.__us([], self.data, hasil)
        return hasil
    
    def __us(self, susunan, sisa, hasil):

        if not sisa:
            hasil.append(susunan)
            return
        
        digunakan = set()
        for i in range(len(sisa)):
            elemen = sisa[i]
            if elemen in digunakan:
                continue
            digunakan.add(elemen)

            sisa_baru = sisa[:i] + sisa[i+1:]
            self.__us(susunan + [elemen], sisa_baru, hasil)






    
if __name__ == "__main__":
    data = list("UNIKA")

    permutasi = Permutasi(data)

    output = permutasi.us()

    for i in output:
        print(i)

    print("Total: ", len(output))
    print("Teoritis: ", permutasi.us_hitung())