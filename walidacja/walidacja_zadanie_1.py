import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel("komputery.xlsx", sheet_name='Arkusz1')
df_2019 = df[df['Rok'] == 2019]

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(
    df_2019['Ilość'],
    labels=df_2019['Marka'],
    colors=['#F5FFC6', '#B4E1FF', '#FFACE4', '#C1FF9B'],
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2})
ax.set_title('Sprzedaż komputerów w 2019 roku\n(według marki)', fontsize=16,
             fontweight='bold', pad=20)
ax.set_aspect('equal')
plt.tight_layout()
plt.savefig('wykres_kołowy_2019.png', dpi=150, bbox_inches='tight')
plt.show()
