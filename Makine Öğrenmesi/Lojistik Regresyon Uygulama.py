######################################################
 # Diabetes Prediction with Logistic Regression
 ######################################################
 # İş Problemi:
 # Özellikleri belirtildiğinde kişilerin diyabet hastası olup
 # olmadıklarını tahmin edebilecek bir makine öğrenmesi
 # modeli geliştirebilir misiniz?
 # Veri seti ABD'deki Ulusal Diyabet-Sindirim-Böbrek Hastalıkları Enstitüleri'nde tutulan büyük veri setinin
 # parçasıdır. ABD'deki Arizona Eyaleti'nin en büyük 5. şehri olan Phoenix şehrinde yaşayan 21 yaş ve üzerinde olan
 # Pima Indian kadınları üzerinde yapılan diyabet araştırması için kullanılan verilerdir. 768 gözlem ve 8 sayısal
 # bağımsız değişkenden oluşmaktadır. Hedef değişken "outcome" olarak belirtilmiş olup; 1 diyabet test sonucunun
 # pozitif oluşunu, 0 ise negatif oluşunu belirtmektedir.
 # Değişkenler
 # Pregnancies: Hamilelik sayısı
 # Glucose: Glikoz.
 # BloodPressure: Kan basıncı.
 # SkinThickness: Cilt Kalınlığı
 # Insulin: İnsülin.
 # BMI Beden kitle indeksi.
 # DiabetesPedigreeFunction: Soyumuzdaki kişilere göre diyabet olma ihtimalimizi hesaplayan bir fonksiyon.
 # Age: Yaş (yıl)
 # Outcome: Kişinin diyabet olup olmadığı bilgisi. Hastalığa sahip 1 ya da değil 0
 # 1. Exploratory Data Analysis
 # 2. Data Preprocessing
 # 3. Model & Prediction
 # 4. Model Evaluation
 # 5. Model Validation: Holdout
 # 6. Model Validation: 10Fold Cross Validation
 # 7. Prediction for A New Observation

 # 1. Gerekli Kütüphaneler
 import pandas as pd
 import numpy as np
 import seaborn as sns
 import matplotlib.pyplot as plt
 from sklearn.model_selection import train_test_split, cross_validate
 from sklearn.preprocessing import RobustScaler
 from sklearn.linear_model import LogisticRegression
 from sklearn.metrics import accuracy_score, roc_auc_score, confusion_matrix, classification_report, RocCurveDisp
 # 2. Yardımcı Fonksiyonlar
 def outlier_thresholds(df, col, q10.05, q30.95
    q1_val = df[col].quantile(q1)
    q3_val = df[col].quantile(q3)
    iqr = q3_val - q1_val
    low_limit = q1_val  1.5 * iqr
    up_limit = q3_val  1.5 * iqr
    return low_limit, up_limit
 def replace_with_thresholds(df, col):
    low, up = outlier_thresholds(df, col)
    df[col] = np.where(df[col] < low, low, np.where(df[col] > up, up, df[col]))
 def plot_confusion_matrix(y_true, y_pred):
    acc = round(accuracy_score(y_true, y_pred), 2)
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt="d")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title(f"Accuracy: {acc}")
    plt.show()
 # 3. Veri Yükleme ve İlk İnceleme
 df = pd.read_csv(r"\Miuul Yaz Kampı\diabetes.csv")
 target = "Outcome"
 features = [col for col in df.columns if col ! target]
 # 4. Eksik ve Aykırı Değer İşleme
 for col in features:
    replace_with_thresholds(df, col)
 # 5. Ölçekleme
 scaler  RobustScaler()
 df[features] = scaler.fit_transform(df[features])
 # 6. Modelleme
 X  df[features]
 y = df[target]
 log_model  LogisticRegression().fit(X, y)
 y_pred = log_model.predict(X)

 y_prob = log_model.predict_proba(X)[:, 1
 # 7. Başarı Değerlendirmesi Tüm veri seti ile)
 print("Training Classification Report:\n", classification_report(y, y_pred))
 plot_confusion_matrix(y, y_pred)
 print("ROC AUC Score Train):", roc_auc_score(y, y_prob))
 # 8. Holdout Doğrulama
 X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=17
 log_model  LogisticRegression().fit(X_train, y_train)
 y_pred = log_model.predict(X_test)
 y_prob = log_model.predict_proba(X_test)[:, 1
 print("Holdout Classification Report:\n", classification_report(y_test, y_pred))
 RocCurveDisplay.from_estimator(log_model, X_test, y_test)
 plt.title("ROC Curve Test Set)")
 plt.plot([0, 1, 0, 1, "r--")
 plt.show()
 print("ROC AUC Score Test):", roc_auc_score(y_test, y_prob))
 # 9. 10Fold Cross Validation
 cv_results = cross_validate(log_model, X, y, cv=10,
                            scoring=["accuracy", "precision", "recall", "f1", "roc_auc"])
 print("CV Accuracy:", cv_results["test_accuracy"].mean())
 print("CV Precision:", cv_results["test_precision"].mean())
 print("CV Recall:", cv_results["test_recall"].mean())
 print("CV F1 Score:", cv_results["test_f1"].mean())
 print("CV ROC AUC", cv_results["test_roc_auc"].mean())
 # 10. Yeni Gözlem Üzerinden Tahmin
 new_sample  X.sample(1, random_state=45
 prediction = log_model.predict(new_sample)
 print("New Sample Prediction:", prediction)