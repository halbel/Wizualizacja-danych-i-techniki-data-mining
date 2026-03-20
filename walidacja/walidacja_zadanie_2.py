import matplotlib.pyplot as plt


miesiace = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec']
zuzycie = [378, 365, 340, 285, 228, 195]
srednia = 295

fig, ax = plt.subplots(figsize=(10, 6))
ax.fill_between(miesiace, zuzycie, alpha=0.15, color='lightblue', zorder=1)
ax.plot(miesiace, zuzycie, color='navy', linewidth=2.5, zorder=3)
ax.plot(miesiace, zuzycie, marker='^', color='navy', markersize=8,
        linestyle='None', zorder=4)
ax.axhline(y=srednia, color='red', linestyle=':', linewidth=2, zorder=2)
ax.text(0.02, srednia+8, f'Średnie zużcie({srednia} kWh)',
        transform=ax.get_yaxis_transform(), color='red', fontsize=10)
ax.set_xlim(-0.3, 5.3)
ax.set_ylim(0, 420)
ax.set_xlabel('Miesiąc', fontsize=11)
ax.set_ylabel('Zużycie (kWh)', fontsize=11)
ax.set_title('Zużycie energii elektrycznej - I półrocze 2025', fontsize=13)
ax.grid(True, color='lightgray', linewidth=0.8, zorder=0)
ax.set_facecolor('white')
plt.tight_layout()
plt.savefig('zuzycie_energii.png', dpi=150, bbox_inches='tight')
plt.show()
print("Wykres zapisany.")
