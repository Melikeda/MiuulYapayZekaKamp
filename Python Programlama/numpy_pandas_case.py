###############################
# Numpy & Pandas - Ödev Soruları
###############################

########################################################################################################################################################################

import numpy as np
import pandas as pd
import seaborn as sns

###############################
# Soru 1:
# 1D ve 2D array'ler oluşturun.
# Bu array’lerin boyut, eleman sayısı ve şekil bilgilerini yazdırın.

arr1d = np.arange(10, 20)
arr2d = np.random.randint(1, 100, size=(3, 4))

print("1D:", arr1d.ndim, arr1d.size, arr1d.shape)
print("2D:", arr2d.ndim, arr2d.size, arr2d.shape)

########################################################################################################################################################################

# Soru 2:
# 5 elemanlı rastgele sayılardan oluşan bir array oluşturun.
# Elemanların ortalamasını, standart sapmasını ve medyanını bulun.

random_array = np.random.randint(50, 100, size=5)
print("Array:", random_array)
print("Ortalama:", np.mean(random_array))
print("Standart Sapma:", np.std(random_array))
print("Medyan:", np.median(random_array))

########################################################################################################################################################################

# Soru 3:
# 0 ile 1 arasında 10 eşit aralıklı sayı üretin.
# Bu sayılardan 0.5'ten büyük olanları filtreleyip yazdırın.

lin_arr = np.linspace(0, 1, 10)
filtered = lin_arr[lin_arr > 0.5]
print("Orijinal:", lin_arr)
print("Filtrelenmiş:", filtered)

########################################################################################################################################################################

# Soru 4:
# Pandas Series kullanarak öğrencilerin yaşlarını tutan bir seri oluşturun.
# Yaş ortalamasını ve en küçük yaşı bulun.

ages = pd.Series([19, 22, 21, 20, 23, 18])
print("Ortalama Yaş:", ages.mean())
print("En Küçük Yaş:", ages.min())

########################################################################################################################################################################

# Soru 5:
# seaborn içerisinden "diamonds" veri setini alın.
# Sadece "carat" ve "price" sütunlarını içeren ilk 5 satırı yazdırın.

df = sns.load_dataset("diamonds")
print(df[["carat", "price"]].head())

########################################################################################################################################################################

# Soru 6:
# Fiyatı 15.000’den fazla olan kaç elmas var?

count_expensive = df[df["price"] > 15000].shape[0]
print("15.000'den pahalı elmas sayısı:", count_expensive)

########################################################################################################################################################################

# Soru 7:
# “cut” sütunundaki her bir kesim tipi için ortalama fiyatı(price) hesaplayın.

avg_price_per_cut = df.groupby("cut")["price"].mean()
print(avg_price_per_cut)

########################################################################################################################################################################

# Soru 8:
# pivot_table kullanarak her “cut” tipi için hem ortalama “carat” hem de “price” değerlerini gösterin.

pivot_table = df.pivot_table(
    values=["carat", "price"],
    index="cut",
    aggfunc="mean"
)
print(pivot_table)

########################################################################################################################################################################

# Soru 9:
# “color” sütununda kaç farklı renk olduğunu bulun. Her bir rengin kaç kez geçtiğini de yazdırın.

print("Farklı Renk Sayısı:", df["color"].nunique())
print("Renk Frekansları:\n", df["color"].value_counts())

########################################################################################################################################################################

# Soru 10:
# “cut” ve “clarity” kombinasyonlarına göre ortalama fiyatları hesaplayın.

grouped = df.groupby(["cut", "clarity"])["price"].mean()
print(grouped)

########################################################################################################################################################################
