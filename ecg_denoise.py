import pandas as pd
import matplotlib.pyplot as plt

def get_denoised_ecg_signal(file_path, column_name, window_size):
    """
    reads a CSV file and gives a denoised signal using the moving average signal processing algorithm.

    args:
        file_path (str): The path to the csv file.
        column_name (str): The name of the column to plot.
        window_size (int): The number of data points to include in the moving average (here 50k for 50 hertz).
    """
    try:
        df = pd.read_csv(file_path)

        if column_name not in df.columns:
            print(f"error: column '{column_name}' not found in the csv file.")
            return

        data = df[column_name]

        denoised_signal = data.rolling(window=window_size, center=True).mean()

        plt.figure(figsize=(12, 6))
        plt.plot(data, label='original signal', alpha=0.5)
        plt.plot(
            denoised_signal,
            label='denoised ecg Signal',
            color='red',
            linewidth=2
        )

        plt.title('original and denoised ecg signal')
        plt.xlabel('index')
        plt.ylabel('value')
        plt.legend()
        plt.grid(True)
        plt.show()

    except FileNotFoundError:
        print(f"error: The file at '{file_path}' was not found.")
    except Exception as e:
        print(f"an error occurred: {e}")

get_denoised_ecg_signal('column3.csv', 'Column3', window_size=50000)