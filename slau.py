import pandas as pd
import numpy as np

def calculate_speed_using_linear_system(time_distance_data):
    n = len(time_distance_data) - 1
    
    if n <= 0:
        return []  # Возвращаем пустой список, если нет данных для вычислений
    
    A = np.eye(n) + np.eye(n, k=-1)
    
    B = np.zeros((n, 1))
    for i in range(n):
        delta_time = time_distance_data[i + 1][0] - time_distance_data[i][0]
        delta_distance = time_distance_data[i + 1][1] - time_distance_data[i][1]
        
        if delta_time != 0:
            B[i, 0] = delta_distance / delta_time
        else:
            B[i, 0] = np.nan
    
    try:
        X = np.linalg.solve(A, B)
    except np.linalg.LinAlgError:
        print("Ошибка в вычислениях. Матрица A не обратима.")
        return []

    speeds = X.flatten().tolist()
    return speeds

# Чтение данных из файла Excel
file_path = 'Data/data.xlsx'
df = pd.read_excel(file_path, header=None, names=['Расстояние', 'Время'])

# Преобразование данных в числовые значения
df['Расстояние'] = pd.to_numeric(df['Расстояние'], errors='coerce')
df['Время'] = pd.to_numeric(df['Время'], errors='coerce')

# Удаление строк с NaN значениями в столбцах 'Расстояние' и 'Время'
df = df.dropna(subset=['Расстояние', 'Время'])

# Применение функции для вычисления скоростей
df['Скорость'] = np.nan  # Создаем столбец 'Скорость' с пустыми значениями

for i in range(1, len(df.columns) - 1, 2):
    time_distance_data = df.iloc[:, i-1:i+1].to_numpy()
    
    speeds = calculate_speed_using_linear_system(time_distance_data)
    
    # Заменяем только те строки, где были вычислены скорости
    df.iloc[:len(speeds), i+1] = speeds

# Сохранение измененного DataFrame в тот же файл Excel
output_file_path = 'Data/output_data.xlsx'
df.to_excel(output_file_path, index=False)

print("Готово! Результаты сохранены в файл:", output_file_path)
