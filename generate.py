import pandas as pd
import random
import matplotlib.pyplot as plt

coordinates = [{"X": random.uniform(0, 100), "Y": random.uniform(0, 100)} for _ in range(5)]

data = []

for i in range(1, 6):
    speeds = [random.uniform(1400, 2500) for _ in range(10)]
    times = [random.uniform(10, 100) for _ in range(10)]

    data.append({"Буровая установка": i, "Скорости (м/с)": speeds, "Времена (с)": times,
                 "X-координата": coordinates[i-1]["X"], "Y-координата": coordinates[i-1]["Y"]})

df = pd.DataFrame(data)

file_path = "Data/data.xlsx"
df.to_excel(file_path, index=False)

print(df)

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_title('Карта с буровыми установками')

for index, row in df.iterrows():
    ax.scatter(row['X-координата'], row['Y-координата'], label=f'Буровая {row["Буровая установка"]}')

ax.legend()
plt.show()
