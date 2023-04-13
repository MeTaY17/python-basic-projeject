#modülleri içe aktarma
import secrets
import string


letters = string.ascii_letters # nüyük ve küçük harfler
digits = string.digits # 0-9 rakamlar
special_chars = string.punctuation # özel karakterler

alphabet = letters + digits +special_chars # alfabeyi oluşturma

#parola uzunluğu
pwd_length = 8

#sifre dizesi oluşturma
pwd = ""
for i in range(pwd_length):
    pwd+= "".join(secrets.choice(alphabet))

print(pwd)


#şifre için kısıtlama içeren kod parçacığı
while True:
    pwd = ""
    for i in range(pwd_length):
        pwd+= "".join(secrets.choice(alphabet))

    if (any(char in special_chars for char in pwd) and sum(char in digits for char in pwd)>=2):
        break

print(pwd)    