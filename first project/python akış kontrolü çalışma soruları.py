# Soru 1: Kullanıcıdan alınan bir sayının tek mi çift mi olduğunu kontrol edin
"""sayi=int(input("bir sayı girin"))
if sayi % 2 == 0:
    print("çift sayı")
else:
    print("tek sayı")"""

# Soru 2: Kullanıcıdan alınan 0-100 arası bir puan için, 5'lik not sistemine göre bir harf notu döndürün.
"""puan=int(input("puanı girin:"))
if puan >=85 and puan <= 100:
    print( "{} beşlik sistemde karşılığı 5".format(puan))
elif puan >=70 and puan <=84:
    print("{} beşlik sistemde karşılığı 4".format(puan))
elif puan >=60 and puan <=69:
    print("{} beşlik sistemde karşılığı 3".format(puan))
elif puan >=50 and puan <=59:
    print("{} beşlik sistemde karşılığı 2".format(puan))
elif puan >=0 and puan <=49:
    print("{} beşlik sistemde karşılığı 1".format(puan))
else:
    print("hatalı ifade")"""

# Soru 3: Kullanıcıdan alınan iki sayıdan hangisinin daha büyük olduğunu ekrana yazdırın.
"""a=int(input("birinci sayıyı girin:"))
b=int(input("ikinci sayıyı girin:"))
if a>b:
    print("{} sayısı daha büyük".format(a))
else:
    print("{} sayısı daha büyük".format(b))"""

# Soru 4: Kullanıcıdan alınan bir sayının pozitif, negatif ya da sıfır olduğunu kontrol edin
"""sayi=int(input("bir sayı girin:"))
if sayi > 0:
    print("{} sayısı pozitif sayı".format(sayi))
elif sayi < 0:
    print("{} sayısı negatif sayı".format(sayi))
else:
    print("sayı sıfır")"""

# Soru 5: Kullanıcıdan alınan üç kenar uzunluğu ile bir üçgenin eşkenar, ikizkenar ya da çeşitkenar
# olduğunu belirtin.
"""a=int(input("birinci kenarı girin:"))
b=int(input("ikinci kenarı girin:"))
c=int(input("üçüncü kenarı girin:"))
if a==b==c :
    print("eşkenar üçgen")
elif a==b or b==c or a==c:
    print("ikizkenar üçgen")
else:
    print("çeşitkenar üçgen")"""

# Soru 6: Kullanıcıdan alınan bir ayın (1-12 arası bir sayı) hangi mevsime ait olduğunu belirleyin.
"""mevsim=int(input("1-12 arası bir sayı girin(1 ve 12 dahil):"))
if mevsim >=0 and mevsim<=3:
    print("ilkbahar mevsimi")
elif mevsim >=4 and mevsim<=6:
    print("yaz mevsimi")
elif mevsim >=7 and mevsim<=9:
    print("sonbahar mevsimi")
else:
    print("kış mevsimi")"""

# Soru 7: Bir ürünün fiyatı 500 TL’yi geçtiğinde 10%, 1000 TL’yi geçtiğinde 20% indirim yapılıyor. Toplam
# ürün fiyatı verildiğinde, indirimli fiyatını hesaplayın.
"""fiyat=int(input("fiyat girin:"))
if fiyat > 500:
    a=fiyat*10//100
    c=fiyat - a
    print("{} dan uygulanan indirim {} ürün fiyatı {} ".format(fiyat,a,c))
elif fiyat > 1000:
    b=fiyat*20//100
    d=fiyat - b
    print("{} dan uygulanan indirim {} ürün fiyatı {} ".format(fiyat,b,d))"""

# Soru 8: Kullanıcının girdiği şifrenin en az 8 karakter, bir büyük harf ve bir rakam içerip içermediğini
# kontrol edin.
"""ka=("Ablu2")
sayılars=("0,1,2,3,4,5,6,7,8,9")
büyükh=("A,E,R,T,Y,U,I,O,P,Ğ,Ü,S,D,F,G,H,J,K,L,Ş,İ,Z,C,V,B,N,M,Ö,Ç")
if len(ka)>=8:
    for i in ka:
        if i in sayılars:
            print("ifade sayı içeriyor:{}".format(i))
        elif i in büyükh:
            print("ifade büyük harf içeriyor:{}".format(i))
else:
    print("en az sekiz karakter içermeli!")"""

# Soru 9: Kullanıcıdan alınan 1-7 arası bir sayıya karşılık gelen haftanın gününü yazdırın.
"""a=int(input("1-7 arası bir sayı girin:"))
if a==1:
    print("pazartesi")
elif a==2:
    print("salı")
elif a==3:
    print("çarşamba")
elif a==4:
    print("perşembe")
elif a==5:
    print("cuma")
elif a==6:
    print("cumartesi")
elif a==7:
    print("pazar")
else:
    print("yanlış ifade girdiniz")"""

# Soru 10: Kullanıcıdan alınan üç farklı sayıyı karşılaştırın ve en büyüğünü ekrana yazdırın
"""a=int(input("birinci sayı:"))
b=int(input("ikinci sayı:"))
c=int(input("üçüncü sayı:"))
d=[]
d.append(a)
d.append(b)
d.append(c)
d.sort()
küçüksayi=d[0]
ortasayi=d[1]
büyüksayi=d[2]
if küçüksayi == ortasayi == büyüksayi:
    print("bütün sayılar eşit ve {}".format(büyüksayi))
else:
    print("küçük sayı: {} , orta sayı {} , büyük sayı {}".format(küçüksayi,ortasayi,büyüksayi))"""






