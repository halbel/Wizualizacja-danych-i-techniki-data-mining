# Zad.1. W folderu z plikami znajdują się pliki graficzne w rozszerzeniu png. 
# Wybierz dwa dowolne zdjęcia i spróbuj (na ile to możliwe) odwzorować kodzie wykresy.

# %%
# import bibliotek

import xlrd
import openpyxl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from sqlite3 import connect

#%%
#pobranie danych

conn = connect('ceny_mleko.db')
data_4 = pd.read_sql("SELECT * FROM 'ceny_produktow'", con=conn)

# %%
# wykres na podstwie danyc z pliku

x = data_4["Rok"]
y =data_4["Wartość"]
srednia = y.mean()

plt.figure(figsize=(10, 6))

plt.title("Dynamika cen mleka w latach dla Polski")
plt.xlabel("Rok")
plt.ylabel("Cena (PLN)")

plt.plot(x, y,'brown',linewidth=3,zorder =3)
plt.plot(x, y, '^',color ='brown',markersize=12,zorder=3)
plt.axhline(srednia, color = 'navy', linestyle = (0, (2, 2)),linewidth=2,zorder=3)
plt.text (0.2,srednia*1.009,f"Średnia cena mleka {srednia:.2f} zł ", color = "navy")

plt.fill_between(x, y, 2.2, color="mistyrose",zorder =2)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.3,zorder =1)
plt.tight_layout()


plt.show()
# %%
# odwzorowanie wykresu_1

x_2 = np.array(["8:00","10:00","12:00","14:00","16:00","18:00","20:00","22:00"])
y_2= np.array([475,750,1250,900,1050,1450,1550,850])
srednia = 1065

plt.figure(figsize=(10, 6))

plt.title("Ruch na stronie internetowej - 24 sierpnia 2025")
plt.xlabel("Godzina")
plt.ylabel("Liczba odwiedzin")

plt.plot(x_2, y_2,'brown', linewidth=3, zorder =3)
plt.plot(x_2, y_2, '^', color ='brown',markersize=10,zorder=3)

plt.margins(y=0)
plt.ylim(0, 1800)

ax = plt.gca()
ax.yaxis.set_major_locator(MultipleLocator(250))

plt.axhline(srednia, color = 'navy', linestyle = (0, (2, 2)), linewidth=2,zorder=3)
plt.text (0.05,srednia*1.009,f"Średnia liczba odwiedzin ( {srednia:.2f})", color = "navy")
plt.fill_between(x_2, y_2, 2.2, color="mistyrose",zorder =2)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.3,zorder =1)
plt.tight_layout()


plt.show()

# %%
# odwzorowanie wykresu_2

data = {
    'id_aplikacji':[101, 102, 103, 104, 105, 106, 107],
    'rozmiar_aplikacji':[12, 45, 55, 75, 90, 120, 200],
    'liczba_pobran':[1200, 850, 720, 580, 450, 320, 180],
    'ocena_uzytkownikow':[4.8, 4.1, 4.5, 4.3, 3.9, 3.5, 3.2],
    'znizka':[0.15, 0.10, 0.12, 0.08, 0.05, 0.07, 0.03]
}
df = pd.DataFrame(data)
x_3 = df['rozmiar_aplikacji']
y_3 = df['liczba_pobran']
colors = df['ocena_uzytkownikow']
sizes = df['znizka'] * 1000 + 50

fig, ax = plt.subplots()
scatter = ax.scatter (x_3, y_3, s = sizes, c = colors, alpha = 0.9, cmap = 'turbo' )
cbar = fig.colorbar(scatter, ax=ax)
cbar.set_label('Średnia ocena użytkowników')
ax.set_xlabel('Rozmiar aplikacji (MB)')
ax.set_ylabel('Liczba pobrań (tysiące)')
ax.set_title('Statystyki aplikacji mobilnej')
ax.grid(True, alpha=0.3)


plt.show()