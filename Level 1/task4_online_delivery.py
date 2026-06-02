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

# 2. Online delivery percentage
delivery_counts = df['Has Online delivery'].value_counts()
total_restaurants = len(df)
delivery_pcts = (delivery_counts / total_restaurants) * 100

yes_count = delivery_counts.get('Yes', 0)
yes_pct = delivery_pcts.get('Yes', 0.0)
no_count = delivery_counts.get('No', 0)
no_pct = delivery_pcts.get('No', 0.0)

# 3. Compare average ratings
avg_ratings = df.groupby('Has Online delivery')['Aggregate rating'].mean()
yes_avg = avg_ratings.get('Yes', 0.0)
no_avg = avg_ratings.get('No', 0.0)

print("="*60)
print("             LEVEL 1 - TASK 4: ONLINE DELIVERY             ")
print("="*60)
print(f"Percentage of restaurants offering online delivery:")
print(f"  -> Yes (Offers Delivery): {yes_count:<5} restaurants ({yes_pct:.2f}%)")
print(f"  -> No  (No Delivery):     {no_count:<5} restaurants ({no_pct:.2f}%)")
print("-"*60)
print(f"Average Ratings comparison:")
print(f"  -> Restaurants with online delivery:    {yes_avg:.2f} / 5.0")
print(f"  -> Restaurants without online delivery: {no_avg:.2f} / 5.0")
diff = yes_avg - no_avg
print(f"  -> Difference: +{diff:.2f} points higher for online delivery!")
print("="*60)

# 4. Create premium dual-plot visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))

# Subplot 1: Donut Chart for Delivery Availability
# Order is No, Yes to align colors nicely
colors_donut = ['#D9534F', '#50E3C2'] # Soft Coral Red (No), Vibrant Mint Green (Yes)
donut_labels = ['No Online Delivery', 'Offers Online Delivery']
donut_sizes = [no_count, yes_count]

# Plot donut
wedges, texts, autotexts = ax1.pie(donut_sizes, labels=donut_labels, autopct='%1.1f%%',
                                  startangle=90, colors=colors_donut, pctdistance=0.75,
                                  textprops=dict(color="#333333", size=11, weight='semibold'),
                                  wedgeprops=dict(width=0.4, edgecolor='w', linewidth=2))

# Center circle to make it a donut
ax1.set_title("Availability of Online Delivery", fontsize=14, fontweight='bold', pad=15)

# Subplot 2: Bar plot comparing average ratings
colors_bar = ['#D9534F', '#50E3C2']
bars = ax2.bar(['No Delivery', 'Offers Delivery'], [no_avg, yes_avg], color=colors_bar, width=0.45, edgecolor='none')

# Add values on top of bars
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2.0, height + 0.1, 
            f'{height:.2f} / 5.0', 
            ha='center', va='bottom', fontsize=12, fontweight='bold', color='#333333')

ax2.set_title("Average Ratings Comparison", fontsize=14, fontweight='bold', pad=15)
ax2.set_ylabel("Average Rating (0 - 5)", fontsize=11, fontweight='semibold')
ax2.set_ylim(0, 5.0)

# Apply spacing
sns.despine(ax=ax2, left=True, bottom=True)
plt.tight_layout()

# Save
output_image = os.path.join(script_dir, 'task4_online_delivery.png')
plt.savefig(output_image, dpi=300)
print(f"Visual representation saved successfully at:\n {output_image}\n")
print("="*60)
