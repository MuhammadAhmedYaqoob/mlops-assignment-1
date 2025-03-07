import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_preprocess_data(csv_path="dataset.csv"):
    df = pd.read_csv(csv_path)
    X = df.drop(columns=["label"])
    y = df["label"]
    return train_test_split(X, y, test_size=0.2, random_state=42)
