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