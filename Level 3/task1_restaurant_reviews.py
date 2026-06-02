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

# 2. Classify reviews and analyze keywords
# 'Rating text' represents the qualitative review in this dataset.
# Positive reviews: 'Excellent', 'Very Good', 'Good'
# Negative reviews: 'Poor', 'Average' (Neutral/Negative qualitative feedback)
# Unrated: 'Not rated'

positive_reviews = df[df['Rating text'].isin(['Excellent', 'Very Good', 'Good'])]['Rating text']
negative_reviews = df[df['Rating text'].isin(['Poor', 'Average'])]['Rating text']

# Simple keyword frequency analysis
pos_keywords = {}
for rev in positive_reviews:
    for word in str(rev).split():
        word = word.lower()
        pos_keywords[word] = pos_keywords.get(word, 0) + 1

neg_keywords = {}
for rev in negative_reviews:
    for word in str(rev).split():
        word = word.lower()
        neg_keywords[word] = neg_keywords.get(word, 0) + 1

# Sort keywords by count
pos_keywords_sorted = sorted(pos_keywords.items(), key=lambda x: x[1], reverse=True)
neg_keywords_sorted = sorted(neg_keywords.items(), key=lambda x: x[1], reverse=True)

# 3. Calculate review length and relationship with rating
df['Review Length'] = df['Rating text'].apply(lambda x: len(str(x)))
avg_len = df['Review Length'].mean()
correlation = df['Review Length'].corr(df['Aggregate rating'])

print("="*65)
print("             LEVEL 3 - TASK 1: RESTAURANT REVIEWS             ")
print("="*65)
print("Most common keywords in POSITIVE reviews:")
for k, count in pos_keywords_sorted[:5]:
    print(f"  -> '{k}': {count} times")
print("-"*65)
print("Most common keywords in NEGATIVE/AVERAGE reviews:")
for k, count in neg_keywords_sorted[:5]:
    print(f"  -> '{k}': {count} times")
print("-"*65)
print(f"Average length of qualitative review strings: {avg_len:.2f} characters")
print(f"Correlation between Review Length and Aggregate Rating: {correlation:.4f}")
print("="*65)

# 4. Create visual representation
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6.5))

# Plot 1: Keyword Frequencies in Reviews
# Combine keywords for visualization
pos_words = [x[0].capitalize() for x in pos_keywords_sorted[:3]]
pos_counts = [x[1] for x in pos_keywords_sorted[:3]]
neg_words = [x[0].capitalize() for x in neg_keywords_sorted[:2]]
neg_counts = [x[1] for x in neg_keywords_sorted[:2]]

all_words = pos_words + neg_words
all_counts = pos_counts + neg_counts
colors_word = ['#50E3C2', '#50E3C2', '#50E3C2', '#D9534F', '#D9534F'] # Soft Teal (Positive), Crimson Red (Negative)

bars1 = ax1.bar(all_words, all_counts, color=colors_word, width=0.5, edgecolor='none')
ax1.set_title("Frequency of Qualitative Review Keywords", fontsize=13, fontweight='bold', pad=15)
ax1.set_ylabel("Occurrences", fontsize=11, fontweight='semibold')
ax1.set_xlabel("Keywords (Teal = Positive, Red = Negative)", fontsize=11, fontweight='semibold', labelpad=10)

# Add values on top of bars
for bar in bars1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2.0, height + (max(all_counts) * 0.015), 
             f'{int(height):,}', 
             ha='center', va='bottom', fontsize=10, fontweight='semibold', color='#333333')

# Plot 2: Relationship between Review Length and Average Rating
# Group by Review Length and calculate average rating
length_grouped = df.groupby('Review Length')['Aggregate rating'].mean().sort_index()

bars2 = ax2.bar(length_grouped.index.astype(str), length_grouped.values, color='#4A90E2', width=0.45, edgecolor='none')
ax2.set_title("Review Length vs. Average Rating", fontsize=13, fontweight='bold', pad=15)
ax2.set_xlabel("Review String Length (Characters)", fontsize=11, fontweight='semibold', labelpad=10)
ax2.set_ylabel("Average Rating (0 - 5)", fontsize=11, fontweight='semibold')
ax2.set_ylim(0, 5.0)

# Add values on top of bars
for bar in bars2:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2.0, height + 0.1, 
             f'{height:.2f}', 
             ha='center', va='bottom', fontsize=10, fontweight='bold', color='#444444')

sns.despine(left=True, bottom=True)
plt.tight_layout()

# Save
output_image = os.path.join(script_dir, 'task1_restaurant_reviews.png')
plt.savefig(output_image, dpi=300)
print(f"Visual representation saved successfully at:\n {output_image}\n")
print("="*65)
