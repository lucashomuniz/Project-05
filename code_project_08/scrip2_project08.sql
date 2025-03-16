
WITH CTE_Modalidades AS (SELECT 
t.Country,
COUNT(DISTINCT t.Discipline) AS Total_Modalidades,
m.Total AS Total_Medalhas
FROM Teams t
LEFT JOIN Medals m ON t.Country = m.Team_Country
GROUP BY t.Country, m.Total),

Ranking AS (SELECT *,
ROW_NUMBER() OVER (ORDER BY Total_Modalidades DESC) AS Rank
FROM CTE_Modalidades)

SELECT Country, Total_Modalidades, Total_Medalhas
FROM Ranking
WHERE Rank <= 15
ORDER BY Total_Modalidades DESC;