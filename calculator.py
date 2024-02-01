import pandas as pd
import numpy as np

file_path = 'Data/data2.xlsx'

xls = pd.ExcelFile(file_path)

output_file_path = 'Data/results.xlsx'
writer = pd.ExcelWriter(output_file_path, engine='xlsxwriter')


for sheet_name in xls.sheet_names:
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    data_time = df.iloc[0:5, 1].values
    data_time2 = [None] * len(df.index )

    data_h = df.iloc[0:5, 0]

    for i in range(0, len(df.index)):
        if (i==0):
            data_time2[i] = data_time[i]
        else:
            data_time2[i] = data_time[i] - data_time[i-1]

    #print(data_time2)
    matrix_time = (np.tri(5,5) * data_time2)
    ans = np.linalg.solve(matrix_time, data_h)
    print(ans)
    

writer._save()

print(f"Результаты сохранены в файл: {output_file_path}")
