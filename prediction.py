import joblib
import pandas as pd

# Load trained model
model = joblib.load("sales_model.pkl")

print("MODEL LOADED SUCCESSFULLY!")

# Load the same data used for training
df = pd.read_csv("cleaned_sales_data.csv")

# Create features
X = df.drop(columns=["gross_amount"])

# Keep only numeric columns
X = X.select_dtypes(include="number")

# Handle missing values
X = X.fillna(X.median())

# Take one real row
sample = X.iloc[[0]]

# Make prediction
prediction = model.predict(sample)

print("PREDICTED GROSS AMOUNT:", prediction[0])
actual = df["gross_amount"].iloc[0]

print("ACTUAL GROSS AMOUNT:", actual)
print("PREDICTED GROSS AMOUNT:", prediction[0])
print("ERROR:", abs(actual - prediction[0]))