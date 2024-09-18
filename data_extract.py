import pandas as pd
import openpyxl
import os 

#leer la data

archivo =r"C:\Users\user\Desktop\SQL_IDAT\CERTUS_DA\DATAOPS\inventario_ordenado.xlsx"

df = pd.read_excel(archivo)

#exportamos en un excel los registros cuyo stock es 10
df_result =df[df['stock']==10]

df_result.to_excel("productos_reabastecer.xlsx",index=False)