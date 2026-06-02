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

# 2. Identify the city with the highest number of restaurants
city_counts = df['City'].value_counts()
top_city = city_counts.index[0]
top_city_count = city_counts.values[0]

# 3. Calculate average rating for restaurants in each city
city_avg_ratings = df.groupby('City')['Aggregate rating'].mean()

# 4. Determine the city with the highest average rating
# Note: A city with very few restaurants can have a high average rating by chance.
# Let's find:
# A) The absolute highest average rating city
absolute_best_city = city_avg_ratings.idxmax()
absolute_best_rating = city_avg_ratings.max()

# B) The highest average rating city among those with a substantial number of restaurants (e.g. at least 10 restaurants)
min_restaurants = 10
substantial_cities = city_counts[city_counts >= min_restaurants].index
if len(substantial_cities) > 0:
    substantial_avg_ratings = city_avg_ratings[substantial_cities]
    best_substantial_city = substantial_avg_ratings.idxmax()
    best_substantial_rating = substantial_avg_ratings.max()
else:
    best_substantial_city = absolute_best_city
    best_substantial_rating = absolute_best_rating

print("="*60)
print("          LEVEL 1 - TASK 2: CITY ANALYSIS          ")
print("="*60)
print(f"City with the HIGHEST NUMBER of restaurants:")
print(f"  -> {top_city}: {top_city_count:,} restaurants")
print("-"*60)
print(f"City with the ABSOLUTE HIGHEST AVERAGE RATING:")
print(f"  -> {absolute_best_city}: {absolute_best_rating:.2f} rating (out of {city_counts[absolute_best_city]} restaurant(s))")
if best_substantial_city != absolute_best_city:
    print(f"City with highest average rating (min {min_restaurants} restaurants):")
    print(f"  -> {best_substantial_city}: {best_substantial_rating:.2f} rating (out of {city_counts[best_substantial_city]} restaurants)")
print("="*60)

# Create a beautiful plot comparing top 10 cities by restaurant count and their average ratings
top_10_cities = city_counts.head(10).index
top_10_df = df[df['City'].isin(top_10_cities)].copy()
# Reorder by top_10_cities frequency order
top_10_avg_ratings = top_10_df.groupby('City')['Aggregate rating'].mean().loc[top_10_cities]

fig, ax1 = plt.subplots(figsize=(11, 6))

# Plot number of restaurants on primary axis
color_bar = '#6C5B7B'  # Deep Muted Purple
bars = ax1.bar(top_10_cities, city_counts.head(10).values, color=color_bar, alpha=0.8, width=0.45, label='Number of Restaurants')
ax1.set_ylabel('Number of Restaurants', color=color_bar, fontsize=12, fontweight='bold')
ax1.tick_params(axis='y', labelcolor=color_bar)
ax1.set_xticks(range(len(top_10_cities)))
ax1.set_xticklabels(top_10_cities, rotation=35, ha='right', fontsize=11, fontweight='semibold')
ax1.set_xlabel('City', fontsize=12, fontweight='bold', labelpad=10)

# Plot average rating on secondary axis
ax2 = ax1.twinx()
color_line = '#D9534F'  # Crimson Red
ax2.plot(top_10_cities, top_10_avg_ratings.values, color=color_line, marker='o', linewidth=3, markersize=8, label='Average Rating')
ax2.set_ylabel('Average Rating (0-5)', color=color_line, fontsize=12, fontweight='bold')
ax2.tick_params(axis='y', labelcolor=color_line)
ax2.set_ylim(0, 5.0)

# Title
plt.title("Top 10 Cities: Restaurant Volume vs. Average Rating", fontsize=15, fontweight='bold', pad=20, color='#333333')

# Annotate value labels
# Calculate vertical offsets based on data scale
max_val = city_counts.head(10).max()
offset = max_val * 0.015

for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2.0, yval + offset, f'{int(yval):,}', ha='center', va='bottom', fontsize=10, fontweight='semibold', color='#333333')

for i, val in enumerate(top_10_avg_ratings.values):
    ax2.text(i, val + 0.15, f'{val:.2f}', ha='center', va='bottom', fontsize=10, fontweight='bold', color=color_line)

sns.despine(top=True, left=False, right=False)
plt.tight_layout()

# Save
output_image = os.path.join(script_dir, 'task2_city_analysis.png')
plt.savefig(output_image, dpi=300)
print(f"Visual representation saved successfully at:\n {output_image}\n")
print("="*60)
