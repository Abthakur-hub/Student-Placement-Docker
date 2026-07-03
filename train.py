import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv("dataset/placement.csv")

# -------------------------------
# Drop unnecessary columns
# -------------------------------
df.drop(["sl_no", "salary"], axis=1, inplace=True)

# -------------------------------
# Encode categorical columns
# -------------------------------
label_encoders = {}

categorical_columns = [
    "gender",
    "ssc_b",
    "hsc_b",
    "hsc_s",
    "degree_t",
    "workex",
    "specialisation",
    "status"
]

for col in categorical_columns:
    encoder = LabelEncoder()
    df[col] = encoder.fit_transform(df[col])
    label_encoders[col] = encoder

# -------------------------------
# Features and Target
# -------------------------------
X = df.drop("status", axis=1)
y = df["status"]

# -------------------------------
# Train Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -------------------------------
# Model
# -------------------------------
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# -------------------------------
# Prediction
# -------------------------------
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("=" * 40)
print("Model Accuracy")
print("=" * 40)
print(f"{accuracy*100:.2f}%")

# -------------------------------
# Save model
# -------------------------------
joblib.dump(model, "placement_model.pkl")

# Save encoders
joblib.dump(label_encoders, "encoders.pkl")

print("\nModel saved successfully!")