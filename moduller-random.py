# # random modülü tanımı : bizim için rastgele sayılar veya değerler üreten fonksiyonlar barındıran modüldür.

import random

for i in range(10):
    print(random.random())              # her çalştığında farklı farklı 0 ile 1 arası rastgele ondalıklı sayılar döndürür.

# uniform fonksiyonu : girilen 2 sınır arasında istenen değer kadar rastgele ondalıklı değerler döner.

for i in range(10):
    print(random.uniform(3,7))          # 3 ile 7 arasında rastgele ondalıklı sayılar döner.


# randint fonksiyonu : girilen 2 sınır arasında (sınırları dahil ederek) istenen kadar rastgele integer değerler döner.

for i in range(5):
    print(random.randint(3,5))          # 3 ile 5 (3 ile 5 dahil) arasında rastgele integer değerler döner.


# randrange fonksiyonu : 3 parametre alır, alt sınır , üst sınır , adım (üst sınır dahil olmaz ve adım parametresi boş bırakılabilir)

for i in range(5):
    print(random.randrange(1,9,2))      # 1 ile 6 sınırları arasında (üst sınır dahil değil)2 şer atlayarak integer değerler döner.

# listelerle kullanılabilecek fonksiyonlar

# choise fonksiyonu : liste üzerinde çalışır ve rastgele seçim döner.

liste = ["siyah","kırmızı","mavi","sarı","beyaz",3,4,5]

print(random.choice(liste))             # listeden rastgele eleman döner

# shuffle fonksiyonu : bu fonksiyon herhangi bir şey üretmez. listeyi karıştırır.

random.shuffle(liste)
print(liste)                            # / [4, 'kırmızı', 'mavi', 3, 'beyaz', 'siyah', 'sarı', 5]
print(liste)                            # / [3, 'mavi', 5, 'kırmızı', 'sarı', 4, 'siyah', 'beyaz']

# sample fonksiyonu : listeden girilen parametre kadar elemanlı mini listeler döndürür.

print(random.sample(liste,2))           # / [5, 'mavi']
print(random.sample(liste,5))           # / ['sarı', 3, 4, 'kırmızı', 'mavi']

# 1  - random fonksiyonu          :  
# 2  - betavariate fonksiyonu     : 
# 3  - choice  fonksiyonu         :  
# 4  - choices fonksiyonu         : 
# 5  - expovariate fonksiyonu     :  
# 6  - gammavariate fonksiyonu    :  
# 7  - gauss fonksiyonu           : 
# 8  - getrandbits fonksiyonu     : 
# 9  - getstate fonksiyonu        : 
# 10 - lognormvariate fonksiyonu  : 
# 11 - normalvariate fonksiyonu   : 
# 12 - paretovariate fonksiyonu   : 
# 13 - randbytes fonksiyonu       : 
# 14 - randint fonksiyonu         :  
# 15 - randrange fonksiyonu       : 
# 16 - sample fonksiyonu          : 
# 17 - seed fonksiyonu            : 
# 18 - setstate fonksiyonu        : 
# 19 - shuffle fonksiyonu         : 
# 20 - triangular fonksiyonu      : 
# 21 - uniform fonksiyonu         : 
# 22 - vonmisesvariate fonksiyonu :
# 23 - weibullvariate fonksiyonu  : 