import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Set style for professional look
sns.set_style("white")
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

# 1. Load the dataset
script_dir = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(os.path.dirname(script_dir), 'Dataset .csv')
df = pd.read_csv(dataset_path)

# 2. Filter coordinates
# Coordinate (0, 0) is a default placeholder, filter it out along with nulls
df_geo = df.dropna(subset=['Longitude', 'Latitude']).copy()
df_geo = df_geo[(df_geo['Longitude'] != 0) & (df_geo['Latitude'] != 0)]

# 3. K-Means clustering to identify distinct regional clusters
# Let's perform K-Means to identify the 3 primary global restaurant hubs in our data
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df_geo['Cluster'] = kmeans.fit_predict(df_geo[['Longitude', 'Latitude']])
centers = kmeans.cluster_centers_

print("="*60)
print("          LEVEL 2 - TASK 3: GEOGRAPHIC ANALYSIS          ")
print("="*60)
print(f"Total restaurants with valid coordinates: {len(df_geo):,}")
print("-"*60)
print("Geographic cluster centers found via K-Means:")
for c_id, center in enumerate(centers):
    c_lon, c_lat = center[0], center[1]
    # Find nearest restaurant in dataset to name this cluster
    distances = ((df_geo['Longitude'] - c_lon)**2 + (df_geo['Latitude'] - c_lat)**2)**0.5
    nearest_idx = distances.idxmin()
    nearest_city = df_geo.loc[nearest_idx, 'City']
    cluster_count = len(df_geo[df_geo['Cluster'] == c_id])
    print(f" Cluster {c_id+1} | Center: Lat {c_lat:.2f}, Lon {c_lon:.2f} | Hub Region: {nearest_city:<10} | Count: {cluster_count:,} ({cluster_count/len(df_geo)*100:.1f}%)")
print("="*60)

# 4. Create premium plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6.5))

# Subplot 1: Global Scatter Plot colored by Cluster
# Use nice colors to distinguish clusters
cluster_colors = ['#4A90E2', '#50E3C2', '#F5A623']
for c_id in range(3):
    clustered_data = df_geo[df_geo['Cluster'] == c_id]
    ax1.scatter(clustered_data['Longitude'], clustered_data['Latitude'], 
                color=cluster_colors[c_id], alpha=0.5, s=15, edgecolor='none', label=f'Cluster {c_id+1}')

ax1.set_title("Global Geographic Distribution & Hub Clusters", fontsize=13, fontweight='bold', pad=15)
ax1.set_xlabel("Longitude", fontsize=11, fontweight='semibold')
ax1.set_ylabel("Latitude", fontsize=11, fontweight='semibold')
ax1.grid(True, linestyle=':', alpha=0.4)
ax1.legend(loc='lower left', fontsize=10)

# Subplot 2: Zoom in on National Capital Region (NCR) of India
# Since the vast majority of restaurants are clustered around New Delhi, India,
# let's zoom in on India's NCR (Lon 76.8 to 77.6, Lat 28.3 to 28.8) to see local patterns.
df_ncr = df_geo[(df_geo['Longitude'] > 76.7) & (df_geo['Longitude'] < 77.6) & 
                (df_geo['Latitude'] > 28.2) & (df_geo['Latitude'] < 28.9)]

if len(df_ncr) > 100:
    # Color NCR restaurants by rating to show spatial quality hotspots
    scatter2 = ax2.scatter(df_ncr['Longitude'], df_ncr['Latitude'], c=df_ncr['Aggregate rating'], 
                           cmap='coolwarm', alpha=0.4, s=8, edgecolor='none')
    cbar = fig.colorbar(scatter2, ax=ax2)
    cbar.set_label("Aggregate Rating (0 - 5)", fontsize=11, fontweight='semibold', labelpad=10)
    ax2.set_title("NCR India Hotspots (Colored by Rating)", fontsize=13, fontweight='bold', pad=15)
    ax2.set_xlabel("Longitude", fontsize=11, fontweight='semibold')
    ax2.set_ylabel("Latitude", fontsize=11, fontweight='semibold')
    ax2.grid(True, linestyle=':', alpha=0.4)
else:
    # Fallback to general rating-colored global scatter
    scatter2 = ax2.scatter(df_geo['Longitude'], df_geo['Latitude'], c=df_geo['Aggregate rating'], 
                           cmap='coolwarm', alpha=0.5, s=15, edgecolor='none')
    cbar = fig.colorbar(scatter2, ax=ax2)
    cbar.set_label("Aggregate Rating (0 - 5)", fontsize=11, fontweight='semibold')
    ax2.set_title("Global Restaurants (Colored by Rating)", fontsize=13, fontweight='bold', pad=15)
    ax2.set_xlabel("Longitude", fontsize=11, fontweight='semibold')
    ax2.set_ylabel("Latitude", fontsize=11, fontweight='semibold')
    ax2.grid(True, linestyle=':', alpha=0.4)

plt.tight_layout()

# Save
output_image = os.path.join(script_dir, 'task3_geographic_analysis.png')
plt.savefig(output_image, dpi=300)
print(f"Visual representation saved successfully at:\n {output_image}\n")
print("="*60)
