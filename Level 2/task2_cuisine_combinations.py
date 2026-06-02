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

# Clean missing cuisines
df_clean = df.dropna(subset=['Cuisines']).copy()

# 2. Identify the most common cuisine combinations
combo_counts = df_clean['Cuisines'].value_counts()
top_combos = combo_counts.head(10)

# Calculate average rating for each combination
combo_avg_ratings = df_clean.groupby('Cuisines')['Aggregate rating'].mean().loc[top_combos.index]
global_avg_rating = df_clean['Aggregate rating'].mean()

print("="*65)
print("         LEVEL 2 - TASK 2: CUISINE COMBINATION ANALYSIS         ")
print("="*65)
print(f"Global Average Rating of all restaurants: {global_avg_rating:.2f} / 5.0")
print("-"*65)
print("Top 10 most common cuisine combinations and their average ratings:")
print(f" {'Cuisine Combination':<32} | Count | Avg Rating | vs. Global")
print("-" * 65)
for combo, count in top_combos.items():
    avg_r = combo_avg_ratings[combo]
    diff = avg_r - global_avg_rating
    diff_str = f"+{diff:.2f}" if diff >= 0 else f"{diff:.2f}"
    # Truncate long combo names for tabular view
    display_name = combo[:32] + '...' if len(combo) > 32 else combo
    print(f" {display_name:<32} | {count:<5} | {avg_r:.2f} / 5.0 | {diff_str}")
print("="*65)

# 3. Create visual representation
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6.5))

# Plot counts of top combinations
colors_count = sns.color_palette("Blues_d", len(top_combos))
bars1 = ax1.barh(top_combos.index[::-1], top_combos.values[::-1], color=colors_count[::-1], height=0.55)
ax1.set_title("Top 10 Most Common Cuisine Combinations", fontsize=13, fontweight='bold', pad=15)
ax1.set_xlabel("Number of Restaurants", fontsize=11, fontweight='semibold')
ax1.set_ylabel("Cuisine Combination", fontsize=11, fontweight='semibold')

# Add values on the bars
for bar in bars1:
    width = bar.get_width()
    ax1.text(width + 15, bar.get_y() + bar.get_height()/2, f'{int(width):,}', 
             va='center', ha='left', fontsize=10, fontweight='semibold', color='#333333')

# Plot average ratings of these combinations
# Highlight ratings visually to see if they are high
colors_ratings = sns.color_palette("viridis_r", len(top_combos))
bars2 = ax2.barh(top_combos.index[::-1], combo_avg_ratings.loc[top_combos.index[::-1]], color=colors_ratings[::-1], height=0.55)
ax2.set_title("Average Ratings for Top Combinations", fontsize=13, fontweight='bold', pad=15)
ax2.set_xlabel("Average Rating (0 - 5)", fontsize=11, fontweight='semibold')
ax2.set_xlim(0, 5.0)

# Add vertical line for global average
ax2.axvline(global_avg_rating, color='#D9534F', linestyle='--', linewidth=2, label=f'Global Avg: {global_avg_rating:.2f}')
ax2.legend(loc='lower right', fontsize=10)

# Add values on the ratings bars
for bar in bars2:
    width = bar.get_width()
    ax2.text(width + 0.1, bar.get_y() + bar.get_height()/2, f'{width:.2f}', 
             va='center', ha='left', fontsize=10, fontweight='bold', color='#444444')

sns.despine(left=True, bottom=True)
plt.tight_layout()

# Save
output_image = os.path.join(script_dir, 'task2_cuisine_combinations.png')
plt.savefig(output_image, dpi=300)
print(f"Visual representation saved successfully at:\n {output_image}\n")
print("="*65)
