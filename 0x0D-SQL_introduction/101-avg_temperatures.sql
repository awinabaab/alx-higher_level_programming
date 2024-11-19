-- Displays the average temperature (Fahrenheit) by city ordered by temperature (descending)

SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE value IS NOT NULL
GROUP BY city
ORDER BY avg_temp DESC;
