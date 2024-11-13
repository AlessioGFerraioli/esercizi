SELECT * 
FROM products
WHERE price > 50


'''
Scrivete una query SQL che restituisca tutti i record dalla tabella "orders"ordinati per data in ordine decrescente.
'''

SELECT *
FROM 'orders'
ORDER BY 'orderDate' DESC

'''
Scrivete una query SQL che aggiorni il prezzo di tutti i prodotti nella tabella"products" aumentandolo del 10%.
'''

UPDATE 'products'
SET 'buyPrice' = 'buyPrice'*1.1;

#Scrivete una query SQL che elimini tutti gli ordini nella tabella "
#orders" con hanno lo stato "Cancelled".

DELETE FROM orderdetails
WHERE orderNumber IN ( 
    SELECT orderNumber 
    FROM orders 
    WHERE status = "Cancelled" );

DELETE FROM orders
WHERE status = "Cancelled";    

#Scrivete una query SQL che restituisca tutti gli utenti dalla tabella"customers"
# il cui nome inizia con la S e vivono in California.

SELECT * 
FROM customers
WHERE state = "CA" 
    and customerName like "S%";


#Si vogliono recuperare dal database "world" la lingua e la nazione di ogni città.
select *
from (JOIN country


#Si vuole recuperare il numero di città per nazione dal database 
#"world" mostrando anche il nome della nazione e 
#ordinando il risultato in base al numero di città.

SELECT country.Name as Name , 
	city.CountryCode,
    COUNT(city.name) as numero_citta 
FROM (country LEFT JOIN 
      city ON 
      city.CountryCode=country.Code)
GROUP BY country.Code;

Si vuole conoscere la lista di repubbliche con aspettativa di vita maggiore dei 70 anni
SELECT country.Name 
FROM country 
WHERE GovernmentForm LIKE "%Rep%"
    AND LifeExpectancy > 70;

#Si vuole recuperare dal database WORLD le lingue parlate per nazione con la rispettiva percentuale di utilizzo;
CREATE VIEW view_lingue AS
SELECT c.Name,
	l.Language, 
	l.Percentage
FROM countrylanguage AS l LEFT JOIN
	country AS c 
    ON l.CountryCode=c.Code;

#Create una vista chiamata PopulationByContinent che mostri il nome del 
#continente e la popolazione totale per ciascun continente.
CREATE VIEW PopulationByContinent AS
SELECT c.Continent, COUNT(c.Population)
FROM country AS c
GROUP BY Continent;

#Create una vista chiamata CapitalCities che mostri il nome dello stato, 
#il nome della sua capitale e la lingua ufficiale
SELECT co.Name as State, 
		cit.Name as Capital, 
		l.Language
FROM (country as co INNER JOIN
	city as cit
    ON co.Capital=cit.ID) INNER JOIN
    countrylanguage as l 
    ON co.Code=l.CountryCode
    WHERE l.IsOfficial = "T";


