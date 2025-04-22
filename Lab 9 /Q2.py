import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
from sklearn.pipeline import Pipeline
import joblib
import re

# 1. Load and preprocess data
def load_and_preprocess(filepath):
    df = pd.read_csv(filepath)

    # Basic cleaning
    df['email'] = df['email'].str.lower()
    df['email'] = df['email'].apply(lambda x: re.sub(r'[^\w\s]', '', x))
    return df

# 2. Feature extraction and model training
def train_spam_classifier(df):
    # Split data
    X = df['email']
    y = df['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create pipeline
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=5000)),
        ('classifier', MultinomialNB())
    ])

    # Train
    pipeline.fit(X_train, y_train)

    # Evaluate
    y_pred = pipeline.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

    return pipeline


# 3. Save and load model
def save_model(model, filename):
    joblib.dump(model, filename)

def load_model(filename):
    return joblib.load(filename)

# 4. Classify new email
def classify_email(model, email_text):
    return model.predict([email_text])[0]


df = load_and_preprocess('emails.csv')

# Train and evaluate
spam_model = train_spam_classifier(df)

# Save model
save_model(spam_model, 'spam_classifier.joblib')

# Example classification
test_email = "Congratulations! You've won a $1000 prize. Click here to claim!"
prediction = classify_email(spam_model, test_email)
print(f"\nEmail classification: {'SPAM' if prediction == 1 else 'NOT SPAM'}")
