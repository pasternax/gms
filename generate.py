import pandas as pd
import random
import matplotlib.pyplot as plt

coordinates = [{"X": random.uniform(0, 100), "Y": random.uniform(0, 100)} for _ in range(5)]

data = []

for i in range(1, 6):
    speeds = [random.uniform(1400, 2500) for _ in range(10)]
    times = [random.uniform(10, 100) for _ in range(10)]

    data.extend(
        [{"Буровая установка": i, "Скорость (м/с)": speed, "Время (с)": time,
          "X-координата": coordinates[i-1]["X"], "Y-координата": coordinates[i-1]["Y"]}
         for speed, time in zip(speeds, times)]
    )

df = pd.DataFrame(data)

file_path = "Data/data.xlsx"

with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
    for name, group in df.groupby('Буровая установка'):
        group.drop('Буровая установка', axis=1).to_excel(writer, sheet_name=f'Буровая_{name}', index=False)

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_title('Карта с буровыми установками')

for _, row in df.groupby('Буровая установка').head(1).iterrows():
    ax.scatter(row['X-координата'], row['Y-координата'], label=f'Буровая {row["Буровая установка"]}')

ax.legend()
plt.show()
