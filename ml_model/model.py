import pickle
from sklearn.ensemble import RandomForestClassifier
from preprocessing import load_and_preprocess_data


def train_model():
    X_train, X_test, y_train, y_test = load_and_preprocess_data()
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(X_train, y_train)

    # Save the trained model
    with open("model.pkl", "wb") as file:
        pickle.dump(model, file)
    print("Model trained and saved.")


if __name__ == "__main__":
    train_model()
