import time
class çalışan():
    def __init__(self,isim,maaş,departman):
        self.isim=isim
        self.maaş=maaş
        self.departman=departman
    def bilgilerigoster(self):
        print("Çalışan bilgileri...")
        time.sleep(3)
        print("İsim:{} \nMaaş:{} \nDepartman:{}".format(self.isim,self.maaş,self.departman))
    def maasiartır(self,yenimaas):
        time.sleep(2)
        self.maaş=yenimaas
        print("Yeni maaşı: {}".format(self.maaş))
    def departmandegistir(self,yenidepartman):
        time.sleep(2)
        self.departman=yenidepartman
        print("Yeni departmanı: {} ".format(self.departman))
class elektrikelektronik(çalışan):
    def __init__(self,isim,maaş,departman,sorumluluk):
        super().__init__(isim,maaş,departman)
        self.sorumluluk = sorumluluk
    def bilgilerigoster(self):
        print("Çalışan bilgileri...")
        time.sleep(3)
        print("İsim:{} \nMaaş:{} \nDepartman:{} \nSorumlu Olduğu Kişi Sayısı: {}".format(self.isim, self.maaş, self.departman,self.sorumluluk))
emirhan=elektrikelektronik("Yılmaz Güney",9000,"ee",10)
emirhan.bilgilerigoster()
emirhan.maasiartır(10000)
emirhan.departmandegistir("pc")
