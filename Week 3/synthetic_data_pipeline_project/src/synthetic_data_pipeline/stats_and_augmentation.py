import pandas as pd
from synthetic_data_pipeline.package_modules import stats, augment


def run_stats_and_augmentation(cleaned_path="data/processed/cleaned_data.csv",
                               augmented_path="data/processed/augmented_data.csv"):
    
    df = pd.read_csv(cleaned_path)

    
    mean_age = stats.mean(df["age"])
    median_income = stats.median(df["income"])
    std_score1 = stats.std(df["score1"])
    std_score2 = stats.std(df["score2"])

    print("📊 Statistics:")
    print(f"Mean Age: {mean_age:.2f}")
    print(f"Median Income: {median_income:.2f}")
    print(f"Std of Score1: {std_score1:.2f}")
    print(f"Std of Score2: {std_score2:.2f}")

    
    augmented_df = augment.augment_data(df, multiplier=2, noise_std=0.05)

    
    augmented_df.to_csv(augmented_path, index=False)
    print(f"Augmented dataset saved to {augmented_path}")


if __name__ == "__main__":
    run_stats_and_augmentation()

