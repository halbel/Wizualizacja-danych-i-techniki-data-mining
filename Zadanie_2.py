#Zad.2. Na bazie pliku oceny11.xlsx stwórz wykres słupkowy. 
#Zadbaj o jego podpisanie i estetykę.

# %%
import xlrd
import openpyxl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from sqlite3 import connect

#%%
data = pd.read_excel('oceny11.xlsx')

#%% 
Klasa = data["Klasa"]
Matematyka = data['Matematyka']
Polski = data["Polski"]
Angielski = data ["Angielski"]

X = np.arange(len(Klasa))
fig, ax = plt.subplots()
ax.bar (X-0.25, Matematyka,color='mediumblue',width=0.25, label= "Matematyka" )
ax.bar (X, Polski, color = 'forestgreen', width = 0.25 , label = "Polski")
ax.bar (X + 0.25, Angielski, color = 'orangered', width = 0.25, label = "Angielski")
ax.set_xticks (X)
ax.set_xticklabels (Klasa)
plt.ylim (0, 7)
ax.legend ()
ax.set_title ('Średnia z ocen w poszczególnych klasach', fontsize=10)
ax.set_ylabel ('Średnia z ocen')
ax.set_xlabel ('Klasa')
ax.grid (axis='y', alpha=0.3)
fig.tight_layout()
plt.show()
plt.savefig('Zadanie_2.pdf', format='png')
# %%
