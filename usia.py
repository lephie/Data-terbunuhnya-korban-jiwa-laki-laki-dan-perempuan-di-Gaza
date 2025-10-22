import pandas as pd
import matplotlib.pyplot as plt 


data = pd.read_excel("killed-in-gaza.xlsx")

jumlah_sex = data['sex'].value_counts()
persentase_sex = (jumlah_sex / len(data)) * 100

bins = [0, 12, 18, 30, 50, 65, 120] 
labels = ['Anak-anak', 'Remaja', 'Dewasa Muda', 'Dewasa', 'Paruh Baya', 'Lansia']
data['kelompok_usia'] = pd.cut(data['age'], bins=bins, labels=labels, right=False)

jumlah_usia = data['kelompok_usia'].value_counts().sort_index()
rata_rata_usia = data['age'].mean()

 
plt.figure(figsize=(8, 5))
plt.bar(jumlah_usia.index, jumlah_usia.values, color=['#0A90B1'], edgecolor='black')
plt.title("Distribusi Korban Berdasarkan Kelompok Usia di Gaza")
plt.xlabel("Kelompok Usia")
plt.ylabel("Jumlah Korban")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()