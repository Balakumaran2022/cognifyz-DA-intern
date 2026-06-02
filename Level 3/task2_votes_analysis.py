import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Force stdout to use UTF-8 to prevent UnicodeEncodeErrors on Windows terminals
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Set style for professional look
sns.set_style("whitegrid")
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

# 1. Load the dataset
script_dir = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(os.path.dirname(script_dir), 'Dataset .csv')
df = pd.read_csv(dataset_path)

# 2. Identify highest and lowest number of votes
max_votes_row = df.loc[df['Votes'].idxmax()]
min_votes_val = df['Votes'].min()
min_votes_count = len(df[df['Votes'] == min_votes_val])
min_votes_sample = df[df['Votes'] == min_votes_val].head(5)

# Calculate correlation between votes and rating
correlation = df['Votes'].corr(df['Aggregate rating'])

print("="*65)
print("             LEVEL 3 - TASK 2: VOTES ANALYSIS             ")
print("="*65)
print("Restaurant with the HIGHEST number of votes:")
print(f"  -> Name:       {max_votes_row['Restaurant Name']}")
print(f"  -> City:       {max_votes_row['City']}")
print(f"  -> Votes:      {int(max_votes_row['Votes']):,}")
print(f"  -> Rating:     {max_votes_row['Aggregate rating']} / 5.0")
print("-"*65)
print(f"Restaurants with the LOWEST number of votes ({min_votes_val} votes):")
print(f"  -> Total restaurants with {min_votes_val} votes: {min_votes_count:,}")
print("  -> Sample restaurants with lowest votes:")
for idx, row in min_votes_sample.iterrows():
    # Clean any special characters if printing fails, or rely on sys.stdout encoding
    try:
        print(f"     * {row['Restaurant Name']} ({row['City']}) - Rating: {row['Aggregate rating']}")
    except Exception:
        # Fallback to ascii representation in case of unexpected errors
        clean_name = str(row['Restaurant Name']).encode('ascii', 'replace').decode('ascii')
        clean_city = str(row['City']).encode('ascii', 'replace').decode('ascii')
        print(f"     * {clean_name} ({clean_city}) - Rating: {row['Aggregate rating']}")
print("-"*65)
print(f"Correlation between Votes and Aggregate Rating: {correlation:.4f}")
if correlation > 0.3:
    print("  -> Interpretation: Moderate/strong positive relationship (more votes = higher rating).")
elif correlation > 0.1:
    print("  -> Interpretation: Weak positive relationship (more votes tend to align with slightly higher rating).")
else:
    print("  -> Interpretation: No significant linear relationship.")
print("="*65)

# 3. Create visual representation
fig, ax = plt.subplots(figsize=(9, 6.5))

# Plot votes vs rating with trendline
sns.regplot(data=df, x='Aggregate rating', y='Votes', color='#4A90E2', 
            scatter_kws={'alpha':0.4, 's':15, 'edgecolor':'none'},
            line_kws={'color':'#D9534F', 'linewidth':2.5, 'label':f'Trendline (r = {correlation:.2f})'}, ax=ax)

ax.set_title("Relationship between Restaurant Ratings and Votes", fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel("Aggregate Rating (0 - 5)", fontsize=11, fontweight='semibold', labelpad=10)
ax.set_ylabel("Number of Votes", fontsize=11, fontweight='semibold', labelpad=10)
ax.legend(fontsize=11)

sns.despine(left=True, bottom=True)
plt.tight_layout()

# Save
output_image = os.path.join(script_dir, 'task2_votes_analysis.png')
plt.savefig(output_image, dpi=300)
print(f"Visual representation saved successfully at:\n {output_image}\n")
print("="*65)
