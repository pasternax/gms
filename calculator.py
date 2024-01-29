import random

data = []

for i in range(1, 11):
    speeds = [random.uniform(1400, 2500) for _ in range(10)]
    times = [random.uniform(10, 100) for _ in range(10)]

    data.append({"Буровая установка": i, "Скорость (м/с)": speeds, "Время (с)": times})

for entry in data:
    print(f"Буровая установка {entry['Буровая установка']}:")
    for j in range(10):
        print(f"  Замер {j+1}: Скорость = {entry['Скорость (м/с)'][j]}, Время = {entry['Время (с)'][j]}")
