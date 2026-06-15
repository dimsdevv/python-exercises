import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys

sys.stdout.reconfigure(encoding='utf-8')

np.random.seed(42)  

n_students = 100
categories = ['Tugas', 'UTS', 'UAS']
weights    = [0.2, 0.3, 0.5]

tugas = np.clip(np.random.normal(75, 12, n_students), 40, 100)
uts   = np.clip(np.random.normal(70, 15, n_students), 30, 100)
uas   = np.clip(np.random.normal(72, 14, n_students), 30, 100)
nilai_akhir = (tugas * weights[0]) + (uts * weights[1]) + (uas * weights[2])
def get_grade(score):
    if score >= 85: return 'A'
    elif score >= 75: return 'B'
    elif score >= 60: return 'C'
    elif score >= 50: return 'D'
    else: return 'E'

huruf = [get_grade(s) for s in nilai_akhir]

grade_counts = {grade: huruf.count(grade) for grade in ['A', 'B', 'C', 'D', 'E']}

print("=" * 60)
print(f"{'STATISTIK NILAI AKHIR (100 Mahasiswa)':^60}")
print("=" * 60)
print(f"Rata-rata Kelas : {np.mean(nilai_akhir):.2f}")
print(f"Nilai Tertinggi : {np.max(nilai_akhir):.2f}")
print(f"Nilai Terendah  : {np.min(nilai_akhir):.2f}")
print(f"Distribusi Nilai: A({grade_counts['A']}), B({grade_counts['B']}), C({grade_counts['C']}), D({grade_counts['D']}), E({grade_counts['E']})")
print("=" * 60)


# =====================================================================
# VISUALISASI
# =====================================================================
# Setting figure
fig = plt.figure(figsize=(18, 6))
fig.suptitle("Analisis Data Nilai Mahasiswa", fontsize=16, fontweight='bold', color='#2c3e50')
fig.patch.set_facecolor('#f4f6f9')

# ---------------------------------------------------------------------
# 1. 3D Surface Plot (Hubungan Tugas, UTS, dan UAS)
# ---------------------------------------------------------------------
ax1 = fig.add_subplot(131, projection='3d')
ax1.set_facecolor('#f4f6f9')

# Buat grid yang lebih detail untuk bentuk melengkung yang mulus
x_surf = np.linspace(40, 100, 40)
y_surf = np.linspace(30, 100, 40)
X, Y = np.meshgrid(x_surf, y_surf)

# Buat bentuk matematis sedikit melengkung (non-linear) agar lebih terlihat 3D
# Kita gunakan persamaan regresi parabolik buatan agar bentuk surfenya menarik (bentuk mangkuk terbalik ringan)
Z = 100 - (((X - 100)**2) * 0.01 + ((Y - 100)**2) * 0.008)
Z = np.clip(Z, 20, 100)

# Plot surface dengan colormap yang mencolok (plasma/viridis/inferno) dan tanpa garis tepi jaring
surf = ax1.plot_surface(X, Y, Z, cmap='plasma', alpha=0.85, 
                        linewidth=0, antialiased=True, zorder=0)

# Tambahkan garis kontur (topografi) di dasar (Z=20) dan di permukaan agar efek 3D lebih kuat
ax1.contour(X, Y, Z, zdir='z', offset=20, cmap='plasma', alpha=0.5)

# Posisikan titik scatter agar berada di atas dan di bawah surface (sebaran acak untuk ilusi)
# Hubungkan dengan tiang vertikal (stem) ke permukaan dasar agar terlihat mengambang di 3D
for i in range(len(tugas)):
    ax1.plot([tugas[i], tugas[i]], [uts[i], uts[i]], [20, uas[i]], color='gray', alpha=0.3, linewidth=0.5, zorder=1)

# Plot titik datanya dengan tepian putih agar menonjol
scatter = ax1.scatter(tugas, uts, uas, c=uas, cmap='plasma', marker='o', 
                      s=30, edgecolor='white', alpha=1.0, label='Nilai Aktual Mahasiswa', zorder=5)

cbar = fig.colorbar(surf, ax=ax1, shrink=0.4, aspect=15, pad=0.08)
cbar.set_label('Skala Nilai UAS\n ', fontsize=9, labelpad=10)

