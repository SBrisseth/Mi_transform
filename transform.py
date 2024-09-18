import pandas as pd
import openpyxl
import os 

#leer la data

archivo =r"C:\Users\user\Desktop\SQL_IDAT\CERTUS_DA\DATAOPS\inventario.xlsx"

df = pd.read_excel(archivo)

#ordenamos por el precio 
df_result =df.sort_values(by='stock',ascending = False).reset_index(drop = True)

df_result.to_excel("inventario_ordenado.xlsx",index=False)