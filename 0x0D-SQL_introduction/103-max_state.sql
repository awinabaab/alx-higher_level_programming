-- Displays the max temperature of each state(ordered by State name)

SELECT state, MAX(value) AS max_temp
FROM temperatures
WHERE value IS NOT NULL
GROUP BY state
ORDER BY state;
