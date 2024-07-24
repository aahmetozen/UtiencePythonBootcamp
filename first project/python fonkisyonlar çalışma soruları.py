# Soru 1: Bir sayının karesini döndüren bir fonksiyon yazın.
"""def kareal():
    sayi=int(input("sayı girin:"))
    kare=sayi**2
    return kare
k=kareal()
print(k)"""
# Soru 2: Bir sayının faktoriyelini hesaplayan bir fonksiyon oluşturun
"""def fakt():
    sayi=int(input("bir sayı girin:"))
    f=1
    while sayi>1:
        f=f*sayi
        sayi=sayi-1
    return f
a=fakt()
print(a)"""
# Soru 3: Bir sayının asal olup olmadığını kontrol eden bir fonksiyon yazın
"""def asalmi():
    a=int(input("bir sayı girin"))
    for i in range(2,a):
        if a % i == 0:
            return ("{} sayısı asal değil".format(a))
            break
        else:
            return ("{} sayısı asal sayı".format(a))
b=asalmi()
print(b)"""
# Soru 4: İlk n Fibonacci sayısını bir liste olarak döndüren bir fonksiyon yazın.

# Soru 5: Bir metinde belirli bir kelimenin kaç kez geçtiğini sayan bir fonksiyon oluşturun.
"""def ksay():
    t=0
    metin="noluyolan"
    aranan="l"
    for h in metin:
        if h==aranan:
            t+=1
    return ("{} kez geçti".format(t))

a=ksay()
print(a)"""
# Soru 6: Bir kelimenin palindrom olup olmadığını kontrol eden bir fonksiyon yazın. (Palindrom nedir
# araştırın)

# Soru 7: Bir liste içindeki en büyük sayıyı bulan bir fonksiyon yazın.
"""def buyukbul():
    l=[5,6,12,4,9,8,11,2]
    maxx=l[0]
    for i in l:
        if i>maxx:
            maxx=i
    return (maxx)

f=buyukbul()
print(f)"""
# Soru 8: Bir dictionary'e anahtar-değer çifti ekleyen bir fonksiyon oluşturun.

# Soru 9: Bir cümledeki ünlü harf sayısını döndüren bir fonksiyon yazın.

# Soru 10: Bir liste içerisindeki sayıların ortalamasını hesaplayan bir fonksiyon oluşturun.







"""t=0
for i in range(5,101):
    t=t+i
    print(t)"""
"""y=4
t=0
while y<=99:
    y+=1
    t=t+y
    print(t)"""


