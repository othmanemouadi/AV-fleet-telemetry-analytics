import pandas as pd


def compute_vehicle_summary(df):
    """
    Compute per-vehicle performance KPIs.
    """

    summary = df.groupby("vehicle_id").agg(
        avg_speed=("speed", "mean"),
        max_speed=("speed", "max"),
        min_speed=("speed", "min"),
        total_records=("vehicle_id", "count")
    )

    if "acceleration" in df.columns:
        summary["hard_brake_events"] = (
            df[df["acceleration"] < -3]
            .groupby("vehicle_id")
            .size()
        )

    if "disengagement_flag" in df.columns:
        summary["total_disengagements"] = (
            df.groupby("vehicle_id")["disengagement_flag"]
            .sum()
        )

    return summary.fillna(0).reset_index()


def compute_daily_trend(df):
    """
    Compute daily average speed trend.
    """

    df["date"] = pd.to_datetime(df["timestamp"]).dt.date

    daily = df.groupby("date").agg(
        avg_speed=("speed", "mean"),
        total_events=("vehicle_id", "count")
    )

    return daily.reset_index()