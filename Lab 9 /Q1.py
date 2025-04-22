import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


# 1. Load and clean data
def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)

    # Handle missing values
    df.fillna({
        'bedrooms': df['bedrooms'].median(),
        'bathrooms': df['bathrooms'].median(),
        'sqft': df['sqft'].mean(),
        'age': df['age'].median()
    }, inplace=True)

    return df


# 2. Feature engineering and preprocessing
def preprocess_data(df):
    # Separate features and target
    X = df.drop('price', axis=1)
    y = df['price']

    # Identify categorical and numerical columns
    categorical_cols = ['neighborhood']
    numerical_cols = ['bedrooms', 'bathrooms', 'sqft', 'age']

    # Create preprocessing pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', 'passthrough', numerical_cols),
            ('cat', OneHotEncoder(), categorical_cols)
        ])

    return X, y, preprocessor


# 3. Model training and evaluation
def train_and_evaluate(X, y, preprocessor):
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create pipeline
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
    ])

    # Train model
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Model Performance:\nMSE: {mse:.2f}\nR2 Score: {r2:.2f}")

    return model


# 4. Predict new house price
def predict_new_house(model, new_data):
    return model.predict(new_data)


df = load_and_clean_data('house_prices.csv')

# Preprocess
X, y, preprocessor = preprocess_data(df)

# Train and evaluate
model = train_and_evaluate(X, y, preprocessor)

# Example prediction
new_house = pd.DataFrame({
    'bedrooms': [3],
    'bathrooms': [2],
    'sqft': [1800],
    'age': [10],
    'neighborhood': ['Urban_B']
})

predicted_price = predict_new_house(model, new_house)
print(f"\nPredicted price for new house: ${predicted_price[0]:,.2f}")
