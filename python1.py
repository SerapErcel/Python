#random modülü kullanarak çok boyutlu liste oluşturan program
import random #random (rastgele) modülü-kütüphanesi çağırıldı
x=[] #boş liste oluşturuldu
for i in range(5): #for döngüsü beş defa dönerek beş adet satır oluşturdu
    x.append([random.randint(1,5) for c in range(4)])
    """
    for c in range(4) dört defa random.randint metodunu çalıştırarak,
    1 ve 5 arasında rastgele sayı oluşturdu
    append metodu ekleme yaptı
    """
print(x) #x listesini ekrana yazdırdı