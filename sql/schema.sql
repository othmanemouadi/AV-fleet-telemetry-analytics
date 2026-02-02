-- ClickHouse schema for autonomous vehicle and delivery robot telemetry

CREATE TABLE IF NOT EXISTS av_fleet_telemetry
(
    vehicle_id String,
    timestamp DateTime,
    sensor_type LowCardinality(String),

    speed Float32,
    speed_mps Float32,
    point_count UInt32,

    route_id String,
    ingestion_time DateTime DEFAULT now()
)
ENGINE = MergeTree
PARTITION BY toDate(timestamp)
ORDER BY (vehicle_id, sensor_type, timestamp);
