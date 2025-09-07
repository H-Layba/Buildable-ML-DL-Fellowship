import numpy as np
import pandas as pd

def augment_data(df, multiplier=2, noise_std=0.01):
    """
   
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns

    augmented_list = [df]
    for _ in range(multiplier - 1):
        noisy_copy = df.copy()
        for col in numeric_cols:
            noisy_copy[col] = noisy_copy[col] + np.random.normal(0, noise_std * df[col].std(), size=len(df))
        augmented_list.append(noisy_copy)

    augmented_df = pd.concat(augmented_list, ignore_index=True)
    return augmented_df


def add_noise(df, noise_level=0.05):
    return augment_data(df, multiplier=2, noise_std=noise_level)
