import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Sample customer data with multiple features
data = {
    'customer_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'age': [25, 32, 45, 28, 50, 38, 42, 29, 35, 40],
    'annual_spending': [2500, 3200, 1800, 4200, 1500, 2800, 2100, 3800, 2900, 2000],
    'monthly_visits': [4, 6, 2, 8, 1, 5, 3, 7, 5, 2],
    'avg_purchase_value': [120, 150, 90, 180, 70, 130, 100, 160, 140, 95]
}

df = pd.DataFrame(data)

# Prepare features (excluding customer_id)
features = df.drop('customer_id', axis=1)

# Clustering without scaling
kmeans_unscaled = KMeans(n_clusters=3, random_state=42)
df['cluster_unscaled'] = kmeans_unscaled.fit_predict(features)

# Clustering with scaling (excluding age)
scaler = StandardScaler()
scaled_features = features.copy()
cols_to_scale = ['annual_spending', 'monthly_visits', 'avg_purchase_value']
scaled_features[cols_to_scale] = scaler.fit_transform(features[cols_to_scale])

kmeans_scaled = KMeans(n_clusters=3, random_state=42)
df['cluster_scaled'] = kmeans_scaled.fit_predict(scaled_features)

# Compare results
print("Cluster Distribution Without Scaling:")
print(df['cluster_unscaled'].value_counts())

print("\nCluster Distribution With Scaling:")
print(df['cluster_scaled'].value_counts())

# Visualize the differences
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.scatterplot(data=df, x='annual_spending', y='monthly_visits',
                hue='cluster_unscaled', palette='viridis')
plt.title('Clustering Without Scaling')

plt.subplot(1, 2, 2)
sns.scatterplot(data=df, x='annual_spending', y='monthly_visits',
                hue='cluster_scaled', palette='viridis')
plt.title('Clustering With Scaling (Features Scaled Except Age)')

plt.tight_layout()
plt.show()

# Analysis
print("\nKey Insights:")
print("1. Without scaling, features with larger values (like annual_spending) dominate the clustering.")
print("2. After scaling, all features contribute more equally to the distance calculations.")
print("3. The scaled version typically produces more balanced clusters that better represent all dimensions.")
print("4. Age wasn't scaled to preserve its original interpretation while other features were normalized.")
