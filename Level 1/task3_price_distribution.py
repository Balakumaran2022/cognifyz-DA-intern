import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for professional look
sns.set_style("whitegrid")
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

# 1. Load the dataset
script_dir = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(os.path.dirname(script_dir), 'Dataset .csv')
df = pd.read_csv(dataset_path)

# 2. Get counts and calculate percentages
price_counts = df['Price range'].value_counts().sort_index()
total_restaurants = len(df)
price_pcts = (price_counts / total_restaurants) * 100

print("="*60)
print("     LEVEL 1 - TASK 3: PRICE RANGE DISTRIBUTION ANALYSIS     ")
print("="*60)
print(f"Total restaurants in the dataset: {total_restaurants}")
print("-"*60)
print("Distribution of price ranges:")
price_labels = {1: 'Low (1)', 2: 'Medium (2)', 3: 'High (3)', 4: 'Very High (4)'}
for price_val, count in price_counts.items():
    pct = price_pcts[price_val]
    label = price_labels.get(price_val, str(price_val))
    print(f" Price Range {price_val} ({label:<11}) | Count: {count:<5} | Percentage: {pct:.2f}%")
print("="*60)

# 3. Create a beautiful styled bar chart
fig, ax = plt.subplots(figsize=(8, 5.5))

# Premium color palette using styled HSL-tailored colors
colors = ["#4A90E2", "#50E3C2", "#F5A623", "#D9534F"]

bars = ax.bar([price_labels[k] for k in price_counts.index], price_counts.values, color=colors, width=0.5, edgecolor='none')

# Add values and percentages on top of the bars
for bar in bars:
    height = bar.get_height()
    pct = (height / total_restaurants) * 100
    ax.text(bar.get_x() + bar.get_width()/2.0, height + (max(price_counts.values) * 0.015), 
            f'{int(height):,}\n({pct:.2f}%)', 
            ha='center', va='bottom', fontsize=11, fontweight='semibold', color='#333333')

# Style the chart
ax.set_title("Distribution of Restaurant Price Ranges", fontsize=15, fontweight='bold', pad=25, color='#222222')
ax.set_xlabel("Price Range Category", fontsize=12, fontweight='bold', labelpad=12, color='#444444')
ax.set_ylabel("Number of Restaurants", fontsize=12, fontweight='bold', labelpad=12, color='#444444')
ax.set_ylim(0, max(price_counts.values) * 1.15) # Leave space for labels
ax.tick_params(axis='x', labelsize=11)
ax.tick_params(axis='y', labelsize=11)

sns.despine(left=True, bottom=True)
plt.tight_layout()

# Save
output_image = os.path.join(script_dir, 'task3_price_distribution.png')
plt.savefig(output_image, dpi=300)
print(f"Visual representation saved successfully at:\n {output_image}\n")
print("="*60)
