SELECT state, count(id) from assignments 
GROUP BY state
ORDER BY state ASC;