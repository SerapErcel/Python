class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):     #ELEMAN EKLEME METODU
        if(self.root == None):
            self.root = Node(val)   #KÖK BOŞ OLDUĞUNDA ELEMANI KÖKE(root) ATADIK
        else:
            self._add(val, self.root)   #KÖK BOŞ DEĞİLSE _add METODUNU ÇAĞIRIDIK

    def _add(self, val, node):
        if(val < node.v):   #ALINAN YENİ DEĞER(val) KÜÇÜK İSE (LEFT)SOL TARAFA EKLE
            if(node.l != None): #DÜĞÜMÜN SOLU BOŞ DEĞİLSE
                self._add(val, node.l)  #node.l için_add METODUNU YENİDEN ÇAĞIR
            else:   #DÜĞÜMÜN SOLU BOŞSA
                node.l = Node(val)  #DEĞERİ node.l(SOLA) ATA
        else:   #ALINAN YENİ DEĞER(val) BÜYÜK İSE (RİGHT)SAĞ TARAFA EKLE
            if(node.r != None): #DÜĞÜMÜN SAĞI BOŞ DEĞİLSE
                self._add(val, node.r)  #node.r için add METODUNU YENİDEN ÇAĞIR
            else:   #DÜĞÜMÜN SAĞI BOŞSA
                node.r = Node(val)  #DEĞERİ node.r(SAĞA) ATA

    def find(self, val):    #GİRİLEN val DEĞERİNİ BULAN METOD
        if(self.root != None):  #EĞER KÖK BOŞ DEĞİLSE
            return self._find(val, self.root)   #_find METODU ÇAĞIRILDI
        else:
            return None     #EĞER KÖK BOŞ İSE NONE DÖNDÜR

    def _find(self, val, node):
        if(val == node.v):  #ARANAN DEĞER DÜĞÜME EŞİTSE
            return node
        elif(val < node.v and node.l != None):#ARANAN DEĞER DÜĞÜMDEN KÜÇÜKSE VE DÜĞÜMÜN SOLU(küçüklerin bulunduğu taraf) BOŞ DEĞİLSE
            self._find(val, node.l) #DÜĞÜMÜN SOL TARAFI İÇİN _find METODU YENİDEN ÇAĞIRILDI
        elif(val > node.v and node.r != None):#ARANAN DEĞER DÜĞÜMDEN BÜYÜKSE VE DÜĞÜMÜN SAĞI(büyüklerin bulunduğu taraf) BOŞ DEĞİLSE
            self._find(val, node.r) #DÜĞÜMÜN SAĞ TARAFI İÇİN _find METODU YENDEN ÇAĞIRILDI

    def printTree(self):    #AĞACI YAZDIRACAK METOD
        if(self.root != None):  #KÖK(root) BOŞ DEĞİLSE
            self._printTree(self.root)  #KÖK(root)için _printTree METODU ÇAĞIRILDI

    def _printTree(self, node):
        if(node != None):   #node BOŞ DEĞİLSE
            self._printTree(node.l) #DÜĞÜMÜN SOLU İÇİN _printTree METODU YENİDEN ÇAĞIRILDI
            print (str(node.v) + ' ')   #node.v STRİNG İFADEYE DÖNDÜRÜLEREK YANINA BİR BOŞLUK İLE EKRANA YAZDIRILDI
            self._printTree(node.r) #DÜĞÜMÜN SAĞI İÇİN _printTree METODU YENİDEN ÇAĞIRILDI

#       3
#     /   \
#    0     4
#      \     \
#        2     8
tree = Tree() #YENİ AĞAÇ OLUŞTURULDU
tree.add(3) #AĞACA YENİ ELEMANLAR EKLENDİ
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree() #AĞAÇ EKRANA YAZILDI
print ("-----",(tree.find(3).v)) #AĞAÇTA 3 DEĞERİ ARANDI
print("-----",tree.find(10)) #AĞAÇTA 10 DEĞERİ ARANDI
