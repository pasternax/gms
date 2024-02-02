import pandas as pd

# Укажите путь к вашему текстовому файлу
txt = 'Data/pick_from_petrel.txt'

# Прочитайте первую строку текстового файла, чтобы получить заголовки
with open(txt, 'r') as file:
    first_line = file.readline().strip()

# Разделите первую строку для получения имен столбцов
column_names = first_line.split()

# Read the text file into a DataFrame using pandas с именами столбцов
df = pd.read_csv(txt, delimiter='\s+', names=column_names, skiprows=1)

# Укажите путь для сохранения Excel файла
excel = 'Data/pick_from_petrel.xlsx'

# Сохраните DataFrame в Excel файл
df.to_excel(excel, index=False)
