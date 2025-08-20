import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image

# Set Seaborn style
sns.set_style("whitegrid")
sns.set_context("talk")

# Create synthetic dataset
np.random.seed(42)
n = 300
df = pd.DataFrame({
    "Customer Segment": np.random.choice(["Premium", "Standard", "Budget"], size=n),
    "Purchase Amount": np.concatenate([
        np.random.normal(500, 50, 100),
        np.random.normal(300, 40, 100),
        np.random.normal(150, 30, 100)
    ])
})

# Create the plot (figsize in inches)
fig = plt.figure(figsize=(8, 8), dpi=64)  # 8*64 = 512
sns.boxplot(data=df, x="Customer Segment", y="Purchase Amount", palette="Set2")

# Add titles and labels
plt.title("Purchase Amount Distribution by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Purchase Amount ($)")

# Save without bbox trimming
temp_file = "chart_temp.png"
fig.savefig(temp_file, dpi=64)  # Might be slightly off

# ✅ Resize to exactly 512x512 using Pillow
img = Image.open(temp_file)
img = img.resize((512, 512))
img.save("chart.png")
