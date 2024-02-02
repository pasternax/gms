import numpy as np
import pandas as pd

points_file = "data/hark_kr.txt"  # файл с координатами плоскости
drill_file_excel = "data/pick_from_petrel.xlsx"  # файл с координатами буровых в формате Excel

points_data = np.loadtxt(points_file, delimiter='\t')
plane_points = points_data[:, :3]

drill_data_excel = pd.read_excel(drill_file_excel)

drill_coordinates = drill_data_excel.iloc[:, 1:4].values

closest_points = []

for drill_coord in drill_coordinates:
    distances = np.dot(plane_points - drill_coord, [0, 0, -1])
    closest_point_index = np.argmin(distances)
    closest_points.append(plane_points[closest_point_index])

closest_points = np.array(closest_points)

# Рассчитайте расстояние и время
distances = np.linalg.norm(closest_points - drill_coordinates, axis=1)
times = drill_data_excel.iloc[:, 3].values  # предполагаем, что время указано в четвертом столбце файла с буровыми установками

# Рассчитайте скорость
speeds = distances / times

# Выведите результаты
for i in range(len(drill_data_excel)):
    print(f"Для буровой установки {i+1}: Скорость = {speeds[i]} м/с")
