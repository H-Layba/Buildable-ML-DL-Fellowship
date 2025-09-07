import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder


def prepare_data(raw_path="data/raw/generated_data.csv",
                 processed_path="data/processed/cleaned_data.csv"):
    
    os.makedirs(os.path.dirname(processed_path), exist_ok=True)

   
    df = pd.read_csv(raw_path)

    
    df.loc[5:10, "income"] = None
    df.loc[20:22, "gender"] = None

    print("🔎 Before Cleaning:")
    print(df.head(15))

    
    for col in df.select_dtypes(include=["int64", "float64"]).columns:
        df[col].fillna(df[col].mean(), inplace=True)

    
    for col in df.select_dtypes(include=["object"]).columns:
        df[col].fillna(df[col].mode()[0], inplace=True)

    
    label_encoders = {}
    for col in df.select_dtypes(include=["object"]).columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    print("\n After Cleaning & Encoding:")
    print(df.head(15))

    
    df.to_csv(processed_path, index=False)
    print(f"\nCleaned dataset saved to {processed_path}")


if __name__ == "__main__":
    prepare_data()