ax1.set_title("3D Surface:\nHubungan Nilai Tugas, UTS, dan UAS", fontweight='bold', fontsize=11, pad=15)
ax1.set_xlabel('Nilai Tugas (X)', fontsize=9, labelpad=10)
ax1.set_ylabel('Nilai UTS (Y)', fontsize=9, labelpad=10)
ax1.set_zlabel('Nilai UAS (Z)', fontsize=9, labelpad=10)

ax1.tick_params(axis='x', pad=3)
ax1.tick_params(axis='y', pad=3)
ax1.tick_params(axis='z', pad=3)


ax1.set_zlim(20, 100)

ax1.view_init(elev=25, azim=-125) 


ax1.xaxis.pane.fill = False
ax1.yaxis.pane.fill = False
ax1.zaxis.pane.fill = False
ax1.xaxis.pane.set_edgecolor('white')
ax1.yaxis.pane.set_edgecolor('white')
ax1.zaxis.pane.set_edgecolor('white')


# 2. Histogram (Distribusi Nilai Akhir)
ax2 = fig.add_subplot(132)
ax2.set_facecolor('#eaf2fb')

# Plot histogram
n, bins, patches = ax2.hist(nilai_akhir, bins=10, color='#3498db', edgecolor='white', linewidth=1.5, alpha=0.9)

import matplotlib.cm as cm
for c, p in zip(n, patches):
    color_val = c / max(n) if max(n) > 0 else 0
    plt.setp(p, 'facecolor', cm.Blues(color_val * 0.6 + 0.4))
mean_val = np.mean(nilai_akhir)
ax2.axvline(mean_val, color='#e74c3c', linestyle='dashed', linewidth=2, label=f'Rata-rata: {mean_val:.1f}')

ax2.set_title("Histogram:\nDistribusi Nilai Akhir", fontweight='bold', fontsize=11)
ax2.set_xlabel("Nilai Akhir (Skala 0-100)")
ax2.set_ylabel("Jumlah Mahasiswa (Frekuensi)")
ax2.grid(axis='y', linestyle='--', alpha=0.7)
ax2.set_axisbelow(True)
ax2.legend()


# 3. Pie Chart (Proporsi Grade A, B, C, D, E)
ax3 = fig.add_subplot(133)
ax3.set_facecolor('#f4f6f9')

labels = list(grade_counts.keys())
sizes = list(grade_counts.values())

color_map = {'A': '#2ecc71', 'B': '#3498db', 'C': '#f39c12', 'D': '#e67e22', 'E': '#e74c3c'}
f_labels = [l for l, s in zip(labels, sizes) if s > 0]
f_sizes  = [s for s in sizes if s > 0]
f_colors = [color_map[l] for l in f_labels]

# Menonjolkan ('explode') slice yang paling dominan (terbesar)
if len(f_sizes) > 0:
    explode = [0.1 if s == max(f_sizes) else 0 for s in f_sizes] 
else:
    explode = []

wedges, texts, autotexts = ax3.pie(
    f_sizes, 
    explode=explode, 
    labels=f_labels, 
    colors=f_colors, 
    autopct='%1.1f%%',
    shadow=True, 
    startangle=140,
    textprops=dict(color="black", fontweight='bold')
)

ax3.set_title("Pie Chart:\nKomposisi Grade Kelas", fontweight='bold', fontsize=11)
ax3.axis('equal') 
ax3.legend(wedges, f_labels, title="Grade", loc="best", bbox_to_anchor=(0.9, 0, 0.5, 1))

# ---------------------------------------------------------------------
# Menyimpan dan menampilkan
# ---------------------------------------------------------------------
# Tambahkan padding layout agar tidak terlalu mepet
plt.tight_layout(w_pad=3.0, h_pad=2.0)
plt.subplots_adjust(top=0.88, bottom=0.15) # Mengatur spacing untuk suptitle utama di atas grafik

save_path = r"d:\fufufafa\Belajar Python H-3\visualisasi_nilai3D.png"
plt.savefig(save_path, dpi=150, bbox_inches='tight', pad_inches=0.2)
print(f"\n[INFO] Grafik telah disimpan sebagai gambar di: {save_path}")

plt.show()
