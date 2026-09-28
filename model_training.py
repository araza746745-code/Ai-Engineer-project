import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. Load data
df = pd.read_csv("cleaned_sales_data.csv")

print("DATA LOADED:", df.shape)

# 2. Target
y = df["gross_amount"]

# 3. Features
X = df.drop(columns=["gross_amount"])

# 4. Only numeric columns
X = X.select_dtypes(include="number")

# 5. Remove missing values from X
X = X.fillna(X.median())

# 6. Remove missing values from y
y = y.fillna(y.median())

print("Missing values in X:", X.isna().sum().sum())
print("Missing values in y:", y.isna().sum())

# 7. Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)

# 8. Create model
model = LinearRegression()

# 9. Train model
model.fit(X_train, y_train)

print("MODEL TRAINED SUCCESSFULLY!")

#make predictions
y_pred = model.predict(X_test)

print("PREDICTIONS:")
print(y_pred[:10])

from sklearn.metrics import mean_absolute_error, r2_score

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("R2 SCORE:", r2)

import joblib
joblib.dump(model,"sales_model.pkl")

print("MODEL SAVED SUCCESSFULLU!")

print("FEATURE NAMES:")
print(X.columns.tolist())

X = X.select_dtypes(include="number")
print("FEATURE NAMES:")
print(X.columns.tolist())
X = X.fillna(X.median())