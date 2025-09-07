import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)


class ModelTrainer:
    def __init__(self, data_path, dataset_type="cleaned", model_dir="models", results_dir="results"):
        self.data_path = data_path
        self.dataset_type = dataset_type
        self.model_dir = model_dir
        self.results_dir = results_dir

        
        os.makedirs(self.model_dir, exist_ok=True)
        os.makedirs(self.results_dir, exist_ok=True)

    def train_and_evaluate(self):
        
        df = pd.read_csv(self.data_path)

        if "purchased" not in df.columns:
            raise ValueError("Target column 'purchased' not found in dataset!")

       
        X = df.drop("purchased", axis=1)
        y = df["purchased"]

       
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        
        models = {
            "logistic": LogisticRegression(max_iter=1000),
            "randomforest": RandomForestClassifier(n_estimators=100, random_state=42),
        }

        metrics_list = []

        for name, model in models.items():
            print(f"\nTraining {name} on {self.dataset_type} dataset...")
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            y_prob = model.predict_proba(X_test)[:, 1]

            
            metrics = {
                "model": name,
                "dataset": self.dataset_type,
                "accuracy": accuracy_score(y_test, y_pred),
                "precision": precision_score(y_test, y_pred),
                "recall": recall_score(y_test, y_pred),
                "f1_score": f1_score(y_test, y_pred),
                "roc_auc": roc_auc_score(y_test, y_prob),
            }
            metrics_list.append(metrics)

            
            model_path = os.path.join(self.model_dir, f"{name}_{self.dataset_type}.joblib")
            joblib.dump(model, model_path)
            print(f"Saved {model_path}")

        
        results_df = pd.DataFrame(metrics_list)
        results_path = os.path.join(self.results_dir, f"metrics_{self.dataset_type}.csv")
        results_df.to_csv(results_path, index=False)
        print(f"Metrics saved to {results_path}")


if __name__ == "__main__":
    print("\n[Standalone Run] Training on cleaned dataset...")
    trainer = ModelTrainer("data/processed/cleaned_data.csv", dataset_type="cleaned")
    trainer.train_and_evaluate()

    print("\n[Standalone Run] Training on augmented dataset...")
    trainer_aug = ModelTrainer("data/processed/augmented_data.csv", dataset_type="augmented")
    trainer_aug.train_and_evaluate()
