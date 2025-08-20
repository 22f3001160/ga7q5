# chart.py

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic customer data
np.random.seed(42)

# Example customer segments
segments = ['Premium', 'Gold', 'Silver', 'Bronze']
data = {
    'Segment': np.random.choice(segments, 400),
    'PurchaseAmount': np.concatenate([
        np.random.normal(500, 50, 100),   # Premium
        np.random.normal(400, 60, 100),   # Gold
        np.random.normal(300, 70, 100),   # Silver
        np.random.normal(200, 80, 100)    # Bronze
    ])
}

df = pd.DataFrame(data)

# Create the figure (512x512 pixels => 8x8 inches at 64 dpi)
plt.figure(figsize=(8, 8))

# Create boxplot
sns.boxplot(data=df, x='Segment', y='PurchaseAmount', palette='pastel')

# Title and labels
plt.title("Customer Purchase Amounts by Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Purchase Amount ($)")

# Save chart as PNG
plt.savefig("chart.png", dpi=64, bbox_inches='tight')
