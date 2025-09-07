import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder


class DataPreprocessor:
    def __init__(self, input_path="data/raw/generated_data.csv",
                 output_path="data/processed/cleaned_data.csv"):
        self.input_path = input_path
        self.output_path = output_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.input_path)
        return self.df

    def insert_missing_values(self):
        """Intentionally insert NaN values into some columns (for demo)."""
        self.df.loc[0:5, "income"] = None
        self.df.loc[10:12, "score1"] = None
        return self.df

    def handle_missing_values(self):
        """Fill missing values with column mean."""
        self.df = self.df.fillna(self.df.mean(numeric_only=True))
        return self.df

    def encode_categoricals(self):
        """Convert categorical features into numeric (Label Encoding)."""
        label_encoders = {}
        for col in self.df.select_dtypes(include=["object"]).columns:
            le = LabelEncoder()
            self.df[col] = le.fit_transform(self.df[col])
            label_encoders[col] = le
        return self.df, label_encoders

    def save_data(self):
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        self.df.to_csv(self.output_path, index=False)
        print(f"Cleaned dataset saved to {self.output_path}")


if __name__ == "__main__":
    prep = DataPreprocessor()
    df = prep.load_data()
    print("Before inserting NaNs:\n", df.head())

    df = prep.insert_missing_values()
    print("After inserting NaNs:\n", df.head(15))

    df = prep.handle_missing_values()
    df, encoders = prep.encode_categoricals()
    print("After cleaning + encoding:\n", df.head())

    prep.save_data()
