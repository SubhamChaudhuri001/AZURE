import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


# Load dataset
df = pd.read_csv("../data/diabetes_risk_dataset.csv")

# Basic Cleaning

# Encode gender (Male=1, Female=0)
df['gender'] = df['gender'].str.strip().str.lower()
df['gender'] = df['gender'].map({'male': 1, 'female': 0})

# Convert target to binary
# Assuming categories: Low, Moderate, High
df['diabetes_risk_category'] = df['diabetes_risk_category'].str.strip().str.lower()

df['diabetes_risk_category'] = df['diabetes_risk_category'].replace({
    'low risk': 0,
    'low': 0,

    'moderate risk': 1,
    'moderate': 1,

    'high risk': 1,
    'high': 1,

    'prediabetes': 1
})

# Drop NaN rows
df = df.dropna(subset=['diabetes_risk_category', 'gender'])


# Features & Target
X = df[['fasting_glucose_level',
        'bmi',
        'insulin_level',
        'age',
        'gender']]

y = df['diabetes_risk_category']

print("Unique target values AFTER cleaning:")
print(df['diabetes_risk_category'].unique())

print("Remaining samples:", len(df))

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", LogisticRegression(max_iter=2000))
])
model.fit(X_train, y_train)

# Accuracy
y_pred = model.predict(X_test)
print("🩸 Diabetes Accuracy:", accuracy_score(y_test, y_pred))

# Save Model
pickle.dump(model, open("diabetes_model.pkl", "wb"))

print("✅ New diabetes_model.pkl created successfully")
