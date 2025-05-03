import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import matplotlib.pyplot as plt

# Sample vehicle data
data = {
    'vehicle_serial_no': [5, 3, 8, 2, 4, 7, 6, 10, 1, 9],
    'mileage': [150000, 120000, 250000, 80000, 100000, 220000, 180000, 300000, 75000, 280000],
    'fuel_efficiency': [15, 18, 10, 22, 20, 12, 16, 8, 24, 9],
    'maintenance_cost': [5000, 4000, 7000, 2000, 3000, 6500, 5500, 8000, 1500, 7500],
    'vehicle_type': ['SUV', 'Sedan', 'Truck', 'Hatchback', 'Sedan', 'Truck', 'SUV', 'Truck', 'Hatchback', 'SUV']
}

df = pd.DataFrame(data)

# Prepare features (excluding serial number)
features = df.drop('vehicle_serial_no', axis=1)

# Clustering without scaling
kmeans_unscaled = KMeans(n_clusters=3, random_state=42)
df['cluster_unscaled'] = kmeans_unscaled.fit_predict(features[['mileage', 'fuel_efficiency', 'maintenance_cost']])

# Clustering with scaling (excluding vehicle_type)
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['mileage', 'fuel_efficiency', 'maintenance_cost']),
        ('cat', OneHotEncoder(), ['vehicle_type'])
    ],
    remainder='passthrough'
)

scaled_features = preprocessor.fit_transform(features)
kmeans_scaled = KMeans(n_clusters=3, random_state=42)
df['cluster_scaled'] = kmeans_scaled.fit_predict(scaled_features)

# Compare results
print("Vehicle Clustering Results")
print("\nWithout Scaling:")
print(df[['vehicle_serial_no', 'cluster_unscaled']].sort_values('cluster_unscaled'))

print("\nWith Scaling:")
print(df[['vehicle_serial_no', 'cluster_scaled']].sort_values('cluster_scaled'))

# Visual analysis
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Unscaled visualization
sns.scatterplot(data=df, x='mileage', y='maintenance_cost',
                hue='cluster_unscaled', style='vehicle_type',
                palette='viridis', s=100, ax=axes[0])
axes[0].set_title('Unscaled Features Clustering')

# Scaled visualization
sns.scatterplot(data=df, x='mileage', y='maintenance_cost',
                hue='cluster_scaled', style='vehicle_type',
                palette='viridis', s=100, ax=axes[1])
axes[1].set_title('Scaled Features Clustering')

plt.tight_layout()
plt.show()

print("\nKey Observations:")
print("1. Without scaling, mileage dominates clustering due to its larger numerical values.")
print("2. After scaling, maintenance_cost and fuel_efficiency have equal influence.")
print("3. The scaled version better captures the relationship between all operational metrics.")
print("4. Vehicle type was one-hot encoded to include categorical information in clustering.")
