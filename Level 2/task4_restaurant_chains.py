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

# 2. Group by restaurant name to identify chains
chain_stats = df.groupby('Restaurant Name').agg(
    Outlets=('Restaurant ID', 'count'),
    AvgRating=('Aggregate rating', 'mean'),
    TotalVotes=('Votes', 'sum')
)

# Filter for names that have more than 1 outlet (actual chains)
chains = chain_stats[chain_stats['Outlets'] > 1].sort_values(by='Outlets', ascending=False)

print("="*75)
print("             LEVEL 2 - TASK 4: RESTAURANT CHAINS ANALYSIS             ")
print("="*75)
print(f"Total unique restaurant names in dataset: {df['Restaurant Name'].nunique():,}")
print(f"Total restaurant chains identified (outlets > 1): {len(chains):,}")
print("-"*75)
print("Top 10 Largest Restaurant Chains (by Outlets count):")
print(f" {'Restaurant Name':<28} | Outlets | Avg Rating | Total Votes")
print("-" * 75)
top_10_largest = chains.head(10)
for name, row in top_10_largest.iterrows():
    print(f" {name:<28} | {int(row['Outlets']):<7} | {row['AvgRating']:.2f} / 5.0 | {int(row['TotalVotes']):,}")
print("-"*75)
print("Top 10 Most Popular Chains (by Total Votes):")
print(f" {'Restaurant Name':<28} | Outlets | Avg Rating | Total Votes")
print("-" * 75)
top_10_popular = chains.sort_values(by='TotalVotes', ascending=False).head(10)
for name, row in top_10_popular.iterrows():
    print(f" {name:<28} | {int(row['Outlets']):<7} | {row['AvgRating']:.2f} / 5.0 | {int(row['TotalVotes']):,}")
print("="*75)

# 3. Create visual representation
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6.5))

# Plot 1: Top 10 Largest Chains (Outlets)
colors_largest = sns.color_palette("autumn_r", len(top_10_largest))
bars1 = ax1.barh(top_10_largest.index[::-1], top_10_largest['Outlets'][::-1], color=colors_largest[::-1], height=0.55)
ax1.set_title("Top 10 Largest Restaurant Chains (by Outlets)", fontsize=13, fontweight='bold', pad=15)
ax1.set_xlabel("Number of Outlets", fontsize=11, fontweight='semibold')
ax1.set_ylabel("Chain Name", fontsize=11, fontweight='semibold')

for bar in bars1:
    width = bar.get_width()
    ax1.text(width + 0.5, bar.get_y() + bar.get_height()/2, f'{int(width)}', 
             va='center', ha='left', fontsize=10, fontweight='semibold', color='#333333')

# Plot 2: Top 10 Most Popular Chains (Total Votes)
colors_popular = sns.color_palette("winter_r", len(top_10_popular))
bars2 = ax2.barh(top_10_popular.index[::-1], top_10_popular['TotalVotes'][::-1], color=colors_popular[::-1], height=0.55)
ax2.set_title("Top 10 Most Popular Chains (by Total Votes)", fontsize=13, fontweight='bold', pad=15)
ax2.set_xlabel("Total Votes Count", fontsize=11, fontweight='semibold')

for bar in bars2:
    width = bar.get_width()
    ax2.text(width + (max(top_10_popular['TotalVotes']) * 0.015), bar.get_y() + bar.get_height()/2, f'{int(width):,}', 
             va='center', ha='left', fontsize=10, fontweight='bold', color='#333333')

sns.despine(left=True, bottom=True)
plt.tight_layout()

# Save
output_image = os.path.join(script_dir, 'task4_restaurant_chains.png')
plt.savefig(output_image, dpi=300)
print(f"Visual representation saved successfully at:\n {output_image}\n")
print("="*75)
