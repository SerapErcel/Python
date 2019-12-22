class Node:
    def __init__(self,data):
        self.item=data
        self.sonraki=None
class bagliListe:
    def __init__(self):
        self.start_node=None
    def listeyi_yaz(self):
        if self.start_node is None:
            print("listede eleman yok")
            return
        else:
            n=self.start_node
            while n is not None:
                print(n.item," ")
                n=n.sonraki
    def bastan_sil(self):
        if self.start_node is None:
            print("silinecek eleman yok")
            return
        self.start_node=self.start_node.sonraki
    def sona_ekle(self,data):
        new_node=Node(data)
        if self.start_node is None:
            self.start_node=new_node
            return
        n=self.start_node
    def eleman_say(self):
        if self.start_node is None:
            return 0
        n=self.start_node
        count=0
        while n is not None:
            count=count+1
            n=n.sonraki
        return count
    def eleman_bul(self,a):
        if self.start_node is None:
            print("listede eleman yok")
            return
        n=self.start_node
        while n is not None:
            if n.item==a:
                print("eleman bulundu")
                return True
            n=n.sonraki
        print("eleman bulunamadı")
        return False
yeni_liste=bagliListe()

yeni_liste.sona_ekle(5)
yeni_liste.sona_ekle(10)
yeni_liste.sona_ekle(15)

yeni_liste.listeyi_yaz()

yeni_liste.bastan_sil()

yeni_liste.sona_ekle(20)
yeni_liste.listeyi_yaz()

print(yeni_liste.eleman_say())
print(yeni_liste.eleman_bul(10))