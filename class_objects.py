class book():
    def __init__(self, ad, yazici, il, janr, sehife, qiymet, dil, stok):
        self.ad=ad
        self.yazici=yazici
        self.il=il
        self.janr=janr
        self.sehife=sehife
        self.fiyat = qiymet
        self.dil = dil
        self.stok= stok

    def stok_veziyyeti(self):
        if self.stok > 0:
            return f"{self.ad} kitabi stokda var."
        else:
            return f" {self.ad} kitabi stokda yoxdur."
        
       
biz=book("Biz", "Yevgeni Zamyatin", 1924, "Bilim-kurgu", 224, "9 Azn", "Rus", 3) 
utopia=book("Utopia", "Thomas More", 1516, "Fəlsəfə düşüncə", 249, "10 AZn", "Ingilis", 5)
kinyas_ve_kayra=book("Kinyas ve Kayra", "Hakan Gunday", 2000,"Roman", 567, "15 Azn", "Turk", 0)
oluler=book("Ölülər","Cəlil Məmmədquluzadə", 1909, " Tragikomediya", 96, "5 Azn", "Azerbaycan", 0) 

print(f"{biz.ad}  adli kitabin yazicisi {biz.yazici}dir ve kitab {biz.il}-cu tarixinde yazilmisdir. { biz.stok_veziyyeti()}")    
print(f"{utopia.ad}  adli kitabin yazicisi {utopia.yazici}dir ve kitab {utopia.il}-ci tarixinde yazilmisdir. { utopia.stok_veziyyeti()}")
print(f"{kinyas_ve_kayra.ad}  adli kitabin yazicisi {kinyas_ve_kayra.yazici}dir ve kitab {kinyas_ve_kayra.il}-ci tarixinde yazilmisdir. { kinyas_ve_kayra.stok_veziyyeti()}")
print(f"{oluler.ad}  adli kitabin yazicisi {oluler.yazici}dir ve kitab {oluler.il}-cu tarixinde yazilmisdir. {oluler.stok_veziyyeti()}")