import pandas as pd

# Load cleaned data
df = pd.read_csv("cleaned_sales_data.csv")

print("DATA LOADED:")
print(df.head())

# Feature 1: Calculated Sales
df["calculated_sales"] = df["quantity"] * df["unit_price"]

print("\nCALCULATED SALES:")
print(df[["quantity", "unit_price", "calculated_sales"]].head())

# Convert order_date to date
df["order_date"] = pd.to_datetime(
    df["order_date"],
    dayfirst=True
)

# Date Features
df["order_year"] = df["order_date"].dt.year
df["order_month"] = df["order_date"].dt.month
df["order_day"] = df["order_date"].dt.day
df["order_dayofweek"] = df["order_date"].dt.dayofweek

print("\nDATE FEATURES:")
print(
    df[
        [
            "order_date",
            "order_year",
            "order_month",
            "order_day",
            "order_dayofweek"
        ]
    ].head()
)

# ONE-HOTE ENCODING
df = pd.get_dummies(
    df,
    columns=["gender"],
    dtype=int
)

print("\nAFTER ONE-HOT ENCODING:")
print(df.head())

# CUSTOMER SEGMENT ENCODING

df = pd.get_dummies(
    df,
    columns=["customer_segment"],
    dtype=int
)

print("\nCUSTOMER SEGMENT ENCODING:")
print(
    df[
        [
            "customer_segment_Consumer",
            "customer_segment_Corporate",
            "customer_segment_Small Business"
        ]
    ].head()
)

# CATEGORY ENCODING

df = pd.get_dummies(
    df,
    columns=["category"],
    dtype=int
)

print("\nCATEGORY ENCODING:")
print(
    df[
        [
            "category_Accessories",
            "category_Electronics",
            "category_Office",
            "category_Wearables"
        ]
    ].head()
)

#Feature selection
drop_columns =[
    "order_id",
    "customer_name",
    "customer_email",
    "customer_phone"
]

df = df.drop(columns=drop_columns)

print("\nAFTER FEATURE SELECTION:")
print(df.head())
print("\nTOTAL COLUMNS:",len(df.columns))

# FEATURE SCALING

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

df[["quantity", "unit_price", "calculated_sales"]] = scaler.fit_transform(
    df[["quantity", "unit_price", "calculated_sales"]]
)

print("\nAFTER SCALING:")
print(df[["quantity", "unit_price", "calculated_sales"]].head())

X = df.drop(columns=["gross_amount"])
y = df["gross_amount"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
print("NON-NUMERIC COLUMNS:")
print(X.select_dtypes(exclude="number").columns)
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)
import numpy as np

X = df.drop(columns=["gross_amount"])

# Sirf numeric columns
X = X.select_dtypes(include="number")

# Missing/infinite values handle karo
X = X.replace([np.inf, -np.inf], np.nan)
X = X.fillna(X.median())

y = df["gross_amount"]

# Target mein missing values hain to remove karo
y = y.fillna(y.median())

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train,y_train)

print("MODEL TRAINED SUCCESSFULLY!")

X = df.drop(columns=["gross_amount"])

#sirf number column rakkho 
X = X.select_dtypes(include="number")

y = df["gross_amount"]

# FEATURES AND TARGET

X = df.drop(columns=["gross_amount"])

# Only numerical columns
X = X.select_dtypes(include="number")

y = df["gross_amount"]

print("X columns:", X.dtypes)

# TRAIN TEST SPLIT
from sklearn.model_selection import train_test_split

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


# MODEL
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

print("MODEL TRAINED SUCCESSFULLY!")
# ==============================
# FINAL DATA FOR MODEL
# ==============================

X = df.drop(columns=["gross_amount"])

# Keep ONLY numeric columns
X = X.select_dtypes(include=["number"])

y = df["gross_amount"]

print("NON-NUMERIC COLUMNS IN X:")
print(X.select_dtypes(exclude=["number"]).columns)

print("X SHAPE:", X.shape)

# ==============================
# TRAIN TEST SPLIT
# ==============================

from sklearn.model_selection import train_test_split


  
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)

# ==============================
# MODEL
# ==============================

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

print("MODEL TRAINED SUCCESSFULLY!")
# =========================
# PREPARE DATA FOR MODEL
# =========================

X = df.select_dtypes(include=["number"]).drop(
    columns=["gross_amount"],
    errors="ignore"
)

y = df["gross_amount"]

print("X SHAPE:", X.shape)
print("NON-NUMERIC COLUMNS:")
print(X.select_dtypes(exclude=["number"]).columns)

# =========================
# TRAIN TEST SPLIT
# =========================

from sklearn.model_selection import train_test_split

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

# =========================
# MODEL
# =========================

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

print("MODEL TRAINED SUCCESSFULLY!")