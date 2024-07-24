# Soru 1: 1'den 100'e kadar olan sayıların toplamını hesaplayın
"""toplam=0
for i in range(0,101,1):
    toplam=toplam+i
    print(toplam)"""
# Soru 2: Kullanıcıdan alınan bir sayının faktoriyelini hesaplayın
"""a=int(input("bir sayı girin"))
c=1
for i in range(1,a+1):
    c=c*i
    print(c)"""
# Soru 3: Verilen bir liste içerisindeki elemanları ekrana yazdırın.
"""liste=["a","b",3,1,"ablum","!"]
for i in liste:
    print(i)"""
# Soru 4: 5'in çarpım tablosunu ekrana yazdırın.
"""a=0
print("50.terime kadar 5in kuvvetleri")
for i in range(0,51):
    a=i*5
    print(a)"""
# Soru 5: Kullanıcıdan alınan bir sayının asal olup olmadığını kontrol edin.
"""a=int(input("bir sayı girin"))
for i in range(2,a):
    if a % i == 0:
        print("{} sayısı asal değil".format(a))
        break
    else:
        print("{} sayısı asal sayı".format(a))"""
# Soru 6: İlk 10 Fibonacci sayısını ekrana yazdırın.

# Soru 7: Verilen bir string içerisindeki belirli bir harfin kaç kez geçtiğini hesaplayın.
"""m=input("metin girin:")
a="a"
d=0
c=0
t=len(m)
while d != t:
    for h in m:
        d+=1
        if a == h:
            c += 1
    if a != h:
        print("harf kelimede geçmiyor")

    print("{} harfi {} kez tekrarlandı".format(a, c))"""
# Soru 8: 1 ile 10 arasında rastgele seçilen bir sayıyı kullanıcıya tahmin ettirin
"""import random
tahmin=int(input("sayı girin:"))
sayilist=[1,2,3,4,5,6,7,8,9]
a=random.choice(sayilist)
print("sayı {} tahmininiz {}".format(a,tahmin))"""
# Soru 9: Verilen bir liste içerisindeki en küçük ve en büyük sayıyı bulun.
"""l=[30,1,5,96]
l.sort()
kucuk=l[0]
buyuk=l[-1]
print("sıralanmış liste:",l)
print("en küçük sayı:{} en büyük sayı:{}".format(kucuk,buyuk))"""
# Soru 10: Yıldızlar kullanarak ters bir üçgen şekli çizin. Örn:
"""c=4
while c>0:
    print("*"*c)
    c=c-1"""

"""
append kullanmadan eleman ekleme
l=[1,2,3,4]

item=0
l[len(l):]=[item]
print(l)"""
