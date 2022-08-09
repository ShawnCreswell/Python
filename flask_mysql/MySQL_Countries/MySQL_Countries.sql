1.

SELECT * FROM languages WHERE language = "Slovene" ORDER BY percentage DESC;

2.

SELECT * FROM cities WHERE country_id >= 1;
SELECT * FROM cities WHERE country_id = (SELECT id FROM countries ORDER by id DESC);

SELECT countries.name AS country, COUNT(cities.id) AS number_cities
FROM countries
JOIN cities ON countries.code = cities.country_code
GROUP BY countries.code
ORDER BY COUNT(cities.id) desc

