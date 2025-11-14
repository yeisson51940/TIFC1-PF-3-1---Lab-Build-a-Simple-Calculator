number1 = int(input("Ingrese el primer numero: "))
number2 = int(input("Ingrese el segundo numero: "))

suma = number1 + number2
print("La suma de",{number1},"y",{number2},"es:",{suma})

Resta = number2 - number1
print("Resultado de la resta:", {Resta})

multiplicacion = number1 * number2
print("Resultado de la multiplicacion:", {multiplicacion})

division = number1 / number2
print("Resultado de la division: ", {division})

modulo = number1 % number2
print("Resultado modulo: ", {modulo}) 

number1 = int(input("Ingrese el primer numero: "))
number2 = int(input("Ingrese el segundo numero: "))
operacion = input("Introduce la operación (+, -, *, /): ")
if operacion == '+':
  resultado = number1 + number2
elif operacion == '-':
  resultado = number1 - number2
elif operacion == '*':
  resultado = number1 * number2
elif operacion == '/':
  if number2 != 0:
    resultado = number1 / number2
  else:
    resultado = "No se puede dividir por cero"
elif operacion ==  '%':
    resultado = number1 % number2
else:
  resultado = "Operación no válida"
print("El resultado es:", {resultado}) 

number1 = int(input("Ingrese el primer numero: "))
number2 = int(input("Ingrese el segundo numero: "))
number3 = int(input("Proporciona el tercer numero: "))
sumar = number1 + number2 + number3
print("Resultado de la suma de tres numeros: ", {sumar})