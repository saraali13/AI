import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.inspection import DecisionBoundaryDisplay
import matplotlib.pyplot as plt


# 1. Load and clean data
def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)

    # Handle missing values
    df.fillna({
        'age': df['age'].median(),
        'total_spending': df['total_spending'].median(),
        'visit_frequency': df['visit_frequency'].median()
    }, inplace=True)

    # Remove outliers
    for col in ['total_spending', 'visit_frequency']:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        df = df[(df[col] > (q1 - 1.5 * iqr)) & (df[col] < (q3 + 1.5 * iqr))]

    return df


# 2. Preprocess and scale features (maintaining feature names)
def preprocess_data(df):
    X = df[['total_spending', 'visit_frequency', 'age']]
    y = df['high_value']

    # Scale features while keeping feature names
    scaler = StandardScaler()
    X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

    return X_scaled, y, scaler


# 3. Train and evaluate model
def train_and_evaluate(X, y):
    # Split data (maintaining DataFrame structure)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Train SVM classifier
    svm = SVC(kernel='linear', C=1.0)
    svm.fit(X_train, y_train)

    # Evaluate
    y_pred = svm.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    # 2D Visualization using first two features
    plt.figure(figsize=(10, 6))
    X_vis = X.iloc[:, :2]  # Use first two features with their names

    # Temporary SVM for visualization
    svm_vis = SVC(kernel='linear', C=1.0).fit(X_vis, y)

    DecisionBoundaryDisplay.from_estimator(
        svm_vis, X_vis, response_method="predict",
        plot_method="pcolormesh", alpha=0.3
    )
    plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y, edgecolors='k')
    plt.xlabel('Total Spending (scaled)')
    plt.ylabel('Visit Frequency (scaled)')
    plt.title('Decision Boundary (First Two Features)')
    plt.show()

    return svm


# 4. Extract classification rules
def extract_rules(svm, scaler):
    coef = svm.coef_[0]
    intercept = svm.intercept_[0]

    print("\nClassification Rules:")
    print(
        f"{coef[0]:.2f}*(total_spending) + {coef[1]:.2f}*(visit_frequency) + {coef[2]:.2f}*(age) + {intercept:.2f} = 0")
    print("\nCustomers are classified as high-value if the equation result is > 0")


# Main execution
df = load_and_clean_data('customers.csv')
X, y, scaler = preprocess_data(df)
model = train_and_evaluate(X, y)
extract_rules(model, scaler)

# Example prediction (properly formatted with feature names)
new_customer = pd.DataFrame({
    'total_spending': [500],
    'visit_frequency': [8],
    'age': [35]
})
new_customer_scaled = pd.DataFrame(
    scaler.transform(new_customer),
    columns=new_customer.columns
)

prediction = model.predict(new_customer_scaled)
print(f"\nNew customer classification: {'HIGH VALUE' if prediction[0] == 1 else 'LOW VALUE'}")
