########################################################
### UTIENCE AKADEMİ PYTHON BOOTCAMP SERTİFİKA SINAVI ###
########################################################

# AÇIKLAMA:
# BU SINAV PYTHON İLE TEMEL PROGRAMLAMA YETENEKLERİNİZİ
# TEST ETMEK İÇİN HAZIRLANMIŞTIR. AŞAĞIDA ÇÖZMENİZ İÇİN
# 8 TANE SORU VERİLMİŞTİR. SORULARIN HEPSİNİ SADECE VE
# SADECE SİZE AYRILAN YERDE ÇÖZDÜĞÜNÜZE EMİN OLUN.
# KODUNUZU YAZARKEN GİRİNTİLERE (INDENTATION) DİKKAT
# EDİN. SİZE VERİLEN FONKSİYON, DEĞİŞKEN VB İSİMLERİN
# HİÇBİRİNİ DEĞİŞTİRMEYİN. KENDİ DEĞİŞKENLERİNİZİ
# TANIMLAYABİLİRSİNİZ, FAKAT FONKSİYONUN GİRDİ VE ÇIKTI
# PARAMETRELERİNE DİKKAT EDEREK DEĞİŞKENLERİ KULLANIN.


# SORU-1
# AŞAĞIDA a VE b INTEGER PARAMETRELERİ ALAN VE BUNLARIN
# ARASINDAKİ TÜM ÇİFT SAYILARI BİR LİSTE HALİNDE DÖNEN
# BİR FONKSİYON TASLAĞI TANIMLANMIŞTIR. FONKSİYONUN İÇİNİ,
# İSTENEN ÇIKTIYI DÖNECEK ŞEKİLDE YAZINIZ.

def cift_sayilar(a, b):
    sonuc = []

    ############# KODUNUZU BURANIN ALTINDAN BAŞLAYARAK YAZIN #############
    for i in range(a,b+1):
        if i%2==0:
            sonuc.append(i)

    #############      KODUNUZU BURAYA KADAR YAZIN          ##############

    return sonuc


# SORU-2
# AŞAĞIDA a POZİTİF INTEGER PARAMETRESİNİ ALAN VE 0'dan
# a'ya KADAR OLAN INTEGER'ları EKRANA YAZDIRAN BİR FONKSİYON
# TASLAĞI TANIMLANMIŞTIR. FONKSİYONUN İÇİNİ, İSTENEN İŞLEVİ
# YERİNE GETİRECEK ŞEKİLDE YAZINIZ.

def from_zero_to_a(a):

    ############# KODUNUZU BURANIN ALTINDAN BAŞLAYARAK YAZIN #############
    if a>0:
        for s in range(0,a+1):
            print(s)
    else:
        print("hatalı sayı girdiniz")
    #############      KODUNUZU BURAYA KADAR YAZIN          ##############


# SORU-3
# AŞAĞIDA list_1 ve list_2 İSİMLERİNDE LİSTE PARAMETRELERİ
# ALAN VE BU İKİ LİSTEYİ BİRLEŞTİREN, ANCAK TEKRAR EDEN
# ELEMANLARI SADECE BİR KEZ İÇEREN FONKSİYON TASLAĞI TANIMLANMIŞTIR.
# FONKSİYONUN İÇİNİ, İSTENEN İŞLEVİ YERİNE GETİRECEK ŞEKİLDE YAZINIZ.
# ÖRNEK: list_1 = ["a", "b", "c"] ve list_2 = ["x", "b", "b"] ise
# ÇIKTI: ["a", "b", "c", "x"] olmalıdır.

def combine_two_lists(list_1, list_2):
    sonuc = []

    ############# KODUNUZU BURANIN ALTINDAN BAŞLAYARAK YAZIN #############
    list3=[]
    list3=list_1+list_2
    sonuc=[]
    for item in list3:
        if item not in sonuc:
            sonuc.append(item)
    #############      KODUNUZU BURAYA KADAR YAZIN          ##############

    return sonuc


# SORU-4
# AŞAĞIDA numbers ADINDA BİR LİSTE PARAMETRESİ ALAN VE BU LİSTENİN
# İÇİNDEN SIRASIYLA EN BÜYÜK VE EN KÜÇÜK ELEMANLARI DÖNEN BİR
# FONKSİYON TASLAĞI TANIMLANMIŞTIR. FONKSİYONUN İÇİNİ, İSTENEN
# İŞLEVİ YERİNE GETİRECEK ŞEKİLDE YAZINIZ. BUILT-IN FONKSİYON KULLANMAYIN.
# ÖRNEK: numbers = [5, 3, 0, -2, 7, 11] ise
# ÇIKTI: (11, 2) olmalıdır.

