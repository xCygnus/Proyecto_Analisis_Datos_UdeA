import os
import pandas as pd
base_path = os.path.dirname(__file__) 
file_path = os.path.join(base_path, 'data', 'raw',
'dataset_regresion_listings.csv')
df = pd.read_csv(file_path)
print('Número de observaciones (filas):', df.shape[0])
print('Número de variables (columnas):', df.shape[1])