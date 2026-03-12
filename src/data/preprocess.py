import logging
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

logging.basicConfig(level=logging.INFO)

categorical_features = [
    "brand",
    "model",
    "seller_type",
    "fuel_type",
    "transmission_type"
]

numerical_features = [
    "vehicle_age",
    "km_driven",
    "mileage",
    "engine",
    "max_power",
    "seats"
]


def preprocess_data(df):

    logging.info("Starting preprocessing")

    df = df.drop(columns=["car_name"])

    df = df.dropna()

    X = df.drop(columns=["selling_price"])
    y = df["selling_price"]

    # Preprocessing transformer
    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
            ("num", "passthrough", numerical_features)
        ]
    )

    # Train test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    logging.info("Preprocessing completed")

    return X_train, X_test, y_train, y_test, preprocessor
    