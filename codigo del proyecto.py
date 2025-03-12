import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder # Import LabelEncoder for encoding categorical features
from sklearn import metrics
from sklearn.metrics import r2_score,mean_squared_error

from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))
  
df = pd.read_csv(fn, encoding='latin-1', sep=';')

# Mostrar las primeras filas para entender la estructura
print(df.head())

features = ['Sexo', 'Edad', 'Nivel de estudios']
X = df[features]
y = df['Consumo de bebidas alchólicas']

label_encoder = LabelEncoder()

# Fit and transform the columns to numerical values (so that we can use RandomForestRegressor)
X['Sexo'] = label_encoder.fit_transform(X['Sexo'])
X['Nivel de estudios'] = label_encoder.fit_transform(X['Nivel de estudios'])
X['Edad'] = label_encoder.fit_transform(X['Edad'])
y=label_encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=77) #dividir la muestra entre train y test
# el modelo se adiestra
rf_model = RandomForestRegressor(random_state=77)
rf_model.fit(X_train, y_train)

# Vemos si predice bien los valores de test
y_pred = rf_model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
# Vemos los errores para ver el rendimiento
print(f"Mean Squared Error: {mse}")
print(f"R2 Score: {r2}")
