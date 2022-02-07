SELECT category_name, cost_average FROM (
    SELECT adverts.category_name AS category_name, AVG(costs.cost) AS cost_average
    FROM adverts INNER JOIN costs
    BY (adverts.id == costs.id)
    GROUP BY category_name
)
WHERE cost_average < 500;
