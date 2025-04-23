# Importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

# 1. Create a NumPy array of numbers from 1 to 10 and calculate the mean
array = np.arange(1, 11)
mean_value = np.mean(array)
print("NumPy Array:", array)
print("Mean of the array:", mean_value)

# 2. Load a small dataset into a pandas DataFrame and display summary statistics
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'Score': [88, 92, 85, 90, 95]
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)
print("\nSummary Statistics:")
print(df.describe(include='all'))  # Includes all columns

# 3. Fetch data from a public API using requests and print a key piece of information
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()
    bitcoin_price_usd = data['bpi']['USD']['rate']
    print("\nCurrent Bitcoin Price in USD:", bitcoin_price_usd)
except requests.exceptions.RequestException as e:
    print("\nFailed to fetch data from the API. Error:", e)

# 4. Plot a simple line graph using matplotlib
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure(figsize=(8, 4))
plt.plot(x, y, marker='o', linestyle='-', color='blue', label='y = 2x')
plt.title('Simple Line Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
