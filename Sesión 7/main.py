#Escribe esta línea de código:
print("Bienvenidos al entrenamiento con Python, vamos a disfrutar al máximo esta sesión")

"""
    Descuento en una compra:
    Si compras más de $1000, obtienes un descuento del 20%
    Pide el monto de la compra y muestra el precio final
"""

#Pedir datos por el teclado al usuario int entero float decimales string cadenas de caracteres bool booleanos

compra = float(input("Digíte el valor de su compra: "))

#Si compras más de $1000 obtienes un descuento del 20%
#Siempre que la salida tenga más de un cambio de resolución, debo implementar condicionales

#Operadores combinados
#Operadores de asignación =, operadores aritméticos +-*/ , operadores lógicos and y, or o, not
#Operadores de comparación ==, !=, >, <, =>, <=

if compra > 1000:
    descuento = compra * 0.2
    #compra = compra - descuento #Operador de asignación
    compra -= descuento # Operador de asignación compuesto
    print(f"El descuento es de ${descuento}, por lo tanto su valor a pagar es de: ${compra}")
    print()
    print("Que tenga un excelente día, gracias por su compra!")