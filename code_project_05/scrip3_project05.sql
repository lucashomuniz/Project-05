
WITH CTE_Tecnicos AS (SELECT 
c.Country,
COUNT(DISTINCT c.Name) AS Total_Tecnicos,
m.Total AS Total_Medalhas
FROM Coaches c
LEFT JOIN Medals m ON c.Country = m.Team_Country
GROUP BY c.Country, m.Total),

Ranking AS (SELECT *,
ROW_NUMBER() OVER (ORDER BY Total_Tecnicos DESC) AS Rank
FROM CTE_Tecnicos)

SELECT Country, Total_Tecnicos, Total_Medalhas
FROM Ranking
WHERE Rank <= 15
ORDER BY Total_Tecnicos DESC