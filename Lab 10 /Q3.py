import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Generate sample student data
np.random.seed(42)
num_students = 100
data = {
    'student_id': np.arange(1, num_students+1),
    'GPA': np.round(np.random.normal(3.0, 0.5, num_students), 2),
    'study_hours': np.round(np.random.normal(15, 5, num_students)),
    'attendance_rate': np.round(np.random.uniform(60, 100, num_students))
}

df = pd.DataFrame(data)

# Feature selection and scaling
features = df[['GPA', 'study_hours', 'attendance_rate']]
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Elbow method to determine optimal K
inertia = []
k_range = range(2, 7)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(k_range, inertia, marker='o')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal K')
plt.xticks(k_range)
plt.grid()
plt.show()

# Silhouette analysis for additional validation
silhouette_scores = []
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    cluster_labels = kmeans.fit_predict(scaled_features)
    silhouette_scores.append(silhouette_score(scaled_features, cluster_labels))

optimal_k = np.argmax(silhouette_scores) + 2  # +2 because range starts at 2
print(f"Optimal number of clusters based on silhouette score: {optimal_k}")

# Perform clustering with optimal K
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
df['cluster'] = kmeans.fit_predict(scaled_features)

# Visualize clusters
plt.figure(figsize=(10, 6))
scatter = plt.scatter(df['study_hours'], df['GPA'], c=df['cluster'],
                     cmap='viridis', alpha=0.7, s=100)
plt.colorbar(scatter, label='Cluster')
plt.xlabel('Weekly Study Hours')
plt.ylabel('GPA')
plt.title(f'Student Clusters (K={optimal_k}) Based on Study Habits and Performance')
plt.grid(True)
plt.show()

# Cluster profiles
cluster_profiles = df.groupby('cluster')[['GPA', 'study_hours', 'attendance_rate']].mean()
print("\nCluster Profiles:")
print(cluster_profiles)

# Final output
print("\nFirst 10 Students with Cluster Assignments:")
print(df[['student_id', 'cluster']].head(10))

print("\nInterpretation:")
print("Cluster 0: Average performers with moderate study hours")
print("Cluster 1: High performers with strong study habits")
print("Cluster 2: At-risk students needing academic support")
