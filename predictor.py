import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder # Import LabelEncoder for encoding categorical features
from sklearn import metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import GridSearchCV


from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

df = pd.read_csv(fn, encoding='latin-1', sep=';')

features = ['Sexo', 'Edad', 'Nivel de estudios']
X = df[features]
y = df['Consumo de bebidas alchólicas']

# Ajustar y transformar las columnas a valores numéricos (para que podamos usar RandomForestClassifier)
label_encoder = LabelEncoder()

X.loc[:, 'Sexo'] = label_encoder.fit_transform(X['Sexo'])
X.loc[:, 'Nivel de estudios'] = label_encoder.fit_transform(X['Nivel de estudios'])
X.loc[:, 'Edad'] = label_encoder.fit_transform(X['Edad'])
y=label_encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=77) # Dividir la muestra entre train y test

# El modelo se adiestra
rf_model = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=5, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features='log2', max_leaf_nodes=None, min_impurity_decrease=0.0, bootstrap=True, oob_score=False, n_jobs=None, random_state=None, verbose=0, warm_start=False, class_weight=None, ccp_alpha=0.0, max_samples=None, monotonic_cst=None)
rf_model.fit(X_train, y_train)

# Vemos si predice bien los valores de test
y_pred = rf_model.predict(X_test)

# Vemos los errores para ver el rendimiento
print("Accuracy:", accuracy_score(y_test, y_pred)) # Cuantas predicciones son correctas
print("Precision:", precision_score(y_test, y_pred, average='weighted')) # Si es baja, da muchos falsos positivos.
print("Recall:", recall_score(y_test, y_pred, average='weighted')) # Si es baja, falla en detectar casos positivos.
