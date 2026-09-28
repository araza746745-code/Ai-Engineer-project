import pandas as pd

df=pd.read_csv("sales_raw_1000_rows_50_columns.csv")

print(df.head())

print(df.shape)

print(df.columns)

print(df.info())

print(df.isnull().sum())

print("Duplicate rows:", df.duplicated().sum())

print(df.describe())

print(df.nunique())

print(df["gender"].value_counts())

print(df["customer_segment"].value_counts())

segment_count = df["customer_segment"].value_counts()

print(segment_count)

print(df.describe())
print(df.nunique())
print(df["gender"].value_counts())
print(df["customer_segment"].value_counts())

print('Duplicate rows:', df.duplicated().sum())

print(df.isnull().sum())

print("Dublicate rows:",df.duplicated().sum())

print("\nDuplicate ordes IDs:")

print(df.isnull().sum()[df.isnull().sum()>0])

print(df[df["order_id"]==500])

print(df.isnull().sum()[df.isnull().sum()>0])
print(df[df["order_id"]==500])

missing_rows=df[df.isnull().any(axis=1)]

print(missing_rows)

return_missing=df[df["return_reason"].isnull()]

print(return_missing[["order_id","return_reason"]])

print(df["return_status"].value_counts(dropna=False))

print(df[df["customer_email"].isnull()][["customer_name","customer_email"]])

# Clean copy
clean_df = df.copy()

# Missing text values
clean_df["customer_email"] = clean_df["customer_email"].fillna("Unknown")
clean_df["city"] = clean_df["city"].fillna("Unknown")
clean_df["return_reason"] = clean_df["return_reason"].fillna("No Return")

# Missing numeric values
clean_df["quantity"] = clean_df["quantity"].fillna(clean_df["quantity"].median())
clean_df["unit_price"] = clean_df["unit_price"].fillna(clean_df["unit_price"].median())

# Check missing values again
print("Missing values after cleaning:")
print(clean_df.isnull().sum().sum())

clean_df = clean_df.drop_duplicates()
print("Rows after cleaning:", len(clean_df))

clean_df.to_csv("sales_cleaned.csv", index=False)

print("cleaned data saved to successfullt!")