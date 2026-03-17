-- Vehicle Performance Summary
SELECT
    vehicle_id,
    COUNT(*) AS total_records,
    AVG(speed) AS avg_speed,
    MAX(speed) AS max_speed,
    MIN(speed) AS min_speed
FROM av_fleet_telemetry
GROUP BY vehicle_id
ORDER BY avg_speed DESC;

-- Hard Braking Events
SELECT
    vehicle_id,
    COUNTIf(acceleration < -3) AS hard_brake_events
FROM av_fleet_telemetry
GROUP BY vehicle_id
ORDER BY hard_brake_events DESC;

-- Daily Average Speed Trend
SELECT
    toDate(timestamp) AS date,
    AVG(speed) AS daily_avg_speed,
    COUNT(*) AS total_events
FROM av_fleet_telemetry
GROUP BY date
ORDER BY date;


-- Disengagement Rate per 100 Miles
SELECT
    vehicle_id,
    SUM(disengagement_flag) AS disengagements,
    SUM(distance_miles) AS total_miles,
    (SUM(disengagement_flag) / SUM(distance_miles)) * 100 AS disengagements_per_100_miles
FROM av_fleet_telemetry
GROUP BY vehicle_id
ORDER BY disengagements_per_100_miles DESC;
