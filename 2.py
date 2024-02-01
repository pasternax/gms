import pandas as pd
import numpy as np

df = pd.read_excel('Data/results.xlsx')

data_time = df.iloc[0:5, 1].values
data_time2 = [None] * len(df.index )

data_h = df.iloc[0:5, 0]


for i in range(0, len(df.index)):
    if (i==0):
        data_time2[i] = data_time[i]
    else:
        data_time2[i] = data_time[i] - data_time[i-1]

print(data_time2)

matrix_time = (np.tri(5,5) * data_time2)

ans = np.linalg.solve(matrix_time, data_h)
print(ans)