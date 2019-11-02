#-----------------------------------------------------------------
#Sayının asal olup olmadığını if-else yapısı ile kontrol etmek
#-----------------------------------------------------------------
x=25
asal=True #if'i kontrol edecek değişkeni tanımladık asal ise True değil ise False
for i in range(2,int(x/2)+1):# x/2 sonucu float döneceğinden int ile tip dönüşümü yapıldı
    if x%i==0:
        asal=False
        break
"""
    For döngüsü 2'den başlayarak x'in yarısından bir fazlasına kadar
    birer birer artacak ve her i için x'in bölünüp bölünemediğini 
    kontrol edecek. x'in tam bölündüğü sayı bulunursa asal değeri False
    olacak ve break ifadesi ile döngüden çıkılacak.
"""
if asal:#asal değeri True ise if bloğu False ise else bloğu çalışacak
    print("x bir asal sayıdır")
else:
    print("x bir asal sayı degildir")
#-----------------------------------------------------------------
#Sayının asal olup olmadığını for-else yapısı ile kontrol etmek
#-----------------------------------------------------------------
y=25
for j in range(2,int(x/2)+1):
    if y%i==0:
        print("y bir asal sayı değildir")
        break
else:
    print("y bir asal sayıdır")