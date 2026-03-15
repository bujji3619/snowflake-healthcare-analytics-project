SELECT disease, COUNT(*) AS total_cases
FROM patients
GROUP BY disease
ORDER BY total_cases DESC;