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

# 2. Analyze rating distribution
# Let's bin the ratings using pd.cut. 
# Since many ratings are exactly 0.0 (unrated), and others range from 1.0 to 5.0, 
# let's create a clear binning system.
bins = [-0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.1]
labels = ['0.0-0.5', '0.5-1.0', '1.0-1.5', '1.5-2.0', '2.0-2.5', '2.5-3.0', '3.0-3.5', '3.5-4.0', '4.0-4.5', '4.5-5.0']
df['Rating Range'] = pd.cut(df['Aggregate rating'], bins=bins, labels=labels)

range_counts = df['Rating Range'].value_counts().sort_index()
most_common_range = range_counts.idxmax()
most_common_count = range_counts.max()
most_common_pct = (most_common_count / len(df)) * 100

# Calculate average number of votes
avg_votes = df['Votes'].mean()

print("="*60)
print("          LEVEL 2 - TASK 1: RESTAURANT RATINGS          ")
print("="*60)
print(f"Total restaurants in the dataset: {len(df)}")
print("-"*60)
print("Distribution of ratings across ranges:")
for r, count in range_counts.items():
    pct = (count / len(df)) * 100
    print(f" Rating Range {r:<7} | Count: {count:<5} | Percentage: {pct:.2f}%")
print("-"*60)
print(f"Most common rating range: {most_common_range} ({most_common_count} restaurants, {most_common_pct:.2f}%)")
print(f"Average number of votes received: {avg_votes:.2f} votes per restaurant")
print("="*60)

# 3. Create a beautiful visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Subplot 1: Distribution of Ratings (KDE + Histogram)
sns.histplot(df['Aggregate rating'], bins=20, kde=True, color='#4A90E2', ax=ax1, edgecolor='none', alpha=0.7)
ax1.set_title("Distribution of Aggregate Ratings", fontsize=14, fontweight='bold', pad=15)
ax1.set_xlabel("Aggregate Rating (0 - 5)", fontsize=11, fontweight='semibold')
ax1.set_ylabel("Number of Restaurants", fontsize=11, fontweight='semibold')

# Draw a vertical line for mean rating
mean_rating = df['Aggregate rating'].mean()
ax1.axvline(mean_rating, color='#D9534F', linestyle='--', linewidth=2, label=f'Mean Rating: {mean_rating:.2f}')
ax1.legend(fontsize=10)

# Subplot 2: Bar plot of Rating Ranges
# Generate colors and highlight the most common range
palette = sns.color_palette("Blues_d", len(range_counts))
colors = [palette[i] for i in range(len(range_counts))]
max_idx = list(range_counts.index).index(most_common_range)
colors[max_idx] = '#D9534F' # Highlight the most common rating range in Crimson Red

bars = ax2.bar(range_counts.index, range_counts.values, color=colors, edgecolor='none', width=0.6)
ax2.set_title("Frequency by Rating Range", fontsize=14, fontweight='bold', pad=15)
ax2.set_xlabel("Rating Range", fontsize=11, fontweight='semibold')
ax2.set_ylabel("Number of Restaurants", fontsize=11, fontweight='semibold')
ax2.set_xticks(range(len(range_counts)))
ax2.set_xticklabels(range_counts.index, rotation=35, ha='right', fontsize=10, fontweight='semibold')

# Add values on top of bars
offset = max(range_counts.values) * 0.015
for bar in bars:
    height = bar.get_height()
    if height > 0:
        ax2.text(bar.get_x() + bar.get_width()/2.0, height + offset, 
                f'{int(height):,}', 
                ha='center', va='bottom', fontsize=9, fontweight='semibold', color='#333333')

sns.despine(left=True, bottom=True)
plt.tight_layout()

# Save
output_image = os.path.join(script_dir, 'task1_restaurant_ratings.png')
plt.savefig(output_image, dpi=300)
print(f"Visual representation saved successfully at:\n {output_image}\n")
print("="*60)
