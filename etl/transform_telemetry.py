"""
ETL transformation script for autonomous vehicle and delivery robot telemetry.

This script demonstrates how raw sensor and telemetry data can be cleaned,
normalized, and transformed into analytics-ready datasets suitable for
storage in an analytical database such as ClickHouse.
"""

import pandas as pd


def load_raw_data(path: str) -> pd.DataFrame:
    """
    Load raw telemetry data from a CSV file.
    """
    return pd.read_csv(path)


def transform_telemetry(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform raw telemetry data into analytics-ready format.
    """
    df = df.copy()

    # Normalize timestamps
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df = df.dropna(subset=["timestamp"])

    # Basic cleaning
    df["speed"] = df.get("speed", 0).fillna(0)
    df["point_count"] = df.get("point_count", 0).fillna(0)

    # Derived metric
    df["speed_mps"] = df["speed"] / 3.6

    return df


def main():
    raw_path = "data/raw/telemetry_sample.csv"
    output_path = "data/processed/telemetry_analytics.csv"

    df_raw = load_raw_data(raw_path)
    df_clean = transform_telemetry(df_raw)

    df_clean.to_csv(output_path, index=False)


if __name__ == "__main__":
    main()
