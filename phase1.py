import pandas as pd

df = pd.read_csv("sales_raw_1000_rows_50_columns.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())

print("\nMISSING VALUES:")
print(df.isnull().sum)

print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())

import pandas as pd

df = pd.read_csv("sales_raw_1000_rows_50_columns.csv")

print("FIRST 5 ROWS:")
print(df.head())

print("\nSHAPE:")
print(df.shape)

print("\nCOLUMNS:")
print(df.columns)

print("\nDATA INFORMATION:")
print(df.info())

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())

print("\nDATA TYPES:")
print(df.dtypes)


print("\nMISSING CUSTOMER EMAIL:")
print(df[df["customer_email"].isnull()])

print("\nMISSING CITY:")
print(df[df["city"].isnull()])

print("\nCUSTOMER PHONE SAMPLE:")
print(df["customer_phone"].head(10))
df["customer_email"]
df["customer_email"].fillna("unknow")

df["customer_phone"]
df["customer_phone"].apply(lambda x: str(int(x))if pd.notna(x)else "unknown")

print("\nCLEANING MISSING EMAIL...")
df["customer_email"] = df["customer_email"].fillna("unknown")

print("CLEANING MISSING CITY...")
df["city"] = df["city"].fillna("Unknown")

print("CONVERTING PHONE TO TEXT...")
df["customer_phone"] = df["customer_phone"].apply(
    lambda x: str(int(x)) if pd.notna(x) else "Unknown"
)

print("\nAFTER CLEANING:")
print(df[["customer_email", "city", "customer_phone"]].head())

print("\nAGE CHECK:")
print(df["age"].describe())

print("\nQUANTITY CHECK:")
print(df["quantity"].describe())

print("\nUNIT PRICE CHECK:")
print(df["unit_price"].describe())

print("\nNUMERICAL SUMMARY:")
print(df.describe())

print("\nNUMERICAL SUMMARY:")
print(df.describe())

print("\nGENDER COUNT:")
print(df["gender"].value_counts())

print("\nCUSTOMER SEGMENT:")
print(df["customer_segment"].value_counts())

print("\nCATEGORY COUNT:")
print(df["category"].value_counts())

print("\nSALES BY CATEGORY:")
print(df.groupby("category")["gross_amount"].sum())

print("\nAVERAGE SALES BY CATEGORY:")
print(df.groupby("category")["gross_amount"].mean())

df.to_csv("cleaned_sales_data.csv",index=False)