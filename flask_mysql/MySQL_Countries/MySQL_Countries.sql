1.

SELECT name, language, percentage FROM countries JOIN languages ON countries.id = languages.country_id 
WHERE languages.language = "Slovene" ORDER by percentage DESC ;

2.

SELECT countries.name AS countries, COUNT(cities.id) AS number_cities 
FROM countries JOIN cities ON countries.id = cities.country_id 
GROUP BY countries.id
ORDER BY COUNT(cities.id) DESC


3.  
SELECT cities.name, cities.population, cities.country_id FROM countries JOIN cities ON countries.id = cities.country_id
WHERE countries.name = "mexico" AND countries.population > 500000
ORDER BY population DESC;

4.
SELECT name, language, percentage FROM countries JOIN languages ON countries.id = languages.country_id 
WHERE languages.percentage > 89
ORDER by percentage DESC ;

5.
SELECT name, surface_area, population FROM countries
WHERE countries.surface_area < 501 AND countries.population > 100000;

6.
SELECT name, government_form, capital, life_expectancy FROM countries
WHERE countries.government_form = "Constitutional Monarchy" AND countries.capital > 200 
AND countries.life_expectancy > 75;

7.
SELECT countries.name, cities.name, cities.district, cities.population FROM countries JOIN cities ON countries.id = cities.country_id
WHERE countries.name = "Argentina" AND cities.district = "Buenos Aires" AND cities.population > 500000;

8.
SELECT countries.region AS region, COUNT(countries.region) AS countries 
FROM countries 
GROUP BY countries.region
ORDER BY COUNT(countries.region) DESC;
