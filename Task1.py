import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)

# Generate 500 custom individuals
n = 500
ages = np.random.randint(1, 90, size=n)  # ages between 1 and 89
genders = np.random.choice(['Male', 'Female'], size=n, p=[0.52, 0.48])

# Create DataFrame
df = pd.DataFrame({
    'ID': range(1, n + 1),
    'Age': ages,
    'Gender': genders
})

# Save to CSV 
df.to_csv("custom_population_dataset.csv", index=False)

# Histogram of Age Distribution
plt.figure(figsize=(10, 5))
sns.histplot(df['Age'], bins=15, kde=True, color='skyblue')
plt.title("Histogram of Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()

# Bar Chart of Gender Distribution
plt.figure(figsize=(6, 5))
sns.countplot(data=df, x='Gender', palette='pastel')
plt.title("Bar Chart of Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
