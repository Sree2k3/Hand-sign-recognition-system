import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('ACC.csv')

# Extract data for F1-Score and Dataset
f1_score = df['F1_Score']
datasets = df['Dataset']

# Create a bar plot for F1-Score
plt.figure(figsize=(10, 6))
plt.bar(datasets, f1_score, color='skyblue')
plt.xlabel('Datasets')
plt.ylabel('F1-Score')
plt.title('F1-Score for Different Datasets')
plt.grid(axis='y')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()
