import os

# Set up Kaggle API credentials
os.makedirs("/root/.kaggle", exist_ok=True)
!cp kaggle.json /root/.kaggle/
!chmod 600 /root/.kaggle/kaggle.json

# Download the Breast Cancer Wisconsin tabular dataset
!kaggle datasets download -d uciml/breast-cancer-wisconsin-data
!unzip -q breast-cancer-wisconsin-data.zip

import pandas as pd

# Load data
df = pd.read_csv("data.csv")

# Drop ID and unnamed columns
df.drop(columns=['id', 'Unnamed: 32'], inplace=True)

# Encode 'diagnosis' column (not used for target here, just preserved)
df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})

# Simulate 'priority' based on radius_mean
df['priority'] = pd.qcut(df['radius_mean'], q=3, labels=['low', 'medium', 'high'])

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Split features and target
X = df.drop(columns=['priority'])
y = df['priority']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# Scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

# Accuracy and F1
acc = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted')

print(f"Accuracy: {acc:.4f}")
print(f"F1 Score: {f1:.4f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Confusion Matrix
conf_mat = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_mat, annot=True, fmt='d', cmap='Blues')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

