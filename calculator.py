import pandas as pd

file_path = 'Data/data.xlsx'  # Замените на путь к вашему файлу
xls = pd.ExcelFile(file_path)

result_data = []

for sheet_name in xls.sheet_names:
    df = xls.parse(sheet_name)

    speed_column = 'Скорость (м/с)'
    time_column = 'Время (с)'

    df[speed_column] = pd.to_numeric(df[speed_column], errors='coerce')
    df[time_column] = pd.to_numeric(df[time_column], errors='coerce')

    df['Расстояние (м)'] = df[speed_column] * df[time_column]

    result_data.append(df)

result_file_path = 'Data/results.xlsx'
with pd.ExcelWriter(result_file_path, engine='xlsxwriter') as writer:
    for i, result_df in enumerate(result_data):
        result_df.to_excel(writer, sheet_name=f'Буровая_{i + 1}', index=False)
