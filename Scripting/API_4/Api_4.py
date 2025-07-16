#Oscar Pérez - DNI: 95656916
#Consigna
#Se espera que, como el profesional a cargo del proceso, puedas resolverlo
#como cualquier candidato que se postule para el puesto. El ejercicio consiste
#en recorrer una serie de números, del 1 al 20, y evaluar las siguientes
#condiciones:

#1. Si el número es divisible por 3, se imprimirá en pantalla el mensaje “Fizz”.
#2. Si el número es divisible por 5, se imprimirá en pantalla el mensaje “Buzz”.
#3. Si el número es divisible por 3 y por 5, se impimirá en pantalla el mensaje “Fizz Buzz”.
#4. Para el resto de los números que no cumple ninguna de las condiciones anteriores, se mostrará en pantalla el mismo número.

def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Llamada a la función con el número máximo
fizz_buzz(100)
        

