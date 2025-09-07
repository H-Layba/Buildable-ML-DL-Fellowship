import pandas as pd
from synthetic_data_pipeline.package_modules import visuals


def run_visualizations(cleaned_path="data/processed/cleaned_data.csv"):
   
    df = pd.read_csv(cleaned_path)

    
    visuals.plot_histogram(df, "age", save_path="plots/age_hist.png")

    
    visuals.plot_bar(df, "gender", save_path="plots/gender_bar.png")

    
    visuals.plot_heatmap(df, save_path="plots/heatmap.png")

    
    visuals.plot_scatter(df, "income", "score1", save_path="plots/income_vs_score1.png")

    print("All plots generated and saved in 'plots/' folder.")


if __name__ == "__main__":
    run_visualizations()
