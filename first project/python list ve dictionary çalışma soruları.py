# Soru 1: Verilen bir liste içindeki tüm sayıların toplamını hesaplayın. (Liste metodlarını kullanmadan)
"""l=[2,5,6,8]
t=0
for s in l:
    t=s+t
print(t)"""
# Soru 2: Tek ve çift sayılar içeren bir liste içindeki tek sayıları bir başka listeye kaydedin
"""list=[1,2,3,4,5,6,7,8,9]
tekl=[]
for s in list:
    if s % 2 == 1:
        tekl.append(s)
        print(tekl)"""
# Soru 3: Bir liste içerisinde en büyük ve en küçük elemanı bulun. (Liste metodlarını kullanmadan)
"""l=[5,2,9,7,1]
minn=l[0]
maxx=l[0]
for i in l:
    if i<minn:
        minn=i
    if i>maxx:
        maxx=i
print("{} en büyük elaman".format(maxx))
print("{} en küçük elaman".format(minn))"""
# Soru 4: Bir1 listeyi artan ya da azalan şekilde sıralayın. (Liste metodlarını kullanmadan)
"""def azalanl(list):
    list = [5, 3, 8, 6, 7, 2]
    for i in range(len(list) - 1):
        for j in range(len(list) - 1):
            if list[j] < list[j + 1]:
                t = list[j]
                list[j] = list[j + 1]
                list[j + 1] = t
    return("azalan şekilde sıralanmış liste: {}".format(list))

def artanl(list):
    list = [5, 3, 8, 6, 7, 2]
    for i in range(len(list) - 1):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                t = list[j]
                list[j] = list[j + 1]
                list[j + 1] = t
    return("artan şekilde sıralanmış liste: {}".format(list))

a=azalanl(list)
b=artanl(list)
print(a)
print(b)"""
# Soru 5: İki farklı listeyi birleştirin. (Liste metodlarını kullanmadan)
"""l1=[4,5,7]
l2=[2,8,4]
l3=[]
l3=l1+l2
print(l3)"""
# Soru 6: Bir dictionary içerisinde belirli bir anahtarın olup olmadığını kontrol edin.
"""my = {'name': 'Ali', 'age': 30, 'email':'ali@gmail.com'}
print(my.keys())"""
# Soru 7: Bir dictionary içerisindeki tüm anahtarları ve değerleri ekrana yazdırın.
"""my = {'name': 'Ali', 'age': 30, 'email':'ali@gmail.com'}
print(my.values())
print(my.keys())"""
# Soru 8: Belirli bir anahtarın değerini değiştirin
"""my = {'name': 'Ali', 'age': 30, 'email':'ali@gmail.com'}
my.update({'name': 'ahmet'})
print(my)"""
# Soru 9: Belirli bir değere sahip anahtar-değer çiftini dictionary'den silin
"""my = {'name': 'ahmet', 'age': 30, 'email':'ali@gmail.com'}
del my['email']
print(my)"""
# Soru 10: Bir dictionary içerisindeki en yüksek değere sahip anahtar-değer çiftini bulun

"""def bubble_sort(list1):
    for i in range(len(list1) - 1):
        for j in range(len(list1) - 1):
            if (list1[j] < list1[j + 1]):
                temp = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = temp
    return list1


list1 = [5, 3, 8, 6, 7, 2]
print("The unsorted list is: ", list1)
print("The sorted list is: ", bubble_sort(list1))"""