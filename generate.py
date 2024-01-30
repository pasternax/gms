import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

coordinates = [
    {"X": 0, "Y": 0},
    {"X": 20, "Y": 20},
    {"X": 70, "Y": 90},
    {"X": 90, "Y": 80},
    {"X": 10, "Y": 90}
]

def generate_data(num_sets, num_points):
    data = []

    for i in range(1, num_sets + 1):
        speeds = [np.random.uniform(1400, 2500) for _ in range(num_points)]
        times = [np.random.uniform(10, 100) for _ in range(num_points)]

        data.extend(
            [{"Буровая установка": i, "Скорость (м/с)": speed, "Время (с)": time,
              "X": coordinates[i - 1]["X"], "Y": coordinates[i - 1]["Y"]}
             for speed, time in zip(speeds, times)]
        )
    return pd.DataFrame(data)

def add_z_coordinate(df, initial_z=0, increase_by=20):
    df['Z'] = initial_z
    df['Z'] += increase_by

def plot_3d_map(ax, ground_x, ground_y, ground_z, df):
    ax.plot_surface(ground_x, ground_y, ground_z, alpha=0.5, cmap='terrain')
    
    for _, row in df.groupby('Буровая установка').head(1).iterrows():
        z_coordinate = ground_z[int(row['Y'] / 100 * len(ground_y)),
                                 int(row['X'] / 100 * len(ground_x))]
        ax.scatter(row['X'], row['Y'], z_coordinate,
                   label=f'Буровая {row["Буровая установка"]}')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()

def main():
    num_sets = 5
    num_points = 5

    df = generate_data(num_sets, num_points)

    add_z_coordinate(df, increase_by=20)

    file_path = "Data/data.xlsx"
    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
        for name, group in df.groupby('Буровая установка'):
            group.drop('Буровая установка', axis=1).to_excel(writer, sheet_name=f'Буровая_{name}', index=False)

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    ground_x = np.linspace(0, 100, 100)
    ground_y = np.linspace(0, 100, 100)
    ground_x, ground_y = np.meshgrid(ground_x, ground_y)

    flat_field = np.zeros_like(ground_x)
    mountain_center_shifted = np.exp(-((ground_x - 10) ** 2 + (ground_y - 10) ** 2) / (20 * 100)) * 60
    ground_z = flat_field + mountain_center_shifted

    plot_3d_map(ax, ground_x, ground_y, ground_z, df)

    plt.title('3D Карта с буровыми установками')
    plt.show()

if __name__ == "__main__":
    main()
