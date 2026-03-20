#Zad.2. Na bazie pliku oceny11.xlsx stwórz wykres słupkowy. 
#Zadbaj o jego podpisanie i estetykę.

# %%
# import bibliotek 
import xlrd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%
# wczytanie danych
data = pd.read_excel('oceny11.xlsx')

#%% 
# tworzenie wykresu
Klasa = data["Klasa"]
Matematyka = data['Matematyka']
Polski = data["Polski"]
Angielski = data ["Angielski"]

X = np.arange(len(Klasa))

fig, ax = plt.subplots()

bar1 = ax.bar (X - 0.25, Matematyka,color='mediumblue',width=0.25, label= "Matematyka" )
bar2 = ax.bar (X, Polski, color = 'forestgreen', width = 0.25 , label = "Polski")
bar3 = ax.bar (X + 0.25, Angielski, color = 'orangered', width = 0.25, label = "Angielski")

ax.bar_label(bar1, fmt='%.2f', padding=3, fontsize=6)
ax.bar_label(bar2, fmt='%.2f', padding=3, fontsize=6)
ax.bar_label(bar3, fmt='%.2f', padding=3, fontsize=6)

ax.set_xticks (X)
ax.set_xticklabels (Klasa)
plt.ylim (0, 7)
ax.legend ()
ax.set_title ('Średnia z ocen w poszczególnych klasach', fontsize=12)
ax.set_ylabel ('Średnia z ocen')
ax.set_xlabel ('Klasa')
ax.grid (axis='y', alpha=0.2)
fig.tight_layout()
plt.savefig('Zadanie_2.pdf', format='png')
plt.show()