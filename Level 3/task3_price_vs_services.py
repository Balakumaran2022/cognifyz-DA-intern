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

# 2. Convert 'Yes'/'No' columns to boolean/numeric for calculations
df['Online Delivery Numeric'] = df['Has Online delivery'].apply(lambda x: 1 if str(x).strip().lower() == 'yes' else 0)
df['Table Booking Numeric'] = df['Has Table booking'].apply(lambda x: 1 if str(x).strip().lower() == 'yes' else 0)

# Group by Price Range and calculate percentages
grouped = df.groupby('Price range').agg(
    OnlineDeliveryPct=('Online Delivery Numeric', 'mean'),
    TableBookingPct=('Table Booking Numeric', 'mean')
) * 100

print("="*65)
print("     LEVEL 3 - TASK 3: PRICE RANGE VS. SERVICES ANALYSIS     ")
print("="*65)
print("Percentage of services available by Price Range:")
print(f" {'Price Range':<15} | Online Delivery | Table Booking")
print("-" * 65)
price_labels = {1: 'Low (1)', 2: 'Medium (2)', 3: 'High (3)', 4: 'Very High (4)'}
for pr, row in grouped.iterrows():
    label = price_labels.get(pr, str(pr))
    print(f" {label:<15} | {row['OnlineDeliveryPct']:.2f}% | {row['TableBookingPct']:.2f}%")
print("-"*65)
print("Correlation Analysis:")
# Calculate Spearman rank correlation since Price range is ordinal
corr_delivery = df['Price range'].corr(df['Online Delivery Numeric'], method='spearman')
corr_booking = df['Price range'].corr(df['Table Booking Numeric'], method='spearman')
print(f"  -> Correlation (Price Range vs. Online Delivery): {corr_delivery:.4f}")
print(f"  -> Correlation (Price Range vs. Table Booking):   {corr_booking:.4f}")
print("="*65)

# 3. Create visual representation
fig, ax = plt.subplots(figsize=(9, 6))

# Prepare data for plotting
plot_df = grouped.reset_index()
plot_df = pd.melt(plot_df, id_vars=['Price range'], value_vars=['OnlineDeliveryPct', 'TableBookingPct'],
                  var_name='Service', value_name='Percentage')

# Map service names for legend
plot_df['Service'] = plot_df['Service'].map({
    'OnlineDeliveryPct': 'Online Delivery',
    'TableBookingPct': 'Table Booking'
})
plot_df['Price Label'] = plot_df['Price range'].map(price_labels)

# Grouped bar chart
sns.barplot(data=plot_df, x='Price Label', y='Percentage', hue='Service',
            palette=['#50E3C2', '#D9534F'], edgecolor='none', width=0.55, ax=ax)

# Add values on top of bars
for p in ax.patches:
    height = p.get_height()
    if height > 0:
        ax.text(p.get_x() + p.get_width()/2.0, height + 1.5, f'{height:.1f}%', 
                ha='center', va='bottom', fontsize=10, fontweight='bold', color='#333333')

ax.set_title("Availability of Services by Price Range Category", fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel("Price Range Category", fontsize=11, fontweight='semibold', labelpad=10)
ax.set_ylabel("Percentage Available (%)", fontsize=11, fontweight='semibold', labelpad=10)
ax.set_ylim(0, 110)
ax.legend(title="Service Type", fontsize=10, title_fontsize=11)

sns.despine(left=True, bottom=True)
plt.tight_layout()

# Save
output_image = os.path.join(script_dir, 'task3_price_vs_services.png')
plt.savefig(output_image, dpi=300)
print(f"Visual representation saved successfully at:\n {output_image}\n")
print("="*65)
