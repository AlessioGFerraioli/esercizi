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