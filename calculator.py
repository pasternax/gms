import pandas as pd

file_path = 'Data/data.xlsx'

xls = pd.ExcelFile(file_path)

output_file_path = 'Data/results.xlsx'
writer = pd.ExcelWriter(output_file_path, engine='xlsxwriter')


for sheet_name in xls.sheet_names:
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    df['Расстояние'] = df['Скорость (м/с)'] * df['Время (с)']
    df.to_excel(writer, sheet_name=sheet_name, index=False)

writer._save()

print(f"Результаты сохранены в файл: {output_file_path}")
