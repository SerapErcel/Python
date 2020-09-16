metin=input("Q klavye ile yazılmış metni giriniz: ")

q_klavye="qwertyuıopğüasdfghjklşi,zxcvbnmöç."
f_klavye="fgğıodrnhpqwuieaütkmlyşxjövcçzsb.,"

ceviri_tablosu=str.maketrans(q_klavye,f_klavye)

print(metin.translate(ceviri_tablosu))