def max_and_min(numbers):
    sonuc = None

    ############# KODUNUZU BURANIN ALTINDAN BAŞLAYARAK YAZIN #############
    minn = numbers[0]
    maxx = numbers[0]
    for i in numbers:
        if i < minn:
            minn = i
        if i > maxx:
            maxx = i
            sonuc="{},{}".format(maxx,minn)
    #############      KODUNUZU BURAYA KADAR YAZIN          ##############

    return sonuc


# SORU-5
# AŞAĞIDA n ADINDA BİR INTEGER PARAMETRESİ ALAN VE BU INTEGER'ın
# KARESİNİ EKRANA YAZDIRAN BİR FONKSİYON TASLAĞI TANIMLANMIŞTIR.
# FONKSİYONUN İÇİNİ, İSTENEN İŞLEVİ YERİNE GETİRECEK ŞEKİLDE YAZINIZ
def display_square(n):

    ############# KODUNUZU BURANIN ALTINDAN BAŞLAYARAK YAZIN #############
    sonuc=n**2
    print(sonuc)
    #############      KODUNUZU BURAYA KADAR YAZIN          ##############


# SORU-6
# AŞAĞIDAKİ FONKSİYON TASLAĞINDA KULLANICIDAN BİR username VE BİR
# password İSTEYİN. ALDIĞINIZ BU DEĞİŞKENLERİ, AŞAĞIDA VERİLEN
# users_db DICTIONARY'SİNDE KONTROL EDİN. EĞER KULLANICI ADI VE PAROLA
# EŞLEŞMESİNİ SAĞLAYAN BİR ANAHTAR-DEĞER ÇİFTİ VARSA FONKSİYONDAKİ
# login_success DEĞİŞKENİNİ True OLARAK, YOKSA False OLARAK DÖNDÜRÜN.
# FONKSİYON TASLAĞINI BU İŞLEVİ YERİNE GETİRECEK ŞEKİLDE YAZINIZ.

def login_function():
    users_db = {
        "admin":"abc123",
        "arif":"xyz.arif",
        "seymanur":"nur.abc"}

    login_success = None

    ############# KODUNUZU BURANIN ALTINDAN BAŞLAYARAK YAZIN #############
    username=input("kullanıcı adını girin:")
    password=input("şifre girin:")
    if users_db.keys()==username and users_db.values()==password:
        login_success=True
    else:
        login_success=False

    #############      KODUNUZU BURAYA KADAR YAZIN          ##############

    return login_success


# SORU-7
# AŞAĞIDA items ADINDA BİR LİSTE PARAMETRESİ ALAN VE BU LİSTENİN
# İÇİNDEKİ ELEMANLARIN SIKLIĞINI BİR DICTIONARY OLARAK DÖNEN BİR
# FONKSİYON TASLAĞI TANIMLANMIŞTIR. FONKSİYONUN İÇİNİ, İSTENEN
# İŞLEVİ YERİNE GETİRECEK ŞEKİLDE YAZINIZ.
# ÖRNEK: items = ["a", "a", "b", "b", "b", "c", "d", "e", "e"] ise
# ÇIKTI: {"a":2, "b":3, "c":1, "d":1, "e":2} olmalıdır.

def count_frequency(items):
    sonuc = {}

    ############# KODUNUZU BURANIN ALTINDAN BAŞLAYARAK YAZIN #############
    from collections import Counter

    my_list = [1, 2, 2, 3, 4, 4, 5]
    element_counts = Counter(my_list)

    for item, count in element_counts.items():
        if count > 1:
            print(f"Tekrar eden eleman: {item}, Sayısı: {count}")
    #############      KODUNUZU BURAYA KADAR YAZIN          ##############

    return sonuc


# SORU-8
# AŞAĞIDAKİ FONKSİYONDA KULLANICIDAN BİR İSİM ALIN. ARDINDAN
# BİR DOĞUM YILI ALIN. EĞER KULLANICI 18 YAŞINDAN BÜYÜK İSE
# (2023'TEN ÇIKARINCA 18 VE DAHA BÜYÜK BİR SAYI KALIYORSA) EKRANA
# "MERHABA kullanıcı_adi HOŞGELDİNİZ" YAZDIRIN. 18 YAŞINDAN KÜÇÜKSE
# EKRANA "ÜZGÜNÜM kullanici_adi GİRİŞ YAPAMAZSINIZ" YAZDIRIN.

def welcoming_function():

    ############# KODUNUZU BURANIN ALTINDAN BAŞLAYARAK YAZIN #############
    name=int(input("isminizi girin:"))
    bırthday=int(input("doğum yılınızı girin:"))
    yas=2023-bırthday
    if yas > 18:
        print("merhaba {} hoşgeldin".format(name))
    else:
        print("üzgünüm {} giriş yapamazsınız".format(name))
    #############      KODUNUZU BURAYA KADAR YAZIN          ##############