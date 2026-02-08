# Zad.1. W folderu z plikami znajdują się pliki graficzne w rozszerzeniu png. 
# Wybierz dwa dowolne zdjęcia i spróbuj (na ile to możliwe) odwzorować kodzie wykresy.
# %%

import xlrd
import openpyxl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlite3 import connect

#%%
data = pd.read_excel('ceny22.xlsx')
data_2 = pd.read_excel('oceny11.xlsx')
data_3= pd.read_csv("cechy22.csv", sep=";", decimal=",")
conn = connect('ceny_mleko.db')
data_4 = pd.read_sql("SELECT * FROM 'ceny_produktow'", con=conn)
# %%
x= data_4["Rok"]
y=data_4["Wartość"]
srednia = y.mean()

plt.figure(figsize=(10, 6))
plt.title("Dynamika cen mleka w latach dla Polski")
plt.xlabel("Rok")
plt.ylabel("Cena (PLN)")
plt.plot(x, y,'brown',linewidth=3,zorder =3)
plt.plot(x, y, '^',color ='brown',markersize=12,zorder=3)
plt.axhline(srednia, color = 'navy', linestyle = (0, (2, 2)),linewidth=2,zorder=3 )
plt.fill_between(x, y, 2.2, color="mistyrose",zorder =2)
plt.text (0.2,srednia*1.009,f"Średnia cena mleka {srednia:.2f} zł ", color = "navy")
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.3,zorder =1)
plt.tight_layout()
plt.savefig('Dynamika cen mleka w latach dla Polski.pdf', format='pdf')
# %%
