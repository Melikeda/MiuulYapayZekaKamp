#####################################
# Python Temelleri - Ödev Scripti
#####################################

#####################################################################################################################################################################

# Soru 1:
# Bir integer, bir float ve bir complex sayı tanımlayın.
# Bu sayıların türlerini yazdırın ve aralarında 1-2 işlem yapın.

# Sayıları tanımlayalım
a = 5           # integer
b = 3.2         # float
c = 2 + 3j      # complex

# Türlerini yazdıralım
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'complex'>

# İşlemler
toplam = a + b          # integer + float -> float
carpim = b * c          # float * complex -> complex

print("Toplam (a + b):", toplam)
print("Çarpım (b * c):", carpim)

#####################################################################################################################################################################

# Soru 2:
# İsminizi içeren bir string değişkeni oluşturun.
# Bu stringin ilk ve son karakterini yazdırın. Ayrıca tüm harfleri büyük yaparak ekrana yazdırın.

# İsminizi içeren string
isim = "Melike"

# İlk karakter
ilk_karakter = isim[0]

# Son karakter
son_karakter = isim[-1]

# Tüm harfleri büyük yapma
buyuk_isim = isim.upper()

print("İsim:", isim)
print("İlk karakter:", ilk_karakter)
print("Son karakter:", son_karakter)
print("Büyük harflerle:", buyuk_isim)

#####################################################################################################################################################################

# Soru 3:
# Aşağıdaki string içinde "veri" kelimesi geçiyor mu kontrol edin.
# Ardından bu stringi boşluklardan bölerek liste haline getirin.

sentence = "Veri bilimi yapay zeka ile birleştiğinde güçlü sonuçlar doğurabilir."

# "veri" kelimesi geçiyor mu? (büyük-küçük harf duyarsız kontrol için lower() kullandım)
if "veri" in sentence.lower():
    print("Cümlede 'veri' kelimesi geçiyor.")
else:
    print("Cümlede 'veri' kelimesi geçmiyor.")

# Cümleyi boşluklardan bölüp liste haline getirme
kelimeler = sentence.split()
print("Liste haline getirilmiş kelimeler:", kelimeler)

#####################################################################################################################################################################

# Soru 4:
# İçerisinde 3 farklı türde veri bulunan bir liste oluşturun.
# Listenin uzunluğunu, ilk ve son elemanını yazdırın.
# Ardından bu listeye yeni bir eleman ekleyin ve ikinci elemanı silin.

# 3 farklı türde veri içeren liste
liste = [10, "merhaba", 3.14]

# Listenin uzunluğu
print("Listenin uzunluğu:", len(liste))

# İlk eleman
print("İlk eleman:", liste[0])

# Son eleman
print("Son eleman:", liste[-1])

# Yeni eleman ekleme
liste.append(True)  # Boolean türünde yeni eleman ekledik

print("Yeni eleman eklendikten sonra liste:", liste)

# İkinci elemanı silme (indeks 1)
del liste[1]

print("İkinci eleman silindikten sonra liste:", liste)

#####################################################################################################################################################################

# Soru 5:
# 2 parametre alan bir fonksiyon yazın. Bu fonksiyon, aldığı iki sayının ortalamasını dönsün.

def ortalama(sayi1, sayi2):
    return (sayi1 + sayi2) / 2

# Fonksiyonu test edelim
print(ortalama(10, 20))  # 15.0
print(ortalama(3.5, 7.5)) # 5.5

#####################################################################################################################################################################

# Soru 6:
# Kullanıcının yaşına göre mesaj yazdıran bir fonksiyon yazın:
# 18'den küçükse "Çok gençsin!", 18-40 arasıysa "Harika bir yaştasın!", 40'tan büyükse "Deneyim önemli!" mesajını yazdırsın.

def yas_mesaji(yas):
    if yas < 18:
        print("Hayat yeni başlıyor!")
    elif 18 <= yas <= 40:
        print("Harika bir yaştasın!")
    else:
        print("Deneyim önemli!")

# Fonksiyonu test edelim
yas_mesaji(15)  # Hayat yeni başlıyor!
yas_mesaji(25)  # Harika bir yaştasın!
yas_mesaji(50)  # Deneyim önemli!

#####################################################################################################################################################################

# Soru 7:
# İçerisinde sayılar olan bir liste içindeki sayıları dolaşarak 2 katını ekrana yazdırın (for döngüsü ile).

sayilar = [1, 5, 10, 7, 3]

for sayi in sayilar:
    print(sayi * 2)

#####################################################################################################################################################################

# Soru 8:
# 1'den başlayarak 20 dahil olacak şekilde çift sayıları yazdırın (while döngüsü ile).

sayi = 1
while sayi <= 20:
    if sayi % 2 == 0:
        print(sayi)
    sayi += 1

#####################################################################################################################################################################

# Soru 9:
# Bir çalışanın haftalık maaşını hesaplayan bir fonksiyon yazın.
# Saatlik ücreti ve haftalık toplam çalışma saati parametre olarak alınsın.
# Haftada 40 saatten fazla çalıştıysa, fazla saatler için %50 zamlı ücret ödensin (mesai).
# Örnek: 45 saat çalışan biri için 5 saatlik mesai uygulanmalı.

def haftalik_maas(saatlik_ucret, calisma_saati):
    normal_saat = min(calisma_saati, 40)
    mesai_saat = max(calisma_saati - 40, 0)
    
    # Normal ücret
    normal_ucret = normal_saat * saatlik_ucret
    
    # Mesai ücreti %50 zamlı
    mesai_ucret = mesai_saat * saatlik_ucret * 1.5
    
    toplam_ucret = normal_ucret + mesai_ucret
    return toplam_ucret

# Fonksiyonu test edelim
print(haftalik_maas(20, 38))  # 760 (38*20)
print(haftalik_maas(20, 45))  # 950 (40*20 + 5*20*1.5)

#####################################################################################################################################################################

