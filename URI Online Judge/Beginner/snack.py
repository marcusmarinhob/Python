# URI ONLINE JUDGE ##############################################
# PROBLEM: 1038 - Snack
# LANGUAGE: Python 3 (Python 3.4.3)
# DEVELOPER: Marcus Marinho
# GITHUB: https://github.com/marcusmarinhob
#################################################################


X, Y = input().split()

productCode = int(X)
numberOfItems = int(Y)

products={
    1: ['Cachorro Quente',4.00],
    2: ['X-Salada',4.50],
    3: ['X-Bacon',5.00],
    4: ['Torrada simples',2.00],
    5: ['Refrigerante',1.50],
}

selectedProduct  = products[productCode]

prod = selectedProduct[0]
price = selectedProduct[1]

total = numberOfItems*price

print('Total: R$ %.2f' % total)
