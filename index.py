import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

try:
    df = pd.read_excel('killed-in-gaza.xlsx')
except FileNotFoundError:
    print("Error: File Not found")
    exit()

count_death = df["sex"].value_counts()
label = count_death.index.tolist()

plt.pie(
    count_death,
    labels=label,
    autopct='%1.1f%%',
    startangle=90,
    colors=['#66b3ff', '#ff9999']
)

plt.title("Presentase Male Vs Female")
plt.axis('equal')
plt.show()

