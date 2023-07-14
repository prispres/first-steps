temperatura = float(input("Ingrese temperatura:"))
conversion = input("Es Fahrenheit(F) o Celsius(C)?:").lower()

if conversion == "c":
   fahrenheit = temperatura * 1.8 + 32
   print(fahrenheit)
elif conversion == "f":
   celsius = (temperatura - 32) * 5/9
   print(celsius)
else: 
   print("Escala incorrecta")

"""
Ejercicio que surgio desde la terminal
Ingrese temperatura:
y desarrolle el algoritmo para la conversion
de Celsius a Fahrenheit

Video 43.31
"""