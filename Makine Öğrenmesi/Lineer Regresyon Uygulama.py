 ######################################################
 # Diamonds Price Prediction with Linear Regression
 ######################################################
 #########################################################
 # 1. Kütüphanelerin İçe Aktarılması
 #########################################################
 # Veri işleme, görselleştirme ve modelleme için gerekli kütüphaneleri yüklüyoruz.
 import seaborn as sns
 import pandas as pd
 import numpy as np
 import matplotlib.pyplot as plt
 from sklearn.linear_model import LinearRegression
 from sklearn.metrics import mean_squared_error, r2_score
 from sklearn.model_selection import train_test_split
 sns.set_theme()
 #########################################################
 # 2. Veri Setinin Yüklenmesi
 #########################################################
 # Seaborn'dan gelen diamonds veri seti, elmasların özelliklerini ve fiyatlarını içerir.
 df = sns.load_dataset("diamonds")
 print(df.head())
 print(df.describe())
 #########################################################
 # 3. Keşifsel Veri Analizi EDA
 #########################################################
 # Elmas fiyatlarıyla karat ağırlığı arasındaki ilişkiyi inceliyoruz.
 sns.scatterplot(x="carat", y="price", data=df, alpha=0.5
 plt.title("Elmas Karat Ağırlığı ve Fiyat İlişkisi")
 plt.xlabel("Karat (carat)")
 plt.ylabel("Fiyat (price)")
 plt.show()
 #########################################################
 # 4. Basit Lineer Regresyon Modeli (carat → price)
 #########################################################
 # Sadece "carat" değişkeni ile fiyat tahmini yapacağız.
 X  df[["carat"]]  # bağımsız değişken 2D
 y = df["price"]    # bağımlı değişken 1D
 model  LinearRegression()
 model.fit(X, y)
 print(f"Model sabiti (b): {model.intercept_:.2f}")
 print(f"Katsayı (w): {model.coef_0.2f}")

 #########################################################
 # 5. Regresyon Doğrusunun Görselleştirilmesi
 #########################################################
 # Scatter plot üzerine modelin tahmin doğrusunu ekliyoruz.
 sns.regplot(x="carat", y="price", data=df, ci=None, line_kws={"color": "red"})
 plt.title(f"price = {model.intercept_:.2f} + {model.coef_0.2f} * carat")
 plt.xlabel("Karat")
 plt.ylabel("Fiyat")
 plt.show()
 #########################################################
 # 6. Model Performans Değerlendirmesi
 #########################################################
 # Eğitim verisi üzerinden tahminler yaparak hata metriklerini hesaplıyoruz.
 y_pred = model.predict(X)
 mse = mean_squared_error(y, y_pred)
 rmse = np.sqrt(mse)
 r2  r2_score(y, y_pred)
 print(f"Mean Squared Error MSE {mse:.2f}")
 print(f"Root Mean Squared Error RMSE {rmse:.2f}")
 print(f"R² Score: {r2.2f}")
 #########################################################
 # 7. Yeni Bir Gözlem Üzerinden Tahmin
 #########################################################
 # 1.5 karatlık bir elmasın tahmini fiyatını hesaplıyoruz.
 yeni_elmas = 1.5  # 1.5 karatlık elmas
 tahmini_fiyat = model.predict(yeni_elmas)[0]
 print(f"1.5 karat elmas için tahmini fiyat: {tahmini_fiyat:.2f} $")                      