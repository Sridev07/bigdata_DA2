# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import minmax_scale
import matplotlib.pyplot as plt
from minisom import MiniSom
data = pd.read_csv("C:\\Users\\Parth\\Downloads\\digital_wallet_transactions.csv")
print(data.head())  # Print the first few rows of the dataset
print(data['transaction_status'].unique())  # Check unique values in the transaction_status column
data_numeric = data.select_dtypes(include=[np.number])  # Keep only numeric columns
data_normalized = minmax_scale(data_numeric.values)
som_shape = (10, 10)  # Define the shape of your SOM grid
som = MiniSom(x=som_shape[0], y=som_shape[1], input_len=data_normalized.shape[1], sigma=1.0, learning_rate=0.5, random_seed=42)
som.random_weights_init(data_normalized)
som.train_random(data_normalized, 100)  # Number of iterations can be adjusted
plt.figure(figsize=(10, 8))
plt.title('SOM Clustering of digital wallet transaction')
distance_map = som.distance_map().T  # Transpose for correct orientation
plt.pcolor(distance_map, cmap='coolwarm')  # Plot heatmap
plt.colorbar()  # Color bar for heatmap
try:
    transaction_status = data['transaction_status'].values  # Ensure this matches your dataset
    markers = {'Successful': 's', 'Pending': 'o', 'Failed': 'o'}  # Squares for successful, circles for pending/failed
    colors = {'Successful': 'g', 'Pending': 'r', 'Failed': 'r'}    # Green for successful, red for pending/failed
    for i, x in enumerate(data_normalized):
        w = som.winner(x)  # Get the winning node
        status = transaction_status[i]

        # Debugging: Print out the index and corresponding transaction status
        print(f"Index: {i}, Status: {status}, Coordinates: {w}")
        plt.plot(w[0] + 0.5, w[1] + 0.5,
                 markers[status],  # Select marker based on transaction status
                 markerfacecolor='None',
                 markeredgecolor=colors[status],  # Select color based on transaction status
                 markersize=12, markeredgewidth=2)

except KeyError:
    print("No transaction status column found. Visualizing without markers.")
except Exception as e:
    print(f"An error occurred: {e}")
plt.show()
