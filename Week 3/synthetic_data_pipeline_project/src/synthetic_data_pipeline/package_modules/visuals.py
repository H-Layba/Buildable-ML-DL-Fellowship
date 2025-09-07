import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_histogram(df, column, save_path="plots/histogram.png"):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.figure(figsize=(6,4))
    sns.histplot(df[column], bins=20, kde=True)
    plt.title(f"Histogram of {column}")
    plt.savefig(save_path)
    plt.close()

def plot_bar(df, column, save_path="plots/bar.png"):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.figure(figsize=(6,4))
    sns.countplot(x=df[column])
    plt.title(f"Bar Plot of {column}")
    plt.savefig(save_path)
    plt.close()

def plot_scatter(df, x_col, y_col, save_path="plots/scatter.png"):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.figure(figsize=(6,4))
    sns.scatterplot(x=df[x_col], y=df[y_col])
    plt.title(f"Scatter Plot: {x_col} vs {y_col}")
    plt.savefig(save_path)
    plt.close()

def plot_heatmap(df, save_path="plots/heatmap.png"):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.figure(figsize=(8,6))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.savefig(save_path)
    plt.close()
