import os


from src.synthetic_data_pipeline.data_generator import DataGenerator

from src.synthetic_data_pipeline.data_preparation import prepare_data

from src.synthetic_data_pipeline.package_modules import augment, stats, visuals

from src.synthetic_data_pipeline.model_trainer import ModelTrainer

DATA_RAW = "data/raw/generated_data.csv"
DATA_CLEANED = "data/processed/cleaned_data.csv"
DATA_AUG = "data/processed/augmented_data.csv"


def main():
    
    print("\n[1] Generating synthetic data...")
    gen = DataGenerator()
    gen.generate_data(num_rows=500, save_path=DATA_RAW)

    
    print("\n[2] Cleaning data...")
    prepare_data(raw_path=DATA_RAW, processed_path=DATA_CLEANED)

    
    print("\n[3] Augmenting data...")
    import pandas as pd
    df_cleaned = pd.read_csv(DATA_CLEANED)

    
    for col in ["age", "income"]:
        print(f"\nStats for {col}:")
        print(f"Mean = {stats.mean(df_cleaned[col])}")
        print(f"Median = {stats.median(df_cleaned[col])}")
        print(f"Std Dev = {stats.std_dev(df_cleaned[col])}")

    
    df_aug = augment.add_noise(df_cleaned, noise_level=0.05)
    os.makedirs("data/processed", exist_ok=True)
    df_aug.to_csv(DATA_AUG, index=False)
    print(f"Augmented dataset saved to {DATA_AUG}")

    
    print("\n[4] Generating plots...")
    os.makedirs("plots", exist_ok=True)
    visuals.plot_histogram(df_cleaned, "age", "plots/age_hist.png")
    visuals.plot_bar(df_cleaned, "gender", "plots/gender_bar.png")
    visuals.plot_heatmap(df_cleaned, "plots/corr_heatmap.png")
    visuals.plot_scatter(df_cleaned, "age", "income", "plots/age_vs_income.png")
    print("Plots saved to plots/ folder.")

    
    print("\n[5] Training models on cleaned dataset...")
    trainer_clean = ModelTrainer(DATA_CLEANED, dataset_type="cleaned")
    trainer_clean.train_and_evaluate()

    print("\n[6] Training models on augmented dataset...")
    trainer_aug = ModelTrainer(DATA_AUG, dataset_type="augmented")
    trainer_aug.train_and_evaluate()

    print("\n Pipeline finished successfully!")


if __name__ == "__main__":
    main()
