import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pickle

# Load dataset
df = pd.read_csv('phishing.csv')

# Drop unnecessary index column if present
if 'Index' in df.columns:
    df.drop(['Index'], axis=1, inplace=True)

# Split features and labels
X = df.drop('class', axis=1)
y = df['class']

# Convert labels if needed: -1 → 0
y = y.replace(-1, 0)

# Debug: Print feature names and count
print("Feature names:", X.columns.tolist())
print("Number of features:", X.shape[1])

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create base models
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
xgb_model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')

# Ensemble: Soft Voting
ensemble_model = VotingClassifier(estimators=[
    ('rf', rf_model),
    ('xgb', xgb_model)
], voting='soft')

# Train the ensemble model
ensemble_model.fit(X_train, y_train)

# Evaluate the model
y_pred = ensemble_model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save model
with open('phishing_model.pkl', 'wb') as f:
    pickle.dump(ensemble_model, f)

print("✅ Model training complete and saved as 'phishing_model.pkl'")