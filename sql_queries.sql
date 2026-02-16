-- Vaccine Cold Chain SQL Queries

-- 1. Show all temperature readings
SELECT *
FROM dbo.Temperature_Readings;

-- 2. High temperature alerts
SELECT *
FROM dbo.Temperature_Readings
WHERE temperature > 8;

-- 3. Average temperature
SELECT AVG(temperature) AS avg_temp
FROM dbo.Temperature_Readings;

-- 4. Join readings with sensor locations
SELECT
    t.timestamp,
    t.temperature,
    s.location
FROM dbo.Temperature_Readings t
JOIN Sensors s
ON t.sensor_id = s.sensor_id;

-- 5. Locations with most alerts
SELECT
    s.location,
    COUNT(*) AS issues
FROM dbo.Temperature_Readings t
JOIN Sensors s
ON t.sensor_id = s.sensor_id
WHERE t.temperature > 8
GROUP BY s.location
ORDER BY issues DESC;
