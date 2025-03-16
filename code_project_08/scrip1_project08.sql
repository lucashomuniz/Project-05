
WITH CTE_Atletas AS (SELECT 
a.Country,
COUNT(DISTINCT a.PersonName) AS Total_Atletas,
m.Total AS Total_Medalhas
FROM Atlhetes a
LEFT JOIN Medals m ON a.Country = m.Team_Country
GROUP BY a.Country, m.Total),

Ranking AS (SELECT *,
ROW_NUMBER() OVER (ORDER BY Total_Atletas DESC) AS Rank
FROM CTE_Atletas)

SELECT Country, Total_Atletas, Total_Medalhas
FROM Ranking
WHERE Rank <= 15
ORDER BY Total_Atletas DESC;