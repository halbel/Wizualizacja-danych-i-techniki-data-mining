#Zad.3. Wybierz jeden inny plik z danymi - stwórz dowolny wykres na jego bazie. 
# Zadbaj o jego podpisanie i estetykę.
#%%
#import bibliotek
import openpyxl
import pandas as pd
import matplotlib.pyplot as plt

#%%
#pobieranie danych
data = pd.read_excel('ceny22.xlsx')
# %%
# czyszczenie danych
data['Rodzaje produktów'] = data['Rodzaje produktów'].str.split(" - ").str[0]
# %%
# pivotowanie tabeli
data_pivot = data.pivot(index = "Rok",
                  columns = "Rodzaje produktów",
                  values= "Wartosc")

# %%
# wyświetlenie wykresu
plt.plot(data_pivot.index, data_pivot ['filety z morszczuka mrożone'], color="darkseagreen",linewidth=2, markersize=8,marker = "8", label ="Filety z morszczuka, mrożone" )
plt.plot(data_pivot.index, data_pivot ['pstrąg świeży niepatroszony'], color="mediumpurple",linewidth=2, markersize=8,marker = "8",label ="Pstrąg świeży, niepatroszony")
plt.plot(data_pivot.index, data_pivot ['śledź solony, niepatroszony'], color="burlywood",linewidth=2, markersize=8,marker = "8",label ="Śledź solony, niepatroszony")
plt.xlabel("Rok")
plt.xticks(rotation=45)
plt.ylabel("Wartość  zł / kg ")
plt.title("Dynamika cen w czasie")
plt.legend(loc = 0)
plt.grid(True)
plt.tight_layout()
plt.show()
