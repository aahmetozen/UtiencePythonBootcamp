"""internet bankacılığı projesi (öğrenme amaçlı basit uyg)"""
print("Python bank'a hoşgeldiniz")

users={"ahmet":"123"}
accounts={"ahmet":400.0}
ibans={"TR081234":"ahmet","TR039876":"ayse"}
activuser="None"

while True:
    answer = input("""yapmak istediğiniz işlemi seçin
    1.Üye Ol
    2.Giriş Yap
    3.Şubeden çık""")

    if answer == ["1", "2", "3"]:
        break
def singup():
    if welcomemenuanswer == "1":
        email = input("Email adresiniz:")
        password = input("parolanız:")
        users[email] = password
        accounts[email] =
        print("üyelik başarıyla tamamlandı")


def wolcomemenu():
    while True:
        answer = input("""yapmak istediğiniz işlemi seçin
        1.Üye Ol
        2.Giriş Yap""")

        if answer == ["1", "2"]:
            return answer
welcomemenuanswer = welcomemenu()


def login():
    email = input("email adrsiniz:")
    if email not in users:
        print("böyle bir kullanıcı bulunamadı")
        return [False,None]
    else:
        while True:
            password = input("parolanız:")
            parola = users[email]  # data basedeki parola
            if parola == password:
                print("giriş başarılı")
                return [True,email]
            else:
                print("parola yanlış")



def dısplaybankingmenu():
    bankmenuanswer = print("""BANKACILIK MENÜSÜ:
    1. hesap bakıyemi göster
    2.para çek
    3.para yatır
    4.para gönder
    5.parolamı değiştir
    6.çıkış yap""")

def accountbalance():
    balance = accounts[activuser]
    print(f"hesap bakiyeniz: {balance}")
    return balance

def parolachange():
    oldpassword=input("mevcut parolanızı girin:")
    if users[activuser] = oldpassword:
        while True:
            newpassword = input("yeni parolanızı girin:")
            newpasswordcheck = input("yeni parolanızı tekrar girin:")
            if newpassword = newpasswordcheck:
                users[activuser]
                print("parolanız başarılı şekilde değiştirildi")
                break
            else:
                print("paralolar eşleşmiyor!")
    else:
        print("mevcut parolanızı yanlış girdiniz")

def moneytransfer():
    iban=input("gindermek istediğniz ibanı girin:")
    if iban not in ibans:
        print("böyle bir iban bulunamadı")
    else:
        transferammount=int(input("göndermek istediğniz miktarı giriniz:"))
        while transferammount > balance:
            transferammount=input(" hesap bakiyeniz yetersiz. tekrar girin:")
        accounts[activuser]= accounts[activuser] - transferammount
        reciveruser=ibans[iban]
        accounts[reciveruser]= accounts[reciveruser] + transferammount

if welcomemenuanswer == "1":
    singup()

succes=login()
if succes:


if dısplaybankingmenuanswer == "1":
    accountbalance()

elif dısplaybankingmenuanswer == "2":
    balance=accountbalance()
    dramamount=int(input("Çekmek istedğiniz miktarı yazın:"))
    if dramamount > balance:
        print(f"bakiye yetersiz. bakiyeniz: {balance}")
    else:
        accounts[activuser] = accounts[activuser] - dramamount
        print(f"{dramamount} TL çekme işlemi tamamlandı.")

elif dısplaybankingmenuanswer == "3":
    balance=accountbalance()
    addamount=int(input("Yatırmak istedğiniz miktarı yazın:"))
    else:
        accounts[activuser] = accounts[activuser] + addamount
        print(f"{addamount} TL çekme işlemi tamamlandı.")

elif dısplaybankingmenuanswer == "4":
    moneytransfer

elif dısplaybankingmenuanswer == "5":
    parolachange()

elif dısplaybankingmenuanswer == "6":
    return False


while True:
    iscontiune=dısplaybankingmenu()
    if iscontiune == False:


