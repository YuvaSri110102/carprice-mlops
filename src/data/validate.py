import logging

logging.basicConfig(level=logging.INFO)

EXPECTED_COLUMNS = [
    "car_name",
    "brand",
    "model",
    "vehicle_age",
    "km_driven",
    "seller_type",
    "fuel_type",
    "transmission_type",
    "mileage",
    "engine",
    "max_power",
    "seats",
    "selling_price"
]


def validate_columns(df):

    logging.info("Validating dataset columns...")

    missing_cols = []

    for col in EXPECTED_COLUMNS:
        if col not in df.columns:
            missing_cols.append(col)

    if missing_cols:
        raise ValueError(f"Missing columns: {missing_cols}")

    logging.info("Column validation successful")

    return True