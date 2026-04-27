
def romano_decimal(romano_numero):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(romano_numero)):
        valor_actual = valores[romano_numero[i]]
        
        if i + 1 < len(romano_numero) and valor_actual < valores[romano_numero[i+1]]:
            total -= valor_actual
        else:
            total += valor_actual
            
    return total 

#comprobamos que funcione bien con el numero romano IX, que es igual a 9 en decimal
print(romano_decimal("IX"))