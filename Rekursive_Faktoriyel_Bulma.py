#Rekürsif ile faktoriyel alma
def faktoriyel(n): #n parametresini alan faktoriyel adlı metot tanımlandı
    return 1 if n==1 else n*faktoriyel(n-1)
#metot else kısmını çalıştırarak kendini çağırıyor ve n-1'i parametre gönderiyor 
print(faktoriyel(1))
