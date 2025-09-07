

import os
import random
import numpy as np
import pandas as pd


class DataGenerator:
    """
    
    """

    def __init__(self, n_rows=500, save_path="data/raw/generated_data.csv"):
        self.n_rows = n_rows
        self.save_path = save_path
        self.data = None

    def generate(self):
        """Generate synthetic dataset."""
        np.random.seed(42)  

        
        age = np.random.randint(18, 70, size=self.n_rows)
        income = np.random.randint(20000, 120000, size=self.n_rows)
        score1 = np.random.normal(50, 15, size=self.n_rows).astype(int)
        score2 = np.random.normal(60, 10, size=self.n_rows).astype(int)
        score3 = np.random.normal(70, 20, size=self.n_rows).astype(int)

        
        gender = np.random.choice(["Male", "Female"], size=self.n_rows)
        product_type = np.random.choice(["A", "B", "C"], size=self.n_rows)

        
        purchased = np.random.choice([0, 1], size=self.n_rows, p=[0.6, 0.4])

        
        self.data = pd.DataFrame({
            "age": age,
            "income": income,
            "score1": score1,
            "score2": score2,
            "score3": score3,
            "gender": gender,
            "product_type": product_type,
            "purchased": purchased
        })
        return self.data

    def save(self):
        """Save generated data to CSV."""
        os.makedirs(os.path.dirname(self.save_path), exist_ok=True)
        self.data.to_csv(self.save_path, index=False)
        print(f"Data saved to {self.save_path}")


if __name__ == "__main__":
    generator = DataGenerator(n_rows=500)
    df = generator.generate()
    print(df.head())   
    generator.save()
