import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for premium/professional look
sns.set_style("whitegrid")
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

# 1. Load the dataset
# The script is in "Level 1" folder, so we load the CSV from parent folder
script_dir = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(os.path.dirname(script_dir), 'Dataset .csv')

if not os.path.exists(dataset_path):
    raise FileNotFoundError(f"Dataset file not found at: {dataset_path}")

df = pd.read_csv(dataset_path)

# Clean missing values in Cuisines
df_clean = df.dropna(subset=['Cuisines']).copy()

# 2. Extract and count individual cuisines
# A restaurant can have multiple cuisines separated by commas.
all_cuisines = df_clean['Cuisines'].apply(lambda x: [c.strip() for c in str(x).split(',') if c.strip()]).explode()

# Get total number of restaurants for percentage calculation
total_restaurants = len(df)

# Count occurrences of each cuisine
cuisine_counts = all_cuisines.value_counts()
top_3_cuisines = cuisine_counts.head(3)

print("="*60)
print("          LEVEL 1 - TASK 1: TOP CUISINES ANALYSIS          ")
print("="*60)
print(f"Total restaurants in the dataset: {total_restaurants}")
print("-"*60)
print("Top 3 most common cuisines and their percentages:")
for rank, (cuisine, count) in enumerate(top_3_cuisines.items(), 1):
    percentage = (count / total_restaurants) * 100
    print(f" {rank}. {cuisine:<12} | Count: {count:<5} | Percentage: {percentage:.2f}%")
print("="*60)

# 3. Create a beautiful horizontal bar chart
fig, ax = plt.subplots(figsize=(9, 5))
colors = ["#4A90E2", "#50E3C2", "#F5A623"] # Sleek modern color palette

# Plot in reverse order so the highest is at the top
y_positions = range(len(top_3_cuisines))
bars = ax.barh(y_positions, top_3_cuisines.values[::-1], color=colors[::-1], height=0.55, edgecolor='none')

# Style the chart
ax.set_yticks(y_positions)
ax.set_yticklabels(top_3_cuisines.index[::-1], fontsize=12, fontweight='semibold')
ax.set_title("Top 3 Most Common Cuisines", fontsize=15, fontweight='bold', pad=20, color='#333333')
ax.set_xlabel("Number of Restaurants", fontsize=12, labelpad=10, color='#555555')
ax.set_xlim(0, max(top_3_cuisines.values) * 1.15) # Leave room for labels

# Add value and percentage annotations on the bars
for bar in bars:
    width = bar.get_width()
    pct = (width / total_restaurants) * 100
    ax.text(width + 30, bar.get_y() + bar.get_height()/2, 
            f'{int(width):,} ({pct:.2f}%)', 
            va='center', ha='left', fontsize=11, fontweight='semibold', color='#444444')

# Despine and clean layout
sns.despine(left=True, bottom=True)
plt.tight_layout()

# Save the visualization
output_image = os.path.join(script_dir, 'task1_top_cuisines.png')
plt.savefig(output_image, dpi=300)
print(f"Visual representation saved successfully at:\n {output_image}\n")
print("="*60)
