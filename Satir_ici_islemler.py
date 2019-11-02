#Satır içi işlemler
str="Hayat Kısa Python Ögrenin"
x=[i for i in str if i.isupper()]#str içindeki harflerden büyük harf olanlar
"""
i.isupper() metodu i'nin büyük harf olup olmadığını kontrol eder 
ve bollean değer döndürür 
"""
print(x)
