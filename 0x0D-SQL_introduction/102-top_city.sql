-- Displays the top 3 cities temperature during July and August orderd by temperature (descending)

SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE value IS NOT NULL AND month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
