import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Load dataset
df = pd.read_csv("../data/dataset-framingham-heart-study.csv")
print(df.columns)

# Remove missing values
df = df.dropna()

# ✅ Use 9 strong features
X = df[['male',
        'age',
        'currentSmoker',
        'diabetes',
        'totChol',
        'sysBP',
        'diaBP',
        'BMI',
        'glucose']]

# Target column
y = df['TenYearCHD']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Pipeline with scaling
model = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", LogisticRegression(max_iter=2000))
])

model.fit(X_train, y_train)

# Accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("❤️ Framingham 9-Feature Model Accuracy:", accuracy)

# Save model
pickle.dump(model, open("heart_model.pkl", "wb"))

print("✅ heart_model.pkl created successfully")
