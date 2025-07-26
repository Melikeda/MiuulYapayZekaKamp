 ################################################
 # CART Classification and Regression Trees)
 ################################################
 # Gerekli kütüphaneler
 import warnings
 import joblib
 import numpy as np
 import pandas as pd
 import seaborn as sns
 import matplotlib.pyplot as plt
 import pydotplus
 from sklearn.tree import DecisionTreeClassifier, export_graphviz, export_text, plot_tree
 from sklearn.metrics import classification_report, roc_auc_score
 from sklearn.model_selection import train_test_split, GridSearchCV, cross_validate, validation_curve
 from skompiler import skompile
 from sklearn.tree import export_graphviz
 from graphviz import Source
 warnings.simplefilter(action='ignore', category=Warning)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', 500
 ################################################
 # 1. Veri Yükleme ve Ön İşleme
 ################################################
 df = pd.read_csv(r"\Miuul Yaz Kampı\diabetes.csv")
 df.head()
 y = df["Outcome"]
 X  df.drop("Outcome", axis=1
 ################################################
 # 2. Modelleme: Temel CART
 ################################################

model  DecisionTreeClassifier(random_state=1.fit(X, y)
 y_pred = model.predict(X)
 y_prob = model.predict_proba(X)[:, 1
 print("Confusion Matrix:\n", classification_report(y, y_pred))
 print("ROC AUC", roc_auc_score(y, y_prob))
 ################################################
 # 3. Holdout Yöntemiyle Değerlendirme
 ################################################
 X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=45
 model  DecisionTreeClassifier(random_state=17.fit(X_train, y_train)
 # Eğitim verisi değerlendirme
 print("Train Score:\n", classification_report(y_train, model.predict(X_train)))
 print("Train ROC AUC", roc_auc_score(y_train, model.predict_proba(X_train)[:, 1
 # Test verisi değerlendirme
 print("Test Score:\n", classification_report(y_test, model.predict(X_test)))
 print("Test ROC AUC", roc_auc_score(y_test, model.predict_proba(X_test)[:, 1
 ################################################
 # 4. Cross Validation CV
 ################################################
 cv_model  DecisionTreeClassifier(random_state=17
 cv_results = cross_validate(cv_model, X, y, cv=5, scoring=["accuracy", "f1", "roc_auc"])
 print("CV Accuracy:", cv_results['test_accuracy'].mean())
 print("CV F1", cv_results['test_f1'].mean())
 print("CV ROC AUC", cv_results['test_roc_auc'].mean())
 ################################################
 # 5. Hiperparametre Optimizasyonu
 ################################################
 params = {"max_depth": range(1, 11, "min_samples_split": range(2, 20
 grid  GridSearchCV(cv_model, params, cv=5, n_jobs=-1, verbose=1.fit(X, y)
 print("Best Params:", grid.best_params_)
 print("Best CV Score:", grid.best_score_)
 ################################################
 # 6. Final Model
 ################################################
 final_model  DecisionTreeClassifier(**grid.best_params_, random_state=17.fit(X, y)
 final_cv = cross_validate(final_model, X, y, cv=5, scoring=["accuracy", "f1", "roc_auc"])
 print("Final CV Accuracy:", final_cv['test_accuracy'].mean())
 print("Final CV F1", final_cv['test_f1'].mean())
 print("Final CV ROC AUC", final_cv['test_roc_auc'].mean())
 ################################################
 # 7. Özellik Önem Grafiği
 ################################################
def plot_importance(model, features, top_n=10
 importance_df = pd.DataFrame({'Feature': features.columns, 'Importance': model.feature_importances_})
 importance_df = importance_df.sort_values("Importance", ascending=False).head(top_n)
 plt.figure(figsize=(8, 6
 sns.barplot(x="Importance", y="Feature", data=importance_df)
 plt.title("Feature Importances")
 plt.tight_layout()
 plt.show()
 plot_importance(final_model, X
 ################################################
 # 8. Validation Curve BONUS
 ################################################
 def val_curve(model, X, y, param_name, param_range, scoring="roc_auc", cv=10
 train_scores, test_scores = validation_curve(
 estimator=model,
 XX,
 y=y,
 param_name=param_name,
 param_range=param_range,
 scoring=scoring,
 cv=cv)
 plt.plot(param_range, train_scores.mean(axis=1, label="Train")
 plt.plot(param_range, test_scores.mean(axis=1, label="Validation")
 plt.title(f"Validation Curve: {param_name}")
 plt.xlabel(param_name)
 plt.ylabel(scoring.upper())
 plt.legend()
 plt.tight_layout()
 plt.show()
 val_curve(final_model, X, y, param_name="max_depth", param_range=range(1, 11
 val_curve(final_model, X, y, param_name="max_depth", param_range=range(2, 20
 ################################################
 # 9. Karar Ağacını Görselleştirme
 ################################################
 def plot_tree_inline(model, feature_names):
 plt.figure(figsize=(40, 20
 plot_tree(model, feature_names=feature_names, filled=True, class_names=True, rounded=True)
 plt.title("Decision Tree")
 plt.show()
 plot_tree_inline(final_model, X.columns)
 ################################################
 # 10. Karar Kurallarını ve Kodları Çıkarma
 ################################################
 print(export_text(final_model, feature_names=list(X.columns)))
 print(skompile(final_model.predict).to("python/code"))
 # Örnek tahmin
 sample = pd.DataFrame([X.iloc[1].values], columns=X.columns)
 print("Prediction:", final_model.predict(sample))